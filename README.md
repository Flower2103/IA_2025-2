# 🐕 Clasificación de Razas de Perros con IA — Proyecto 2025-2

## 📌 Objetivo General
Desarrollar una aplicación web que permita al usuario subir imágenes (JPEG, JPG, PNG) de perros de las razas **Pastor Alemán**, **Pastor Belga Malinois**, **Pastor de Anatolia** o **criollos**, con el propósito de implementar y evaluar un modelo de Inteligencia Artificial que identifique la raza del perro.  
Este proyecto aplica los conocimientos adquiridos en la asignatura de Inteligencia Artificial (periodo 2025-2).

---

## 📌 Descripción del Problema
Muchas personas no cuentan con la experiencia o conocimientos suficientes para identificar la raza de su perro, especialmente cuando fue adoptado, regalado o rescatado. Desconocer la raza puede llevar a ignorar necesidades específicas relacionadas con:

- comportamiento  
- salud  
- alimentación  
- características físicas  

Por ello, este proyecto busca crear una herramienta que permita identificar la raza de un perro a partir de una imagen, facilitando a los usuarios comprender mejor a su mascota y mejorar su cuidado, mientras se aplican técnicas de IA.

---

# 📂 Base de Datos Utilizada

### 📌 Fuente
Las imágenes se obtuvieron de:  
**https://www.gettyimages.com.mx/**  

Razas buscadas:

- Pastor Belga Malinois  
- Pastor Alemán  
- Golden Retriever 

---

### 📌 Número de imágenes actuales

| Raza                     | Imágenes |
|--------------------------|----------|
| Pastor Alemán            | 200      |
| Pastor Belga Malinois    | 200      |
| Golden Retriever          | 200 |


---

### 📌 Estructura de los datos
- Imágenes seleccionadas mostrando únicamente al perro.
- Variación de edad, poses, iluminación y movimiento.
- Tamaño final: **224×224 px**.
- Fondo eliminado mediante **rembg**.
- Imágenes organizadas en carpetas por raza.

---

# 🧹 Tratamiento de los Datos

### 1️⃣ Redimensionamiento  
Todas las imágenes se ajustan al tamaño **224×224 px**, requerido por la CNN.

### 2️⃣ Normalización  
Los valores de píxel se escalan al rango **0–1** dividiendo entre 255.

### 3️⃣ Filtrado y limpieza  
Se eliminan imágenes:

- borrosas  
- incompletas  
- con objetos o personas  
- con baja resolución  

### 4️⃣ Aumento de Datos (Data Augmentation)
Incluye transformaciones como:

- rotación  
- zoom  
- desplazamientos  
- brillo  
- volteo horizontal  

---

## ✔️ Justificación del preprocesamiento

| Paso | Razón |
|------|--------|
| **Redimensionamiento** | Garantiza compatibilidad con el modelo y uniformidad. |
| **Normalización** | Mejora la estabilidad del entrenamiento y acelera la convergencia. |
| **Filtrado** | Aumenta la calidad del dataset y evita confusiones al modelo. |
| **Data Augmentation** | Reduce el sobreajuste y mejora la generalización. |

---

# 🤖 Modelo de IA Propuesto

### 📌 Tipo de modelo  
Se utiliza una **Red Neuronal Convolucional (CNN)** basada en **MobileNetV2** mediante *Transfer Learning*, añadiendo capas densas personalizadas para la clasificación.

### 📌 Justificación
- Las **CNN** son ideales para tareas de reconocimiento de imágenes.  
- MobileNetV2 es eficiente, liviano y preciso.  
- El *transfer learning* reduce el tiempo de entrenamiento y mejora resultados con pocos datos.

> *“Las redes neuronales convolucionales impulsan el reconocimiento de imágenes y las tareas de visión artificial.”* — IBM

### 📌 Comparación con otros modelos  
Por ahora solo se utiliza MobileNetV2.

---

# 🚧 Progreso Actual

✔ Dataset de 2 razas recolectado  
✔ Preprocesamiento aplicado  
✔ Entrenamiento inicial completado  
✔ Pruebas con éxito en perro real (Pastor Belga Malinois → 100% de acierto)  
✔ Integración con aplicación web Flask  

🔧 A mejorar:  
- La calidad del dataset de Pastor Alemán  
- Manejo de razas no incluidas (criollos)

Cuando el usuario carga una imagen en la interfaz, el sistema la ajusta automáticamente a **224×224 px**.

---

# 📅 Tareas Pendientes

- Revisar el dataset de Pastor Alemán y reemplazar imágenes de baja calidad.  
- Añadir 200+ imágenes de Pastor Anatolia.  
- Añadir 200+ imágenes de perros criollos.  
- Implementar un umbral de confianza para clasificar posibles perros criollos.  
- Mejorar la interfaz web.  
- Continuar evaluando la efectividad del modelo.

---

