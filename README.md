# Tutorial API REST- Flask (cipher/decipher)
API REST - Flask. Esta es una API básica que proporciona 2 endpoints, para cifrar y descifrar información utilizando el algoritmo RC4 utilizando en WEP. Esta aplicación está desarrollada para el curso de Desarrollo de Soluciones Cloud. 

# Ejecución 
Para ejecutar la aplicación siga las siguientes instrucciones: 

## Crear un nuevo ambiente virtual
* ```$ python3 -m venv nuevo_ambiente```
* ```$ source nuevo_ambiente/bin/activate```

## Instalar las dependencias
* ```$ pip install flask``` 
* ```$ pip install flask-restful```
* ```$ pip install flask-marshmallow```

## Configurar variables de entorno
* ```$ export FLASK_APP=app.py```
* ```$ export FLASK_DEBUG=1```
* ```$ export FLASK_ENV=development```

## Ejecutar
* ```$ flask run -h 0.0.0.0```

## Consumir los servicios
* Utilice Postman (o una herramienta equivalente) para realizar solicitudes post a los endpoints disponibles. 
* Ruta Endpoint 1 [POST]: ```http://ip_servidor:5000/cipher```
* Ruta Endpoint 2 [POST]: ```http://ip_servidor:5000/decipher```
* Ambos Endpoints requieren un JSON con el siguiente formato:  
```{"message" : "Texto a Cifrar/Descifrar", "key": "llave para Cifrar/Descifrar"}```

## Pruebas de Carga (Básicas)
### Instalar Apache Benchmark
* ```$ sudo apt-get install apache2-utils```  
### Crear archivos JSON
* Crear un archivo JSON de ejemplo (En el repositorio encontrará un par de ejemplos disponibles):  
```{"message" : "Texto a Cifrar/Descifrar", "key": "llave para Cifrar/Descifrar"}```
### Ejecución del comando 
* ```$ ab -n 1000 -c 100 -p data-cifrar.json -T application/json -rk http://ip_servidor:5000/cipher```
* ```$ ab -n 1000 -c 100 -p data-descifrar.json -T application/json -rk http://ip_servidor:5000/decipher```  

donde:
* ```-k (keepAlive)```. Realizar múltiples solicitudes dentro de una sesión HTTP, funcionalidad de los navegadores por la naturaleza
* ```-r (flag)```. Indica que la conexión (socket) no se cierra al recibir errores
* ```-n (requests)```. Número total de solicitudes para ejecutar
* ```-c (concurrency)```. Cantidad de conexiones concurrentes
* ```-p (file.json)```. JSON que se envia en el cuerpo del request
* ```-T application/json```. Especifica la estructura de datos del body


# Cifrado RC4 basado en el proyecto:
* [https://github.com/g2jun/RC4-Python](https://github.com/g2jun/RC4-Python)
