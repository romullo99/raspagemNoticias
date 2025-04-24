from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time

CAMINHO_CHROMEDRIVER = "C:\\Users\\Educação\\Pictures\\raspagemNoticias\\driver\\chromedriver.exe"

chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')


service = Service(CAMINHO_CHROMEDRIVER)
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://ge.globo.com/pe/futebol/times/nautico/")
time.sleep(5)

noticias = driver.find_elements(By.CLASS_NAME, "feed-post-body-title")[:10]

conteudo = "📰 Notícias do Náutico:\n\n"

for i, noticia in enumerate(noticias, start=1):
    titulo = noticia.text
    try:
        link = noticia.find_element(By.TAG_NAME, "a").get_attribute("href")
    except NoSuchElementException:
        link = "Link não encontrado"
    
    linha = f"{i}. {titulo}\n   🔗 {link}\n\n"
    print(linha)
    conteudo += linha

with open("noticias_nautico.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(conteudo)

# Fecha o navegador
driver.quit()

print("✅ Arquivo 'noticias_nautico.txt' criado com sucesso!")
