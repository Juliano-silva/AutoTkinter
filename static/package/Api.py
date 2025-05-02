import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from database import DataBS

lista_api = []
lista_search_url = []

def searchAPI(Buscar,quantidade):
    url = f"https://www.google.com/search?q={Buscar}"
    options = webdriver.ChromeOptions()
    options.add_argument(r"user-data-dir=C:\Users\ronal\AppData\Local\Google\Chrome\User Data") 
    driver = webdriver.Chrome(options=options)

    driver.get(url)

    Achar = driver.find_elements(By.TAG_NAME,'cite')

    for cite in Achar:
        Conteudo = str(cite.text).split()
        if (len(Conteudo) > 0 and str(Conteudo[0])[0:5] == "https" and quantidade > 0):
            lista_search_url.append(Conteudo[0])
            quantidade-=1
        

    driver.quit()

    return lista_search_url


def locateAPI(url,quantidade):
    response = requests.get(url)


    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        texto = soup.get_text()

        for i in texto.split():
            if (str(i).find("/api/") != -1 and quantidade > 0):
                lista_api.append(i)
                quantidade-=1
    else:
        print(f'Erro ao acessar a página: {response.status_code}')

    return lista_api



searchAPI("Pokemon API",11)


for i in lista_search_url:
    DataBS("insert",f"{i}",f"{locateAPI(str(i),5)}") 