import os
from rembg import remove
from PIL import Image

dataset_origen = "dataset"
dataset_destino = "dataset_nofondo"

for raza in os.listdir(dataset_origen):
    carpeta_origen = os.path.join(dataset_origen, raza)
    carpeta_destino = os.path.join(dataset_destino, raza)
    os.makedirs(carpeta_destino, exist_ok=True)
    
    for img_name in os.listdir(carpeta_origen):
        ruta_img = os.path.join(carpeta_origen, img_name)
        with open(ruta_img, "rb") as f:
            input_img = f.read()
        output_img = remove(input_img)
        
        # Guardar imagen procesada
        base, _ = os.path.splitext(img_name)
        ruta_guardado = os.path.join(carpeta_destino, base + ".png")
        with open(ruta_guardado, "wb") as f:
            f.write(output_img)
