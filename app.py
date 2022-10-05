from http.server import executable
from IPython.display import display
import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib

# contatos_df = pd.read_excel("test.xlsx")
contatos_df = pd.read_excel("Lista_de_Empreendedores.xlsx")


display(contatos_df)
o = webdriver.ChromeOptions()
o.add_argument(
    'user-data-dir=/Users/lucascardoso/Library/Application Support/Google/Chrome')

# navegador = selenium.webdriver.Chrome(
#     executable_path="./chromedriver", chrome_options=o)
navegador = selenium.webdriver.Chrome(
    executable_path="./chromedriver")
navegador.get("https://web.whatsapp.com/")

while len(navegador.find_elements_by_id("side")) < 1:
    time.sleep(1)

texto_postagem = f"O dia dos namorados está chegando! E com ele nossos clientes vão estar a procura de presentes para seus amados e amadas, e com isso trazendo mais vendas para os empreendedores! \n\nPor isso, estamos procurando estabelecimentos que irão fazer *PROMOÇÕES ou tem PRODUTOS PARA ESSA DATA* queremos fazer um post em nosso instagram (@aua.conecta) para ajuda-los a alavancar suas vendas! \n\nCaso seu negócio vá fazer algo do tipo, por favor me diga para que nos possamos *incluir seu estabelecimento em nossa postagem!*"
link_postagem = "https://forms.gle/fYCJRgakFbUvRzXj9"
chamada = "[DIA DOS NAMORADOS NO AUA]"
numero_nao_encontrado = []

# i é o indice na planilha
for i, contato in enumerate(contatos_df['Contato']):
    try:
        pessoa = contatos_df.loc[i, "Nome do Empreendedor"].split()[0]
        numero_contato = contatos_df.loc[i, "Contato"]

        texto = urllib.parse.quote(
            f"*{chamada}* \n\nBomm diaa {pessoa}!\n{texto_postagem}\n\nQualquer dúvida, fique a vontade para perguntar ;)")

        link_mensagem = f"https://web.whatsapp.com/send?phone=55{numero_contato}&text={texto}"

        navegador.get(link_mensagem)
        while len(navegador.find_elements_by_id("side")) < 1:
            time.sleep(10)
        text_input_element = navegador.find_element_by_xpath(
            '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
        print(text_input_element)
        text_input_element.send_keys(Keys.ENTER)
        time.sleep(10)
    except:
        numero_nao_encontrado.append(pessoa)
        continue
print(f"PROBLEMAS NO CONTATO: {numero_nao_encontrado}")
