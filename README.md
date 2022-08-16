# Challenge - Melissa Vargas
## Descripción General
***
Esta aplicación fue diseñada para obtener una información del proveedor y disponibilizarla a los Usuarios autorizados del área de Compras equipos de la empresa y a otros terceros previamente autorizados a través de APIs. 

Estas son algunas de las consideraciones que cubre la aplicación:

* Proteger los datos Según su clasificación (Tarjetas de Crédito válidas, Sensibles de los clientes)
* Cumplir con las normas PCI DSS y Habeas Data Aplicables según el tipo de información manejada
* Almacenar de manera segura la información en la base de datos
* Disponibilizar APIs

La aplicación consta de varios módulos que son accesibles dependiendo del rol (admin, authorized, user) con el que sea accedida que tenga el usuario.

## Aplicaciones y Versiones Usadas
***
Aplicaciones usadas para el desarrollo del Challenge:
* MySql: Última Version
* Python: Version 3.9
* Docker Desktop

## Instalación
***
Para hacer uso de esta aplicación por favor siga los siguientes pasos: 
```
$ git clone https://example.com
$ cd ../path/to/the/file
$ npm install
$ npm start
```

## Posibles Mejoras
***
1. Bloquear sesión por tiempos de inactividad del usuario.
2. Incluir módulo de creación de usuarios.
3. Cifrar la foto del DNI antes de ser guardada en la base de datos.
4. Incluir mecanismos de autenticación en las API REST.
