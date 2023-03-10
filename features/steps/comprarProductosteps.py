from behave import *
from selenium import webdriver

stat = False


@given('El usuario inicia el navegador')
def launchbrowser(context):
    context.driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
    context.driver.maximize_window()
    # context.driver=webdriver.Chrome()


@when("El usuario abre el sitio {site}")
def opensaucedemo(context, site):
    context.driver.get(site)


@then('El usuario se inicia sesion con las credenciales usuario {user} y contraseña {password}')
def login(context, user, password):
    context.driver.find_element("id", "user-name").click()
    context.driver.find_element("id", "user-name").send_keys(user)
    context.driver.find_element("id", "password").click()
    context.driver.find_element("id", "password").send_keys(password)
    context.driver.find_element("id", "login-button").click()


@given('El usuario agrega el primer producto al carrito')
def addproduct(context):
    context.driver.find_element("id", "add-to-cart-sauce-labs-backpack").click()


@when('El usuario ingresa al carrito')
def gotocart(context):
    context.driver.find_element("xpath", "//div[@id='shopping_cart_container']/a/span").click()


@when('El usuario ingresa a la opcion de checkout')
def gotocheckout(context):
    context.driver.find_element("id", "checkout").click()


@when('El usuario llena todos sus datos con nombre {fistName}, apellido {lastName}, codigo postal {postalCode}')
def filluserinformation(context, fistName, lastName, postalCode):
    context.driver.find_element("id", "first-name").click()
    context.driver.find_element("id", "first-name").send_keys(fistName)
    context.driver.find_element("id", "last-name").click()
    context.driver.find_element("id", "last-name").send_keys(lastName)
    context.driver.find_element("id", "postal-code").click()
    context.driver.find_element("id", "postal-code").send_keys(postalCode)
    context.driver.find_element("id", "continue").click()


@when('El usuario finaliza la compra')
def finishthepurchase(context):
    context.driver.find_element("id", "finish").click()


@then('El usuario verifica que la compra ha sido completada con exito')
def verifysuccesspurchase(context):
    status = context.driver.find_element("xpath", "//div[@id='header_container']/div[2]/span").is_displayed()
    assert status is True
    #context.driver.close()


@when('El usuario verifica que exista la QTY de un producto')
def verifyproductqty(context):
    status = context.driver.find_element("xpath",
                                         "//div[@id='cart_contents_container']/div/div/div[3]/div").is_displayed()
    assert status is True
    stat = False


@then('El usuario selecciona la opcion de Remove')
def removeproduct(context):
    context.driver.find_element("id", "remove-sauce-labs-backpack").click()


@then('El usuario verifica que ya no exista la QTY de un producto')
def verifyproductqtyisnotdisplayed(context):
    assert stat is False


@when('El usuario selecciona la opcion de Continue Shopping')
def continueshopping(context):
    context.driver.find_element("id", "continue-shopping").click()


@when('El usuario agrega el segundo producto al carrito')
def addsecondproduct(context):
    context.driver.find_element("id", "add-to-cart-sauce-labs-bike-light").click()
