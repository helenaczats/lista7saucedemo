Feature: Fluxo de Compras

Scenario: Fluxo de compras produto "Sauce Labs Backpack"
        Given que acesso o site Sauce Demo
        When preencho os campos de login com usuario standard_user e senha secret_sauce 
        Then sou direcionado para pagina Home
        When incluo o produto Sauce Labs Backpack no carrinho
        Then valido os campos titulo, quantidade e preco do produto Sauce Labs Backpack
        When removo o produto 
        Then verifico que o carrinho esta vazio 
        Then realizo logout