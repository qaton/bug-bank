# Hackaton QA TripleTen Nov 2023

## Equipo: QACTION

## Integrantes

* Susana Villegas
* Ada Obregón
* Jorge Sifuentes
* Omar Centeno

## Aplicaciones probadas

* [Platzi Fake Store API](https://fakeapi.platzi.com/)
* [BugBank de Jhonatas Matos](https://github.com/jhonatasmatos/bugbank-ui)
* [Restful-Booker de Mark Winteringham](https://restful-booker.herokuapp.com/)



## BugBank

Proyecto de automatización de pruebas para la aplicación de Bug Bank, utilizando Python, Selenium y Pytest

### Funcionalidades principales de la aplicación

* Registro de un nuevo usuario
* Login a la aplicación
* Realizar una transferencia bancaria
* Retiro de fondos

### Enfoque de las pruebas

Esta suite de pruebas busca verificar la funcionalidad de la aplicación BugBank,  utilizando el marco de trabajo de Page Object Model.

Las herramientas para realizar el proyecto son Selenium y Pytest para realizar la automatización del navegador y pruebas respectivamente. El lenguaje de programación seleccionado fue Python.

<!-- Se crearon dos clases para separar la lógica de las pruebas. **_UrbanRoutesPage_** es la clase que guarda los selectores y acciones a realizar en la página. _**TestUrbanRoutes**_ es la clase donde se desarrollarán las pruebas y la verificación de la información. -->

### Evaluación de las pruebas
* Se cubre el escenario del usuario o usuaria de pedir el taxi.
* Utiliza al menos 4 tipos distintos de localizadores.
* Las pruebas interactúan con las entradas.
* Las pruebas interactúan con los botones.
* Las funciones de espera se utilizan correctamente.

## Pautas para el estilo del código

* Los nombres de las variables describen claramente lo que se almacena en ellas.
* Si el proyecto tiene varias variables con datos similares, esas variables tienen nombres únicos, pero descriptivos.
* Se utilizan nombres descriptivos para funciones que reflejan lo que hacen.
* Los nombres de funciones comienzan con un verbo.
* Los nombres no deben incluir abreviaturas inapropiadas o poco claras.

## Instalar y correr las pruebas
<!-- 1. Clonar este proyecto: `git clone git@github.com:` -->
2. Entrar a la carpeta del proyecto: `cd bug-bank`
3. Activar entorno virtual `source venv/bin/activate`
4. Instalar dependencias: `pip3 install requirements`. También se puede instalar de forma manual: `pip3 install selenium pytest`
5. Realizar la configuración de Chrome webdriver (ver más adelante)
6. Definir la URL del servidor en el archivo `fixtures/secrets.py` variable: `BASE_URL`
7. Correr pruebas: `python3 main.py --browser chrome`

<!-- ### Configuración de Chrome webdriver

Durante las pruebas se debe de agregar algunas características extras al driver. El código base de este proyecto incluía
la siguiente configuración para obtener el código del teléfono:
```py
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
chrome_options.add_experimental_option("perfLoggingPrefs", {'enableNetwork': True, 'enablePage': True})
capabilities = DesiredCapabilities.CHROME
capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
```
Sin embargo, al momento de incluirlo en la instancia del driver, generó un error. Debido a esto, se tiene que realizar la configuración de las `DesiredCapabilities` directamente en el código, agregando esta configuración en la clase `DesiredCapabilities` que se encuentra en el archivo desired_capabilities.py.

La ruta completa para acceder al archivo es: selenium > webdriver > common > desired_capabilities.py.

Dentro de la clase DesiredCapabilities, agregar la siguiente configuración para la constante CHROME:
```py
    CHROME = {
        "browserName": "chrome",
        "goog:loggingPrefs": {'performance': 'ALL'}
    }
``` -->

## Estructura del proyecto
Dada la complejidad del proyecto y los diferentes elementos que se necesitan para llevar a cabo las pruebas, organicé el proyecto en las siguientes carpetas:
* **Fixtures**: contiene las variables de entorno en `secrets.py` y los datos de prueba.
* **Tests**: carpeta para contener los archivos con las diferentes pruebas que pueda contener el proyecto.
* **Pages**: carpeta para organizar las diferentes páginas que necesite el proyecto.
<!-- * **Utils**: contiene diferentes archivos utilizados para interceptar las respuestas en la red, hechas a la API de la aplicación que gestiona los viajes. -->

## Futuras tareas

<!-- * Realizar la configuración para gestionar la configuración de Firefox y Safari, permitiendo la intercepción de las peticiones, y obteniendo el código telefónico.
Las pruebas pueden correr en tres navegadores diferentes en caso de ser necesario: Chrome, Firefox y Safari.
La implementación de las pruebas en Firefox y Safari no está terminada, por lo que es una tarea a completar para futuros sprints. Sin embargo, es una funcionalidad interesante para pruebas que quise incluir. -->
Para correr las pruebas desde la terminal se pueden utilizar los siguientes comandos:
```sh
python3 main.py --browser chrome # default
python3 main.py --browser firefox
python3 main.py --browser safari
```
