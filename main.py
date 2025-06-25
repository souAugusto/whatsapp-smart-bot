from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json

# Carrega respostas
with open("responses/rules.json", encoding="utf-8") as f:
    rules = json.load(f)

# Inicia navegador
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com')
input("Escaneie o QR Code e pressione Enter...")

def responder_mensagem():
    try:
        mensagens = driver.find_elements(By.CLASS_NAME, "_21Ahp")
        ultima = mensagens[-1].text.lower()
        resposta = rules.get(ultima, "Desculpe, não entendi.")
        campo_msg = driver.find_element(By.XPATH, '//div[@title="Digite uma mensagem"]')
        campo_msg.click()
        campo_msg.send_keys(resposta + Keys.ENTER)
    except Exception as e:
        print("Erro:", e)

while True:
    responder_mensagem()
    time.sleep(5)