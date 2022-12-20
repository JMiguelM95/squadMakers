Feature: Comprar Productos en https://www.saucedemo.com/

  Background: Ingresando al sitio
    Given El usuario inicia el navegador
    When El usuario abre el sitio https://www.saucedemo.com/
    Then El usuario se inicia sesion con las credenciales usuario standard_user y contraseña secret_sauce

  Scenario: Comprar un producto
    Given El usuario agrega el primer producto al carrito
    When El usuario ingresa al carrito
    And El usuario ingresa a la opcion de checkout
    And El usuario llena todos sus datos con nombre Miguel, apellido Miranda, codigo postal 0000
    And El usuario finaliza la compra
    Then El usuario verifica que la compra ha sido completada con exito

  Scenario:  Eliminar producto de un carrito
    Given El usuario agrega el primer producto al carrito
    When El usuario ingresa al carrito
    And El usuario verifica que exista la QTY de un producto
    Then El usuario selecciona la opcion de Remove
    And El usuario verifica que ya no exista la QTY de un producto

  Scenario: Agregar 2 productos diferentes al carrito
    Given El usuario agrega el primer producto al carrito
    When El usuario ingresa al carrito
    And El usuario selecciona la opcion de Continue Shopping
    And El usuario agrega el segundo producto al carrito
    And El usuario ingresa al carrito
    And El usuario ingresa a la opcion de checkout
    And El usuario llena todos sus datos con nombre Miguel, apellido Miranda, codigo postal 0000
    And El usuario finaliza la compra
    Then El usuario verifica que la compra ha sido completada con exito







