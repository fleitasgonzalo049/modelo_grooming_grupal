# Detector de Grooming con Naive Bayes

Este repositorio contiene un modelo de clasificación de texto basado en **Naive Bayes** y técnicas de procesamiento de lenguaje natural (PLN) para la detección automática de patrones de *grooming* en mensajes de texto.

## 👥 Autores
* **Demey Gustavo**
* **Fleitas Gonzalo**

---

## 📊 Resumen del Rendimiento del Modelo

* **Precisión General (Accuracy):** **0.80** (80%) sobre el conjunto de prueba. El modelo evaluó 5 mensajes nuevos no vistos previamente, logrando 4 clasificaciones correctas y 1 error.
* **Técnicas Utilizadas:** 
  * Algoritmo de clasificación *Naive Bayes*.
  * Vectorización de texto mediante `CountVectorizer`.
  * División de datos de entrenamiento y prueba (`train_test_split`).

### 📈 Reporte de Clasificación

| Clase | Precision | Recall | F1-score |
| :--- | :---: | :---: | :---: |
| **Grooming** | 1.00 | 0.67 | 0.80 |
| **No Grooming** | 0.67 | 1.00 | 0.80 |

* **Matriz de Confusión:**
  ```text
  [[2, 1],
   [0, 2]]
