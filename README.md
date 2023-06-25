# Spark
## Colaboratory
Para el colaboratory se utilizó el ejemplo proporcionado en clase. Por lo cual solo faltaba encontrar el datset. El dataset obtenido es de movielens obtenido desde kaggle el cual cuenta con con 27.000.000 valoraciones a 58.000 películas por 280.000 usuarios. Los archivos estaban por separado siendo las películas y los ratings por usuario archivos diferentes, antes de procesar los datos se revisaron y se unieron por medio del ID de las películas. El archivo final con el que se trabajó el modelo es MovieUserRating.csv. En la última conjunto de código se especifica en la variable id_to_retrieve al usuario al que se le recomendará películas según los rating que dió.

## VM
Para las máquinas virtuales se utilizó el código del colab también excluyendo la parte del dataset que ya tenemos unido. También se siguieron los pasos del instructivo sin problemas. Para subir el programa a Spark se tuvieron dificultades, se encontró información relevante en el siguiente artículo: https://sparkbyexamples.com/spark/spark-submit-command/?expand_article=1. Como el especificar cuál será el adminsitrador del cluser y también especificar los archivos que se compartirán.

![alt text]([notion://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F16031a23-c096-43f2-9c4f-1b77cde1ff31%2FUntitled.png?table=block&id=eab6194f-afe4-4d23-9fbb-7c54b1dc103d&spaceId=19445f3d-5547-49dc-ab9b-6425816851e5&width=2000&userId=60c0996e-5dbe-4927-8dbc-de3f19329f3c&cache=v2](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F16031a23-c096-43f2-9c4f-1b77cde1ff31%2FUntitled.png?id=eab6194f-afe4-4d23-9fbb-7c54b1dc103d&table=block&spaceId=19445f3d-5547-49dc-ab9b-6425816851e5&width=2000&userId=60c0996e-5dbe-4927-8dbc-de3f19329f3c&cache=v2))


Se debe especificar quién manejará el cluster para la aplicación, por lo que se debe colocar la etiqueta de master, además de especificar que el administrador de cluster el cuál es en este caso el mismo spark, para lo cual se coloca la dirección ip del host y el puerto. Datos que se configuraron en el instructivo.
```
--master spark://HOST:PORT
```

Al estar trabajando con pySpark la línea para especificar los archivos que se compartirán es diferente. Se coloca la etiqueta --py-files seguido del nombre de los archivos a compartir.
```
--py-files file1.py,file2.py,file3.zip
```

Sin embargo, no para resolver el error los archivos se tuvieron que copiar en el mismo directorio en el que se encuentran en el nodo master.

