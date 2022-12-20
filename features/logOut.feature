Feature: Desloguearse de https://www.saucedemo.com/

  Background: Ingresando al sitio
    Given El usuario ingresa el navegador
    When El usuario ingresa el sitio https://www.saucedemo.com/
    Then El usuario se ingresa sesion con las credenciales usuario standard_user y contraseña secret_sauce

  Scenario: Usuario sin compra finalizada se desloguea
    And El usuario selecciona el menu de opciones
    And El usuario selecciona la opcion de LogOut
    And El usuario verifica que se ha deslogueado

  Scenario: Usuario con compra finalizada se desloguea
    And El usuario a finalizado la compra de un producto
    And El usuario selecciona el menu de opciones
    And El usuario selecciona la opcion de LogOut
    And El usuario verifica que se ha deslogueado

