from behave import *
import comprarProductosteps


@given('El usuario ingresa el navegador')
def launchbrowser(context):
    comprarProductosteps.launchbrowser(context)


@when('El usuario ingresa el sitio {site}')
def opensaucedemo(context, site):
    comprarProductosteps.opensaucedemo(context, site)


@then('El usuario se ingresa sesion con las credenciales usuario {user} y contraseña {password}')
def login(context, user, password):
    comprarProductosteps.login(context, user, password)


@then('El usuario a finalizado la compra de un producto')
def preparecasepurchase(context):
    comprarProductosteps.addproduct(context)
    comprarProductosteps.gotocart(context)
    comprarProductosteps.gotocheckout(context)
    comprarProductosteps.filluserinformation(context, "Miguel", "Miranda", "0000")
    comprarProductosteps.finishthepurchase(context)


@then('El usuario selecciona el menu de opciones')
def sidebaroption(context):
    context.driver.find_element("id", "react-burger-menu-btn").click()


@then('El usuario selecciona la opcion de LogOut')
def logoutoption(context):
    context.driver.implicitly_wait(15)
    context.driver.find_element("id", "logout_sidebar_link").click()


@then('El usuario verifica que se ha deslogueado')
def verifylogout(context):
    status = context.driver.find_element("id", "user-name").is_displayed()
    assert status is True
    context.driver.close()
