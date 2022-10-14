from http.server import executable
from IPython.display import display
import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib

contatos_df = pd.read_excel("test.xlsx")
# contatos_df = pd.read_excel("Lista_de_Empreendedores.xlsx")


display(contatos_df)
o = webdriver.ChromeOptions()
o.add_argument(
    'user-data-dir=/Users/lucascardoso/Library/Application Support/Google/Chrome')

# navegador = selenium.webdriver.Chrome(
#     executable_path="./chromedriver", chrome_options=o)
navegador = selenium.webdriver.Chrome(
    executable_path="./chromedriver")
navegador.get("https://web.whatsapp.com/")
    

while len(navegador.find_elements(By.ID,"side")) < 1:
    time.sleep(1)

texto_postagem = f"Antes de tudo, quero *AGRADECER* você por permanecer resiliente na dificil tarefa de ter um pequeno negócio em nossa região, você é parte da solução. Também quero agradecer por confiar em nossa equipe para ajudar a mostrar seu negócio e sua HISTÓRIA para mais pessoas através de nosso app, aprendemos muito! E esperamos ter retribuido para você toda nossa gratidão."
link_postagem = "https://pertinhodecasa.com.br"
chamada = "[OBRIGADO E ATÉ BREVE!]"
numero_nao_encontrado = []

# i é o indice na planilha
for i, contato in enumerate(contatos_df['Contato']):
    try:
        pessoa = contatos_df.loc[i, "Nome do Empreendedor"].split()[0]
        numero_contato = contatos_df.loc[i, "Contato"]

        texto = urllib.parse.quote(
            f"*{chamada}* \n\nOlá {pessoa} tudo bem?!\n\n{texto_postagem}\n\nVenho comunicar que o *aplicativo AUA - Compre do Pequeno irá ser desligado em breve*, agora, seremos parte de uma família maior. A *Pertinho de Casa*, essa plataforma exclusiva e GRATUITA para pequenos empreendedores que te convido para fazer parte, o link para conhecer esta aqui embaixo:\n\n {link_postagem} \n\n*MUITO OBRIGADO POR TUDO, E ATÉ UMA PRÓXIMA!*\n\nAtensiosamente,\n*Toda a equipe AUA*")

        link_mensagem = f"https://web.whatsapp.com/send?phone=55{numero_contato}&text={texto}"

        navegador.get(link_mensagem)
        while len(navegador.find_elements(By.ID,"side")) < 1:
            time.sleep(1)
        text_input_element = navegador.find_element(By.XPATH,
            '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
        print(text_input_element)
        text_input_element.send_keys(Keys.ENTER)
        time.sleep(5)
    except:
        numero_nao_encontrado.append(pessoa)
        continue
print(f"PROBLEMAS NO CONTATO: {numero_nao_encontrado}")
