from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
import os
from werkzeug.utils import secure_filename
from tensorflow.keras.preprocessing.image import load_img, img_to_array # type: ignore
import base64
import io
from io import BytesIO
from PIL import Image
from rembg import remove


app = Flask(__name__)

# ------------------------------
#  Cargar modelo
# ------------------------------
MODEL_PATH = "modelo/modelo_perros_cnn.keras"

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError("NO SE ENCONTRÓ EL MODELO. ENTRENALO CON train_model.py")

model = tf.keras.models.load_model(MODEL_PATH)

# Cargar nombres de clases desde las carpetas del dataset
dataset_path = "dataset_nofondo"
CLASSES = sorted(os.listdir(dataset_path))
print("CLASES:", CLASSES)

def quitar_fondo(ruta_imagen):
    with open(ruta_imagen, "rb") as f:
        input_img = f.read()

    output_img = remove(input_img)

    # Crear ruta nueva correctamente
    base, ext = os.path.splitext(ruta_imagen)
    output_path = base + "_nofondo.png"

    with open(output_path, "wb") as f:
        f.write(output_img)

    return output_path


# ------------------------------
#  Ruta principal
# ------------------------------
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# ------------------------------
#  Ruta de predicción
# ------------------------------
@app.route("/predict", methods=["POST"])
def predict():
    image_b64 = request.form.get("image")

    if not image_b64:
        return render_template("index.html", error="No se recibió ninguna imagen ajustada")

    # Decodificar imagen base64
    image_data = base64.b64decode(image_b64.split(",")[1])
    input_img = io.BytesIO(image_data)

    # ------------------------------
    #  Quitar fondo directamente en memoria
    # ------------------------------
    # force_return_bytes=True evita el error _io.BytesIO not supported
    output_img = remove(input_img.read(), force_return_bytes=True)
    img = Image.open(io.BytesIO(output_img)).convert("RGB")
    img = img.resize((224, 224))

    # ------------------------------
    #  Preparar imagen para predicción
    # ------------------------------
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # ------------------------------
    #  Predicción
    # ------------------------------
    pred = model.predict(img_array, verbose=0)[0]
    idx = np.argmax(pred)
    confianza = float(pred[idx])

    THRESHOLD = 0.50
    raza = CLASSES[idx] if confianza >= THRESHOLD else "Raza no encontrada"
    confianza = round(confianza * 100, 2)

    # ------------------------------
    #  Convertir imagen final a base64 para mostrarla en la web
    # ------------------------------
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    final_image_b64 = "data:image/png;base64," + base64.b64encode(buffered.getvalue()).decode()

    return render_template(
        "index.html",
        prediccion=raza,
        confianza=confianza,
        final_image=final_image_b64
    )


if __name__ == "__main__":
    app.run(debug=True)