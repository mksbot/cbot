from pprint import pprint
import telebot
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import time

from arquivos_texto import registro, abrir_reg

API_TOKEN = '6159093978:AAEyVQZYRBA2YYkX6GNwl9ypGBWHYGUwNz4'

bot = telebot.TeleBot(API_TOKEN)
page = ('https://www.crunchyroll.com/pt-br/simulcastcalendar?filter=premium&date=2023-12-11')
service = Service()
optiones = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=optiones)
while True:
    time.sleep(500)
    driver.get(page)
    final = None
    titulo2 = []
    titulo = driver.find_elements(By.TAG_NAME,'article')

    imagen = driver.find_elements(By.TAG_NAME,'a')
    for nu, it in enumerate(imagen):
        if 'JUJUTSU KAISEN SEASON 2'.lower().replace(' ', '-') in str(it.get_attribute('href')):
            print(it.get_attribute('href'))
    for nu, it in enumerate(titulo[-10:]):
        texto = f'{it.text}'
        try:
            reg = abrir_reg('animes')
        except:
            registro('', 'animes', 'nao')
            reg = abrir_reg('animes')
        if texto not in reg:
            if 'pm' in it.text or 'am' in it.text:
                registro(texto, 'animes', 'nao')
                time.sleep(6)
                bot.send_message(6512880606, f'🧿 {texto}')

    #

# for nu , it in enumerate(titulo2[-5:]):
#     if not len(it.text) <= 4:
#         print(it.text)

# bot.infinity_polling()