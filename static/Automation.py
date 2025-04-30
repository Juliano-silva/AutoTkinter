# Capturar um Texto
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()



def Buscar_Conteudo(url,tag,quantidade):
    driver.get(url)
    linhas = 0

    try:
        elementos = driver.find_elements(By.TAG_NAME, tag)  
        for i in elementos:
            linhas += 1;
            # Pegar o Conteudo de uma Tag
            # print(f"[{linhas}] {str(i.text).encode('utf-8').decode('utf-8')}")

            #Pegar o conteudo de uma Imagem
            # img_url = i.get_attribute("src")
            # print(img_url)
            if(linhas == quantidade):
                return;
    except NoSuchElementException:
        print("O elemento não Existe")

    driver.quit()


Buscar_Conteudo("https://digitalmonster.fandom.com/pt/wiki/Categoria:Digimon","img",155)