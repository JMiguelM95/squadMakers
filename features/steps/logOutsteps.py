import os

from behave import *
import comprarProductosteps
from dotenv import load_dotenv


@given('El usuario ingresa el navegador')
def launchBrowser(context):
    comprarProductosteps.launchBrowser(context)


@when('El usuario ingresa el sitio {site}')
def openSauceDemo(context, site):
    comprarProductosteps.openSauceDemo(context, site)


@then('El usuario se ingresa sesion con las credenciales usuario {user} y contraseña {password}')
def logIn(context, user, password):
    comprarProductosteps.logIn(context, user, password)


@then('El usuario a finalizado la compra de un producto')
def prepareCasePurchase(context):
    load_dotenv()
    comprarProductosteps.addProduct(context)
    comprarProductosteps.goToCart(context)
    comprarProductosteps.goToCheckout(context)
    comprarProductosteps.fillUserInformation(context, os.getenv('username'), os.getenv('lastName'), os.getenv('postalCode'))
    comprarProductosteps.finishThePurchase(context)


@then('El usuario selecciona el menu de opciones')
def sideBarOption(context):
    context.driver.find_element("id", "react-burger-menu-btn").click()


@then('El usuario selecciona la opcion de LogOut')
def logOutOption(context):
    context.driver.implicitly_wait(15)
    context.driver.find_element("id", "logout_sidebar_link").click()


@then('El usuario verifica que se ha deslogueado')
def verifyLogOut(context):
    status = context.driver.find_element("id", "user-name").is_displayed()
    assert status is True
    context.driver.close()
