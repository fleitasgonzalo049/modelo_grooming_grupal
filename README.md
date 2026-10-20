Detector de Grooming con Naive Bayes

Este repositorio contiene un modelo de clasificación de texto basado en Naive Bayes y técnicas de procesamiento de lenguaje natural (PLN) para la detección automática de patrones de grooming en mensajes de texto.   
TXT
👥 Autores

    Demey Gustavo

       
    TXT

    Fleitas Gonzalo

       
    TXT

📊 Resumen del Rendimiento del Modelo

    Precisión General (Accuracy): 0.80 (80%) sobre el conjunto de prueba. El modelo evaluó 5 mensajes nuevos no vistos previamente, logrando 4 clasificaciones correctas y 1 error.   
    TXT+ 1

    Técnicas Utilizadas:

        Algoritmo de clasificación Naive Bayes.   
        TXT

        Vectorización de texto mediante CountVectorizer.   
        TXT

        División de datos de entrenamiento y prueba (train_test_split).   
        TXT

📈 Reporte de Clasificación
Clase	Precision	Recall	F1-score
Grooming	

1.00
TXT
	

0.67
TXT
	

0.80
TXT
No Grooming	

0.67
TXT
	

1.00
TXT
	

0.80
TXT

    Matriz de Confusión:
    Plaintext

    [[2, 1],
     [0, 2]]

    (El modelo identificó correctamente 2 mensajes de grooming y 2 mensajes legítimos, registrando un falso negativo donde un mensaje de grooming fue clasificado como no peligroso).   
    TXT

🔍 Ejemplos de Clasificación de Nuevos Mensajes

El modelo demostró capacidad para identificar patrones asociados con secreto, aislamiento o solicitud de material sensible:   
TXT

    ¿Podes mandarme una foto tuya? No se la muestres a nadie. → grooming

       
    TXT

    No le digas a tus papas que hablamos, ¿si? → grooming

       
    TXT

    ¿Jugamos Minecraft esta tarde? → no_grooming

       
    TXT

    ¿Terminaste el trabajo practico de historia? → no_grooming

       
    TXT

📌 Conclusión

El proyecto demuestra que es viable utilizar modelos de Naive Bayes junto con enfoques de PLN para detectar conductas de riesgo en comunicaciones textuales. Si bien el rendimiento actual es equilibrado y prometedor (80% de accuracy), futuras iteraciones se beneficiarán de la ampliación del conjunto de datos de entrenamiento.   
TXT+ 1
