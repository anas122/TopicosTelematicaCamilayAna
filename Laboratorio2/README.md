# Info de la materia: ST0263 Tópicos Especiales en Telemática
#
# Estudiante(s): Ana Sofia Arango Gonzalez, asarangog@eafit.edu.co y Camila Mejia Muñoz, cmejiam10@eafit.edu.co
#
# Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co
#
# Laboratorio 2
#
# 1. Breve descripción de la actividad
Implementación de un cliente simulador de eventos IoT que envia los datos a un servidor a través de un Middleware Orientado a Mensajes (MOM), en este caso RabbitMQ, y finalmente se visualizan en la plataforma Ubidots.

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
Se cumplieron y desarrollaron todos los aspectos de la actividad propuesta por el profesor. Se implementó el simulador de eventos IoT que envia los datos a través del MOM RabbitMQ, aquí se almacenan y posteriormente un consumidor consume estos datos y los visualiza en la plataforma Ubidots. Además, se elaboró el mapa mental del protocolo AMQP.

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
Todos los aspectos se cumplieron y desarrollaron.

# 2. Información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.
El proyecto está compuesto por un productor, el cual se encarga de envíar los datos y un consumidor, el cual se encarga de recuperar los datos para luego visualizarlos. Como mejores prácticas se utilizó el Single Responsibility Principle. 

# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.
Python 3.10.6  
Libreria pika versión de Python 3.10.6  
Libreria time versión de Python 3.10.6  
Libreria requests versión de Python 3.10.6  
Libreria math versión de Python 3.10.6  
Libreria random versión de Python 3.10.6

## Como se compila y ejecuta.
1. Se inicializa el docker y se corre el servidor.
2. Se debe conectar a la interfaz de RabbitMQ con el respectivo usuario y contraseña y crear la queue y exchange necesarias y conectarlas entre ellas usando bind.
3. Se ejecuta el archivo "producer.py" con el comando `python3 producer.py` para generar y enviar los datos. Este se puede ejecutar las veces que se quiera, dependiendo de la cantidad de datos que se quiera generar.
4. Se ejecuta el archivo "consumer.py" con el comando `python3 consumer.py` para recuperar los datos y posteriormente mostrarlos en Ubidots.
5. Se accede a la plataforma Ubidots para visualizar los datos.

## Detalles del desarrollo y técnicos.
El archivo "producer.py" se encarga de generar los valores aleatoriamente y se conecta con el RabbitMQ para luego enviarlos al exchange, que los llevará a la queue. El archivo "consumer.py" se encarga de recuperar los datos de RabittMQ, luego se conecta a Ubidots y los muestra.

## Descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)
Para la dirección IP se utiliza la IP elástica de la instancia creada en AWS.  
Para el exchange se pone el nombre de este creado en la interfaz de RabbitMQ.  
Para la conexión con RabbitMQ se pone el usuario y la contraseña correspondiente.  
Para el Token se utiliza el correspondiente a la cuenta de Ubidots.  
Para el device_label se utiliza el dispositivo donde se encuentran los datos en Ubidots.  
Para el variable_label se pone el nombre de la variable que se va a enviar.
## 

# 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.
Python 3.10.6  
Libreria pika versión de Python 3.10.6  
Libreria requests versión de Python 3.10.6

# IP o nombres de dominio en nube o en la máquina servidor.
IP elástica de la máquina servidor: 3.220.79.140

## Descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)
En la instancia de AWS se debe habilitar el ingreso de tráfico TCP en el puerto 5672 y 15672, en el grupo de seguridad.

## Como se lanza el servidor.
Para lanzar el servidor se ejecuta el comando `sudo docker run -d --hostname my-rabbit -p 15672:15672 -p 5672:5672 --name rabbit-server -e RABBITMQ_DEFAULT_USER=user -e RABBITMQ_DEFAULT_PASS=password rabbitmq:3-
management`

## Una mini guia de como un usuario utilizaría el software o la aplicación
1. Se inicializa el docker y se corre el servidor.
2. Se debe conectar a la interfaz de RabbitMQ con el respectivo usuario y contraseña y crear la queue y exchange necesarias y conectarlas entre ellas usando bind.
3. Se ejecuta el archivo "producer.py" con el comando `python3 producer.py` para generar y enviar los datos. Este se puede ejecutar las veces que se quiera, dependiendo de la cantidad de datos que se quiera generar.
4. Se ejecuta el archivo "consumer.py" con el comando `python3 consumer.py` para recuperar los datos y posteriormente mostrarlos en Ubidots.
5. Se accede a la plataforma Ubidots para visualizar los datos.

## Resultados o pantallazos 
![image](https://user-images.githubusercontent.com/37346028/191346490-df3a54be-81ba-4307-99c2-796b05ac5c9b.png)
![image](https://user-images.githubusercontent.com/37346028/191347016-54bcf56f-1e17-4583-a392-8d371c3d4aed.png)
![image](https://user-images.githubusercontent.com/37346028/191347074-3746c14c-0ca7-431b-8475-fb1bad550d22.png)
![image](https://user-images.githubusercontent.com/37346028/191347136-fe24bc45-8b02-40b0-b572-190a99d24645.png)
![image](https://user-images.githubusercontent.com/37346028/191347204-a1a8c479-be9f-4b8b-a865-8cd84c607dfe.png)

# 5. otra información que considere relevante para esta actividad.
![image](https://user-images.githubusercontent.com/37346028/191347286-0ab0dffc-6083-47e8-998b-fc9e5463f09d.png)

# Referencias:
## https://help.ubidots.com/en/articles/569964-simulate-data-in-ubidots-using-python

#### versión README.md -> 1.0 (2022-agosto)
