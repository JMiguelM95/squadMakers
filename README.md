# SquadMakers

_El proyecto se basa en la automatización del sitio https://www.saucedemo.com/._

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos personales._

### Documentacion del Proyecto 📋

```
Ingresar a la ruta /YOUR-REPOSITORY/resources/docs/
```

### Pre-requisitos 📋

_Que cosas necesitas para instalar el software y como instalarlas_

```
Java 8+
IDE [PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows) o el de tu preferencia.
Instalar [Python](https://www.python.org/)
Instalar [Git](https://git-scm.com/)
Descargar [Chrome Driver](https://chromedriver.chromium.org/) respectivo a su version de Chrome, e instalar en la ruta del proyecto clonado -> drivers
*Recordar de agregar las variables de entorno si es necesario

```

### Instalación 🔧

_Para este caso solo se necesitara hacer los pasos comunes de clonacion de proyecto con Git_

_1. Abrir el IDE e irnos a la opcion de VSC que se encuentra en la parte superior o si es tu primera vez en PyCharm, seleccionaremos la opcion Get from VCS_

_2. Pegaremos la url del [repositorio](https://github.com/JMiguelM95/squadMakers.git) y seleccionaremos la opcion clonar._

_3. Seleccionaremos la opcion de confiar en el proyecto._

_4. Luego iremos a la opcion de File -> Settings for New Projects._

_5. Iremos a la opcion de Python Interpreter y en la lista si no nos muestra ningun interprete, seleccionaremos Add interpreter -> Add Local Interpreter._

_6. En Location, buscaremos la ruta de la carpeta de Python310 (en mi caso, que se encontraba en el disco local C) si no, crearemos una carpeta llamada env dentro de Users->Usuario._

_7. Luego siempre en Python Interpreter, seleccionaremos la opcion de Install +, e instalaremos selenium, behave, gherkin-oficial._

_8. Ya estaremos listos para ejecutar el proyecto._


## Ejecutando las pruebas ⚙️

_Para ejecutar los casos automatizados, simplemente abriremos una terminal dentro de PyCharm y ejecutaremos el siguiente comando_

```
behave ./features
```

### Analice los resultados 🔩

_Estas pruebas automatizadas validan que el flujo de compras, modificacion de carrito y log out, funcionen correctamente_

## Autores ✒️

* **Miguel Miranda** - *QA Automator* - [Miguel Miranda](https://www.linkedin.com/in/miguel-miranda-98a157161/)
