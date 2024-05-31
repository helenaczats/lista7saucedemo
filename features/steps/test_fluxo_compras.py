# 1 - Bibliotecas / Imports
import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'que acesso o site Sauce Demo')
def step_impl(context):
    # Setup / Inicializacão
    context.driver = webdriver.Chrome()   #instanciar o objeto do Selenium WebDriver especializado para o Chrome
    context.driver.maximize_window()      #maximizar a janela do navegador
    context.driver.implicitly_wait(10)    #esperar até 10 seg por qualquer elemento
    # Passo em si
    context.driver.get("https://www.saucedemo.com") #abrir o navegador no endereço do site alvo
    

# Preenche com usuario e senha
@when(u'preencho os campos de login com usuario {usuario} e senha {senha}')
def step_impl(context, usuario, senha):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario) #preencher usuário
    context.driver.find_element(By.ID, "password").send_keys(senha)    #preencher a senha
    context.driver.find_element(By.ID, "login-button").click() 
    
@then(u'sou direcionado para pagina Home')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"
    time.sleep(2) # espera por 2 segundos - remover depois(alfinete)
    
#Incluir produto no carrinho de compras   
@when(u'incluo o produto Sauce Labs Backpack no carrinho')
def step_impl(context):
    context.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click() 

#Validar os campos do produto   
@then(u'valido os campos titulo, quantidade e preco do produto Sauce Labs Backpack')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click() #entra no carrinho de compras
    assert context.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").text == "1" #valida quantidade
    assert context.driver.find_element(By.CSS_SELECTOR, ".inventory_item_name").text == "Sauce Labs Backpack" #valida titulo mochila
    assert context.driver.find_element(By.CSS_SELECTOR, ".inventory_item_price").text == "$29.99" #valida preço mochila
   
#Remover o produto do carrinho 
@when(u'removo o produto')
def step_impl(context):
    context.driver.find_element(By.ID, "remove-sauce-labs-backpack").click() #remove mochila  
      
#Valido carrinho vazio    
@then(u'verifico que o carrinho esta vazio')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click() #entra no carrinho de compras
    numero_carrinho = context.driver.find_elements(By.CSS_SELECTOR, ".shopping_cart_linkspan")
    assert len(numero_carrinho) == 0 #valida quantidade    

#Logout
@then(u'realizo logout')
def step_impl(context):
    context.driver.find_element(By.ID, "react-burger-menu-btn").click() #entra no menu
    context.driver.find_element(By.ID, "logout_sidebar_link").click() #faz log out no site@when(u'incluo o produto "Sauce Labs Backpack" no carrinho')


#teardown / encerramento

    context.driver.quit()  