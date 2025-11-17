# Microservicio de Usuarios con Docker Compose

Este proyecto demuestra la creación de un microservicio independiente utilizando Flask (Python) y una base de datos MySQL, orquestados mediante Docker Compose. El objetivo es mostrar los principios básicos de los microservicios y cómo se comunican entre sí a través de contenedores Docker.

## Tecnologías utilizadas
- Python 3.10
- Flask
- MySQL
- Docker
- Docker Compose

## Funcionalidad del microservicio

El microservicio expone dos rutas:

### GET /
Devuelve un mensaje indicando que el servicio está funcionando:
<img width="740" height="272" alt="Image" src="https://github.com/user-attachments/assets/17e8c347-5037-4f1d-8d1c-e3c3097fe0e4" />
### GET /usuarios
Se conecta al contenedor MySQL, consulta los nombres almacenados en la tabla usuarios y devuelve la lista en formato JSON:
<img width="1110" height="237" alt="Image" src="https://github.com/user-attachments/assets/c6286b73-d79c-489b-8a77-afecc12bf704" />
## Cómo ejecutar el proyecto
1. Clonar el repositorio
2. Construir y ejecutar los contenedores
```bash
docker-compose up --build
```
3. Acceso al microservicio
```bash
http://localhost:5000/
```
Lista de usuarios:
```bash
http://localhost:5000/usuarios
```
###  Inicialización de la base de datos
Se crea la tabla dentro del cliente MySQL:
```bash
USE usuarios_db;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100)
);

INSERT INTO usuarios (nombre) VALUES ('Juan'), ('Ana'), ('Carlos');

```
### Comandos usados para revisar la funcionalidad de los contenedores
Ver contenedores en ejecución:
```bash
docker ps
```
Detener los contenedores:
```bash
docker-compose down
```
Reconstruir contenedores:
```bash
docker-compose up --build
```
Detener contenedores sin eliminar volúmenes:
```bash
docker-compose stop
```
Ver logs de un servicio:
```bash
docker logs practica-usuarios-1
```

Todos los contenedores que se usan se pueden visualizar en docker desktop, para verificar si estan funcionando correctamente de la sigueitne manera:
<img width="2553" height="977" alt="Image" src="https://github.com/user-attachments/assets/3b93705a-5666-4846-a146-e7babd39d159" />
