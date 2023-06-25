# Spark
Nombre: Daria López Franco
Los archivos se encuentran en la rama l0stKitten-patch-1
## Colaboratory
Para el colaboratory se utilizó el ejemplo proporcionado en clase. Por lo cual solo faltaba encontrar el datset. El dataset obtenido es de movielens obtenido desde kaggle el cual cuenta con con 27.000.000 valoraciones a 58.000 películas por 280.000 usuarios. Los archivos estaban por separado siendo las películas y los ratings por usuario archivos diferentes, antes de procesar los datos se revisaron y se unieron por medio del ID de las películas. El archivo final con el que se trabajó el modelo es MovieUserRating.csv. En la última conjunto de código se especifica en la variable id_to_retrieve al usuario al que se le recomendará películas según los rating que dió.

## VM
Para las máquinas virtuales se utilizó el código del colab también excluyendo la parte del dataset que ya tenemos unido. También se siguieron los pasos del instructivo sin problemas. Para subir el programa a Spark se tuvieron dificultades, se encontró información relevante en el siguiente artículo: https://sparkbyexamples.com/spark/spark-submit-command/?expand_article=1. Como el especificar cuál será el adminsitrador del cluser y también especificar los archivos que se compartirán.

![1](https://github.com/l0stKitten/Spark/assets/92339980/cc9110bb-e2a9-4164-825e-199cb32f4dd1)

Se debe especificar quién manejará el cluster para la aplicación, por lo que se debe colocar la etiqueta de master, además de especificar que el administrador de cluster el cuál es en este caso el mismo spark, para lo cual se coloca la dirección ip del host y el puerto. Datos que se configuraron en el instructivo.
```
--master spark://HOST:PORT
```

Al estar trabajando con pySpark la línea para especificar los archivos que se compartirán es diferente. Se coloca la etiqueta --py-files seguido del nombre de los archivos a compartir.
```
--py-files file1.py,file2.py,file3.zip
```

Sin embargo, no para resolver el error los archivos se tuvieron que copiar en el mismo directorio en el que se encuentran en el nodo master. Por lo que el comanddo para ejecutar el código es:
```
spark-submit <Nombre del archivo>
```
El colocar o no datos adicionales no afectó en nada.

El código utilizado es el mismo usado en el colab (FilmRecommendc.py). Al igual que en el colab para cambiar la recomendación del usuario hay que editar el archivo colocando la ID deseada.

### Resultados
En el ejemplo del colab, al usuario 1 se le recomienda Pulp Fiction, mientras que al ejecutarlo en la máquina virtual se le recomendó Forest Gump. Además cabe resaltar que toma alrededor de 10min la ejecución en la máquina virtual. Se estima mejorar ese tiempo agregando más nodos al clúster.

![image](https://github.com/l0stKitten/Spark/assets/92339980/b1ac5e41-2e02-4929-84e5-49a1c96a29b6)


