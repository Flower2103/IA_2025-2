import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.models import Model
import os

# ------------------------------
# CONFIGURACIÓN
# ------------------------------
IMG_SIZE = 224
BATCH_SIZE = 16
EPOCHS = 15
DATASET_DIR = "dataset"

# Verifica clases automáticamente
CLASSES = sorted(os.listdir(DATASET_DIR))
NUM_CLASSES = len(CLASSES)
print("CLASES DETECTADAS:", CLASSES)

# ------------------------------
# DATA AUGMENTATION
# ------------------------------
train_datagen = ImageDataGenerator(
    rescale=1/255.0,
    validation_split=0.2,
    rotation_range=25,
    width_shift_range=0.15,
    height_shift_range=0.15,
    brightness_range=[0.8, 1.2],
    zoom_range=0.20,
    horizontal_flip=True
)

train_gen = train_datagen.flow_from_directory(
    DATASET_DIR,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    subset="training"
)

val_gen = train_datagen.flow_from_directory(
    DATASET_DIR,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    subset="validation"
)

# ------------------------------
# CARGAR MODELO BASE
# ------------------------------
base_model = MobileNetV2(
    weights="imagenet",
    include_top=False,
    input_shape=(IMG_SIZE, IMG_SIZE, 3)
)

# Congelar capas iniciales para evitar sobreentrenamiento
base_model.trainable = False

# ------------------------------
# CAPAS PERSONALIZADAS
# ------------------------------
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(256, activation="relu")(x)
x = Dropout(0.3)(x)
x = Dense(128, activation="relu")(x)
x = Dropout(0.3)(x)
predictions = Dense(NUM_CLASSES, activation="softmax")(x)

model = Model(inputs=base_model.input, outputs=predictions)

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.0005),
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

model.summary()

# ------------------------------
# ENTRENAMIENTO
# ------------------------------
history = model.fit(
    train_gen,
    validation_data=val_gen,
    epochs=EPOCHS
)

# ------------------------------
# GUARDAR MODELO
# ------------------------------
os.makedirs("modelo", exist_ok=True)
model.save("modelo/modelo_perros_cnn.keras")

print("Modelo guardado en modelo/modelo_perros_cnn.keras")
