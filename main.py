import random
from pprint import pprint
import telebot
from selenium import webdriver

from selenium.webdriver.common.by import By

import time

from telebot.util import quick_markup

from arquivos_texto import registro, abrir_reg

API_TOKEN = ['6812826133:AAHTh_ZzbOSXeKjAedxwpPKJMeuMt6AT-o8',
             '6859056897:AAFAhdg80DyiYjBX3lIKBzZ-xWaRqDDQGQ8']

bot = telebot.TeleBot(API_TOKEN[0])
bot2 = telebot.TeleBot(API_TOKEN[1])
import requests
from bs4 import BeautifulSoup

while True:
    try:
        contador = int(abrir_reg('cont'))
    except:
        registro(10, 'cont', 'nao')
        contador = int(abrir_reg('cont'))
    page = f'https://animesonlinecc.to/episodio/page/{str(contador)}/'
    print(page)
    hesders = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, como Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51'}

    site = requests.get(page, headers=hesders)
    soup = BeautifulSoup(site.content, 'html.parser')
    magnet2 = soup.find_all('div', class_='animation-2 items')
    i = 1
    lista = []
    for v in magnet2[0]:

        lista2 = []
        informaçoes = str(v.text).replace('do ', 'do >')
        num = informaçoes.find('>')
        nome = informaçoes[num + 1:]
        num = nome.find('Episodio')
        episodio = nome[num:]
        nome = nome[:num].upper()
        mau_elementos = (
            "a,b,c,ç,Ç,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,"
            "Y,Z,À,Á,Â,Ä,Å,Ã,Æ,Ç,É,È,Ê,Ë,Í,Ì,Î,Ï,Ñ,Ó,Ò,Ô,Ö,Ø,Õ,O,E,Ú,Ù,Û,Ü,Ý,Y à,á,â,ä,å,ã,æ,ç,é,è,ê,ë,í,ì,î,ï,ñ,ó,ò,"
            "ô,ö,ø,õ,o,e,ú,ù,û,ü,ý,y")

        for c in nome:
            if c not in lista or c == ' ':
                tag = nome.replace(c, '_')
        idioma = informaçoes[1:5].upper()
        descriçao = (f'{"_" * (len(nome) + 10)}\n\n'
                     f'     ✅{nome}\n'
                     f'{"_" * (len(nome) + 10)}\n\n'
                     f'#{tag}\n'
                     f'🎞{episodio}   |   '
                     f'🇧🇷{idioma}'
                     )
        try:
            reg = abrir_reg('animes')
        except:
            registro(f'{nome}{episodio}', 'animes', 'nao')
            reg = abrir_reg('animes')
        if str(nome + episodio) not in reg:
            lista2.append(descriçao)
            for c in v.div:

                try:
                    link = c['href']
                    site = requests.get(link, headers=hesders)
                    soup = BeautifulSoup(site.content, 'html.parser')
                    magnet2 = soup.find_all('div', class_='play-box-iframe fixidtab')
                    link2 = magnet2[0].iframe['src']

                    imagem = c.img['src']
                    botao = quick_markup({

                        'ASSISTIR | BAIXAR': {'url': link2},

                    }, row_width=2)
                    lista2.append(botao)
                    lista2.append(imagem)
                    lista2.append(f'{nome + episodio}')
                    lista.append(lista2)
                    print(nome)


                except:
                    pass
        else:
            time.sleep(120)
            print('>> JA FOI ENVIADO !!')
    lista.reverse()
    if f'{len(lista)}' not in '0':
        for num, it in enumerate(lista):
            descriçao, botao, imagem, nomer = lista[num]
            print('>> ENVIANDO !!')
            time.sleep(random.randint(0, 150))
            if num % 2 == 0:
                bot2.send_photo(-1002000136655, f'{imagem}', caption=f'{descriçao}', reply_markup=botao)
            else:
                bot.send_photo(-1002000136655, f'{imagem}', caption=f'{descriçao}', reply_markup=botao)
            registro(f'{nomer}', 'animes', 'nao')
    if str(contador) not in '0':
        print(contador)
        contador -= 1
        registro(contador, 'cont')
