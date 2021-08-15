# FreddyGram

FreddyGram es el proyecto llevado a cabo en el curso de **Django** en **platzi**, el mismo trata de un clon de la red social **Instagram**.

## Documentación

### Django

Nace en 2003, con la necesidad de hacer web's con la filosofía de hacer las cosas de manera agíl.

- Poder hacer sitios escalables.
- URLs bien diseñadas.
- HTTP request y responses.
- -ORM, que es conectar a na DB a traves de una interfaz python.

#### Características.

- Rápido desarrollo.
- Listo para todo.
- Seguro contra ataques.
- Versátil.

#### Ventajas

- Es desarrollado en Python.
- -DRY(Don’t repeat yourself).
- Comunidad Open Source.

#### App

Una **app** dentro de **Django** es un modulo de **python** que provee un conjunto de funcionalidades relacionadas entre sí.
Las **apps** son una combinación de models, vistas, urls, archivos estaticos.

Muchas **apps** en django estan hechas para ser reutilizadas.

#### Patrones de Diseño

Un **patrón de diseño**, en términos generales, es una solución reutilizable a un problema común.
El patrón más común para el desarrollo web es **MVC (Model, View, Controller)**. **Django** implementa un patrón similar llamado** MTV (Model, Template, View)**.

##### M en MTV

El Modelo en **Django** usa diferentes opciones para conectarse a múltiples bases de datos relacionales, entre las que se encuentran: **SQLite, PostgreSQL, Oracle y MySQL.**
Para la creación de tablas, **Django** usa la técnica del **ORM (Object Relational Mapper)**, una abstracción del manejo de datos usando OOP.

##### T en MTV

**Template system de Django** es una manera de presentar los datos usando HTML, está inspirado en **Jinja2** y su sintaxis, por lo cual comparte muchas similitudes. Permite incluir alguna lógica de programación.

##### V en MTV

**Vista**: Parte de un proyecto de Django que se encarga de la
lógica de negocio y es la conexión entre el template y el modelo.

### ORM

**ORM: Object-relational mapping**. Es el encargado de permitir
el acceso y control de una base de datos relacional a través de
una abstracción a clases y objetos.

#### Modelo de usuarios

Las opciones que **Django** propone para implementar **Usuarios** personalizados son:

- Usando el Modelo proxy
- Extendiendo la clase abstracta de Usuario existente
- La opción OneToOneField restringe la posibilidad de tener perfiles duplicados.
  Django no guarda archivos de imagen en la base de datos sino la referencia de su ubicación.

#### Cambios en base de datos

Para reflejar los cambios en la base de datos, siempre que se crea o se edita un **modelo** debemos cancelar el server, ejecutar **makemigrations**, **migrate** y luego de nuevo volver a correr el servidor con runserver.

Con respecto a las imágenes, **Django** por defecto no está hecho para servir la media, pero editando las urls logramos que se puedan mostrar. Para servir archivos de media, usamos **MEDIA_ROOT** y **MEDIA_URLS**.

#### Templates y archivos estáticos

Los **templates** quedarán definidos en un nuevo folder que llamaremos /templates/.

El concepto de **archivos estáticos** en **Django**, son archivos que se usan a través de la aplicación para pintar los datos. Pueden ser archivos de imagen, audio y video, o archivos css y scripts js.

Para servir archivos estáticos, nos apoyamos en **STATIC_ROOT** y **STATIC_URLS**.

#### Middleware

Un **middleware** en **Django** es una serie de hooks y una **API** de bajo nivel que nos permiten modificar el objeto request antes de que llegue a la vista y response antes de que salga de la vista.

**Django** dispone de los siguientes **middlewares** por defecto:

- SecurityMiddleware
- SessionMiddleware
- CommonMiddleware
- CsrfViewMiddleware
- AuthenticationMiddleware
- MessageMiddleware
- XFrameOptionsMiddleware

