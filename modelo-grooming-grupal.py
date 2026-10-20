import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

# Mensajes del dataset
mensajes = [
    "¿Cuántos años tenés?",
    "No le digas a nadie que hablamos.",
    "Hola, ¿cómo estás?",
    "¿Querés jugar algo online?",
    "Sos muy linda, no le muestres esto a tus papás.",
    "¿Terminaste la tarea de matemáticas?",
    "Podés mandarme una foto tuya, pero que sea solo para mí.",
    "¿Querés que te ayude con el juego que no podías pasar?",
    "No le contés a nadie que hablamos por acá, ¿sí?",
    "¿Te gustó la película de ayer?",
    "¿Estás solo en casa ahora?",
    "¿Querés hacer una videollamada para estudiar juntos?",
    "No le digas a tus padres que te escribí, es nuestro secreto.",
    "¿Cómo te fue en el examen de historia?",
    "Mandame una foto tuya, pero que nadie más la vea.",
    "¿Jugamos Minecraft esta tarde?",
    "Sos muy especial para mí, no le cuentes a nadie lo que hablamos.",
    "¿Querés que te pase los apuntes de biología?",
    "¿Podés mostrarme cómo estás vestida ahora?",
    "¿Tenés ganas de salir a andar en bici mañana?",
    "No hace falta que le digas a nadie que hablamos tanto.",
    "¿Querés que estudiemos juntos para el parcial?"
]

# Etiquetas
etiquetas = [
    "grooming",
    "grooming",
    "no_grooming",
    "no_grooming",
    "grooming",
    "no_grooming",
    "grooming",
    "no_grooming",
    "grooming",
    "no_grooming",
    "grooming",
    "no_grooming",
    "grooming",
    "no_grooming",
    "grooming",
    "no_grooming",
    "grooming",
    "no_grooming",
    "grooming",
    "no_grooming",
    "grooming",
    "no_grooming"
]

# Crear DataFrame
df = pd.DataFrame({
    "mensaje": mensajes,
    "etiqueta": etiquetas
})

# Convertir texto a numeros
vectorizador = CountVectorizer()
X = vectorizador.fit_transform(df["mensaje"])

# Variable objetivo
y = df["etiqueta"]

# Separar datos para entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Crear modelo
modelo = MultinomialNB()

# Entrenar modelo
modelo.fit(X_train, y_train)

# Realizar predicciones sobre los datos de prueba
y_pred = modelo.predict(X_test)

# Calcular accuracy
# Accuracy:
# Mide el porcentaje de predicciones correctas.
# Formula: aciertos / total de ejemplos.
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Mostrar reporte de clasificacion
# Classification Report:
# Resume el rendimiento del modelo para cada clase.
# Precision: de todo lo que predijo como una clase, cuanto acerto.
# Recall: de todos los casos reales de una clase, cuantos encontro.
# F1-score: promedio entre precision y recall.
print("\nReporte de clasificacion:")
print(classification_report(y_test, y_pred))

# Mostrar matriz de confusion
# Confusion Matrix:
# Muestra cuantos ejemplos clasifico bien y cuantos confundio.
# Permite ver exactamente donde comete errores.
print("\nMatriz de confusion:")
print(confusion_matrix(y_test, y_pred))

# Mensajes nuevos para clasificar
mensajes_nuevos = [
    "¿Podes mandarme una foto tuya? No se la muestres a nadie.",
    "¿Jugamos Minecraft esta tarde?",
    "No le digas a tus papas que hablamos, ¿si?",
    "¿Terminaste el trabajo practico de historia?"
]

# Transformar mensajes nuevos
X_nuevo = vectorizador.transform(mensajes_nuevos)

# Predecir clases
predicciones = modelo.predict(X_nuevo)

resultado = pd.DataFrame({
    "Mensaje": mensajes_nuevos,
    "Prediccion": predicciones
})

print(resultado)
print("\nClasificacion de mensajes nuevos:")
for mensaje, pred in zip(mensajes_nuevos, predicciones):
    print(f"{mensaje} --> {pred}")

print(X_train.shape)
print(X_test.shape)
# Calcular aciertos y errores
aciertos = (y_test == y_pred).sum()
errores = (y_test != y_pred).sum()

# Grafico de barras
plt.figure(figsize=(6, 4))

plt.bar(
    ["Aciertos", "Errores"],
    [aciertos, errores],
    color=["green", "red"]
)

plt.title("Resultado del modelo")
plt.ylabel("Cantidad de mensajes")

plt.show()