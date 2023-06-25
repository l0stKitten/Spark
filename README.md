# Spark
## Colaboratory
Para el colaboratory se utilizó el ejemplo proporcionado en clase. Por lo cual solo faltaba encontrar el datset. El dataset obtenido es de movielens obtenido desde kaggle el cual cuenta con con 27.000.000 valoraciones a 58.000 películas por 280.000 usuarios. Los archivos estaban por separado siendo las películas y los ratings por usuario archivos diferentes, antes de procesar los datos se revisaron y se unieron por medio del ID de las películas. El archivo final con el que se trabajó el modelo es MovieUserRating.csv. En la última conjunto de código se especifica en la variable id_to_retrieve al usuario al que se le recomendará películas según los rating que dió.

## VM
Para las máquinas virtuales se utilizó el código del colab también excluyendo la parte del dataset que ya tenemos unido. También se siguieron los pasos del instructivo sin problemas. Para subir el programa a Spark se tuvieron dificultados sin embargo se encontró solución en el siguiente artículo: https://sparkbyexamples.com/spark/spark-submit-command/?expand_article=1.

Dado que estamos manejando un cluster se debe especificar 
```
--deploy-mode cluster
```

También se debe especificar que clúster es el manager, por lo que se debe colocar la etiqueta de master, además de especificar que el administrador de cluster el cuál es en este caso el mismo spark, para lo cual se coloca la dirección ip del host y el puerto. Datos que se configuraron en el instructivo.
```
--master spark://HOST:PORT
```

Finalmente como estamos trabajando con pySpark la línea para especificar los archivos que se compartirán es diferente. Se coloca la etiqueta --py-files seguido del nombre de los archivos a compartir.
```
--py-files file1.py,file2.py,file3.zip
```
