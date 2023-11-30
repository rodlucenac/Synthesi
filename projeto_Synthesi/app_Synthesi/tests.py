from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random
import string
import time
import os
import tempfile
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-gpu")
browser = webdriver.Chrome(options=chrome_options)


wait = WebDriverWait(browser, 10)

username = ''.join(random.choices(string.ascii_lowercase, k=8))
password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))

class SalasPageTest(TestCase):
    def test_a_salas(self):
        browser.get("http://127.0.0.1:8000/salas/")
        time.sleep(5)
        from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random
import string
import time
import os
import tempfile
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options)


wait = WebDriverWait(browser, 10)

username = ''.join(random.choices(string.ascii_lowercase, k=8))
password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))

class SalasPageTest(TestCase):
    def test_a_salas(self):
        browser.get("http://127.0.0.1:8000/salas/")
        time.sleep(5)

    
    
    

        
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random
import string
import time
import os
import tempfile
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from django import forms 

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-gpu")
browser = webdriver.Chrome(options=chrome_options)


wait = WebDriverWait(browser, 10)

username = ''.join(random.choices(string.ascii_lowercase, k=8))
password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
my_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

class MyForm(forms.Form):
    my_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))


class SalasPageTest(TestCase):
    def test_a_salas(self):
        browser.get("http://127.0.0.1:8000/salas/")
        time.sleep(2)
        browser.find_element(By.ID, "icn1").click()
        time.sleep(2)
        assert browser.current_url == "http://127.0.0.1:8000/eu_eo_mundo/"
    
    
    def test_b_atividades(self):
        browser.get("http://127.0.0.1:8000/monitoramento/messi/manha/8/")
        time.sleep(3)
        browser.find_element(By.ID, "autoavaliacao").click()
        time.sleep(3)
        browser.find_element(By.ID, "enviar").click()
        time.sleep(2)
        assert browser.current_url == ("http://127.0.0.1:8000/monitoramento/messi/manha/8/")
    
    
    def test_c_autoavaliacao(self):
        browser.get("http://127.0.0.1:8000/monitoramento/messi/manha/8/")
        time.sleep(3)
        browser.find_element(By.ID, "reunioes").click()
        time.sleep(3)
        browser.find_element(By.ID, "solicitar").click()
        time.sleep(2)
        browser.find_element(By.ID, "mensagem_solicitacao").send_keys(password)
        time.sleep(2)
        browser.find_element(By.ID, "enviar").click()
        time.sleep(2)
    
        assert browser.current_url == "http://127.0.0.1:8000/solicitar/messi/manha/8/"

    
    



    




        

    
    
    

        
