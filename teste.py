import requests
from bs4 import BeautifulSoup

from arquivos_texto import abrir_reg, registro

page = 'https://animefire.plus/home/2'
print(page)
hesders = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, como Gecko) '
                      'Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51'}
site = requests.get(page, headers=hesders)
soup = BeautifulSoup(site.content, 'html.parser')
magnet2 = soup.find_all('div', class_='row ml-1 mr-1 mr-md-2')
i = 1
lista = []
for v in magnet2[0]:
    lista2 = []
    informaçoes = str(v.text).replace('     ', '>')
    num = informaçoes.find('- E')
    episodio = informaçoes[num+1:informaçoes.find('>', num)]
    nome = informaçoes[:num].upper()
    if 'Dub' in nome or 'DUB' in nome or 'dub' in nome:
        mau_elementos = (
            "a,b,c,ç,Ç,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,"
            "Y,Z,À,Á,Â,Ä,Å,Ã,Æ,Ç,É,È,Ê,Ë,Í,Ì,Î,Ï,Ñ,Ó,Ò,Ô,Ö,Ø,Õ,O,E,Ú,Ù,Û,Ü,Ý,Y à,á,â,ä,å,ã,æ,ç,é,è,ê,ë,í,ì,î,ï,ñ,ó,ò,"
            "ô,ö,ø,õ,o,e,ú,ù,û,ü,ý,y".replace(',', ' ').split())
        tag = ''
        for c in nome:
            if c not in mau_elementos:
                if tag == '':
                    tag = nome.replace(str(c), '_')
                else:
                    tag = tag.replace(str(c), '_')
        idioma = ' #DUB'
        descriçao = (f'{"_" * (len(nome) + 10)}\n\n'
                     f'     ✅{nome}\n'
                     f'{"_" * (len(nome) + 10)}\n\n'
                     f'#{tag[:24].replace("__", "_")}..\n'
                     f'🎞{episodio}   |   '
                     f'🇧🇷{idioma}'
                     )
        print(descriçao)
        try:
            reg = abrir_reg('animes_dub')
        except:
            registro(f'{nome}{episodio}', 'animes_dub', 'nao')
            reg = abrir_reg('animes_dub')

        if str(nome + episodio) not in reg:
            lista2.append(descriçao)
            print(v)

            try:
                link = v.a['href']
                site = requests.get(link, headers=hesders)
                soup = BeautifulSoup(site.content, 'html.parser')
                magnet2 = soup.find_all('div', id='div_video',)
                for j in magnet2[0]:
                    try:
                        link2 = j.video['data-video-src']
                    except:
                        pass

                tratar_link = requests.get(link2)
                links = str(tratar_link.text)
                inicio = links.find('http', 150)
                fim = links.find('label', inicio)

                link3 = links[inicio:fim - 3].replace('\/', '/')
                print(link3)

                imagem = v.img['data-src']
                print(imagem)
                botao = quick_markup({

                    'ASSISTIR | BAIXAR': {'url': link3},

                }, row_width=2)
                lista2.append(botao)
                lista2.append(imagem)
                lista2.append(f'{nome + episodio}')
                lista.append(lista2)
                print(nome)
            except:
                    pass
        else:

            print('>> JA FOI ENVIADO !!')