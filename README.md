# python-project

Para instalar a versão mais recente do WebDriver podemos instalar o web driver manage.
Para isso instalamos com o comando pip install webdriver-manager
Em seguida utilizamos os comandos:

# Selenium 3

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

