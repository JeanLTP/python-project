# python-project

Esse projeto foi desenvolvido com base no curso Automação de Testes Web com Selenium Webdriver e Python na plataforma Udemy


# WebDriver
Para instalar a versão mais recente do WebDriver podemos instalar o web driver manage.
Para isso instalamos com o comando pip install webdriver-manager
Em seguida utilizamos os comandos:

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