![Middleware django](https://cdn-images-1.medium.com/max/800/1*t9TAX89Y3rZUXth2Le07Xg.png "Middleware django")

#### Formularios en Django

La clase utilitaria para **formularios** de **Django** nos ayuda a resolver mucho del trabajo que se realiza de forma repetitiva. La forma de implementarla es muy similar a la implementación de la clase models.model.

Algunas de las clases disponibles en **Django** al implementar form, son:

- BooleanField
- CharField
- ChoiceField
- TypedChoiceField
- DateField
- DateTimeField
- DecimalField
- EmailField
- FileField
- ImageField"

#### Generic auth views

**Django** cuenta con varias **vistas genéricas** basadas en clases para resolver muchas de las funcionalidades relacionadas con la autenticación, como es el caso de:

- login
- logout
- password_change
- password_change_done
- password_reset
- password_reset_done
- password_reset_confirm
- password_reset_complete

Estas **vistas genéricas** nos permiten ahorrarnos varias líneas de código, además de que incluyen características adicionales de mucha utilidad.

### Deployment

Liberar un proyecto de **Django** a producción es una tarea bastante sencilla pero que puede confundir a muchos la primera vez que se intente. El objetivo de esta lectura es tener una breve a introducción a la arquitectura de un proyecto de **Django** corriendo en un servidor de producción (un servidor de verdad) y que consecuentemente los siguientes tutoriales de configuración tengan más sentido al momento de que los leas.

**WSGI** significa** Web Server Gateway Interface** y es un protocolo sencillo de llamadas para que un web server (como NGINX o Apache) se comuniquen con una aplicación web o framework escritos en **Python**.

**WSGI** nos permite delegar el trabajo de aplicar reglas complejas de enrutamiento a un web server como NGINX y al mismo tiempo lograr que exista una comunicación del usuario final de nuestro proyecto de **Python**. Dicho esto, esta sería la ilustración de un servidor que expone múltiples servicios como e-mail a través de pop3, un app server usando **SSL**, otro app server redirigiendo las peticiones HTTP a HTTPS y una base de datos de PostgreSQL:

![](https://static.platzi.com/media/user_upload/Captura%20de%20pantalla%202018-07-31%20a%20la%28s%29%2019.16.03-8b5449d4-edce-4602-ace8-7d2a23429127.jpg)

#### Conexión a base de datos

**Django** obtiene la estructura, acceso y control de los datos de una aplicación a través de su **ORM (Object Relational Mapper)**, esto significa que no importa qué motor de base de datos esté usando, el mismo código seguirá funcionando, configurar esto en un proyecto de **Django** es cuestión de segundos.

Todo se define dentro del archivo **settings.py** de nuestro proyecto dentro de la variable **DATABASES**:

##### DATABASES

Será el nodo padre que nos servirá para indicar que definiremos una base de datos.
Dentro, tendremos el nodo default este tendrá toda la configuración clave de la base de datos.

![](https://static.platzi.com/media/user_upload/datos%20para%20conexio%CC%81n%20de%20base%20de%20datos%20django-8292986f-e2fd-4f06-842e-d819f9396c48.jpg)

Además, **Django** puede trabajar con múltiples bases de datos usando una estrategia llamada **routers** por lo que el diccionario **DATABASES** puede contener múltiples llaves con diferentes bases de datos. Pero eso sí, necesita siempre existir una llave “default”.

Es un diccionario de **python** el cual requiere definir una base de datos por default, más de eso al final, usando la llave default que a su vez será otro diccionario con los datos de configuración:

La configuración recibirá el engine el cual puede ser:

- PostgreSQL: 'django.db.backends.postgresql’
- MySQL: 'django.db.backends.mysql’
- SQLite: 'django.db.backends.sqlite3’
- Oracle: 'Django.db.backends.oracle’

  El nombre de la base de datos “NAME”.
  El usuario “USER”.
  La contraseña “PASSWORD”.
  La ubicación o host del servidor de la base de datos “HOST”.
  Y el puerto de conexión “PORT”.

Adicionalmente, se pueden configurar más detalles por base de datos, por ejemplo, configurar que todos los queries de una vista sean empaquetados en una sola transacción a la base de datos usando **ATOMIC_REQUESTS=True**

![ORM DJANGO](https://static.platzi.com/media/user_upload/Django-database-3e08c778-1e3d-445a-a2de-5ac070f53e56.jpg "ORM DJANGO")
