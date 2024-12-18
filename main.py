from selenium import webdriver
import time

# abriria o navegador
navegador = webdriver.Chrome()

# iria para a página do google flights
link = "https://www.google.com/travel/flights/search?tfs=CBwQAhooEgoyMDI1LTAyLTEwagwIAhIIL20vMDZnbXJyDAgDEggvbS8wNXF0ahooEgoyMDI1LTAyLTE3agwIAxIIL20vMDVxdGpyDAgCEggvbS8wNmdtckABSAFwAYIBCwj___________8BmAEB&hl=pt-BR&gl=BR"
navegador.get(link)

time.sleep(5)

# pegar o preço da passagem aérea mais barata
preco = navegador.find_element("class name", "jLMuyc").text


# preco.txt
with open("preco.txt", "w") as arquivo:
    arquivo.write(preco)