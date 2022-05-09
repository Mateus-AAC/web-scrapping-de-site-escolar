import requests
import unidecode as uni
from bs4 import BeautifulSoup

def scrap_email_info(email: str) -> dict:

    email_url = f'https://www.escol.as/{email}'

    page = requests.get(email_url)

    soup = BeautifulSoup(page.content, 'html.parser')
    indicador = soup.select('.mr-6')

    try:
        email_dic = {
            soup.select('h1')[0].text: [soup.select('span > a ')[1].text, soup.select('span')[1].text],
        }

        if (email_dic == {}):

            return

        else :
            email = email_dic

            for chave, valor in email.items():
                dados = f"Nome da Escola = {chave} || Email = {valor[0]} || Estado e Cidade = {valor[1]}"
            
            dadosOut = uni.unidecode(dados)

            with open('escolas.txt', 'a') as arquivo:
                arquivo.write(str(dadosOut) + '\n')
                    
            print(dadosOut)

    except:
        return ' '  

def alterarPagina():
    id = 28911
    for x in range(0, 10):
        cont = id + x
        scrap_email_info(cont)


alterarPagina()

print("Acabou de gerar o arquivo.")