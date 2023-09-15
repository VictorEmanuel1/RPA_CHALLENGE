from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import chromedriver_binary 

dict_xpaths = {
    'botao_download':'/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/a',
    'botao_start': '/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button',
    'botao_nome': '/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/div/div[1]/rpa1-field/div',
    'botao_submit': '/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input'
}

# Função para definir se vai rodar em headless ou não
def get_options():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--headless")
    return chrome_options 

# # Instancia o driver do Chrome
driver = webdriver.Chrome(r"C:\Users\Dinu\Documents\ProBot\chrome.exe")
navegador = driver
navegador.get('https://www.rpachallenge.com/')
navegador.maximize_window()
print('Acessou o site') 


# # # Clica no botão de download
# driver.find_element_by_xpath(dict_xpaths['botao_download']).click()
# print('Clicou no botão de download')

# lendo a planilha
wb = pd.read_excel(r'C:\Users\victor.queiroz\Downloads\challenge.xlsx', sheet_name='Sheet1')
Tabela1 = pd.DataFrame(wb)
processar = len(wb.index)
print('Vou processar essa quantidade de linhas: ' + str(processar))

# Criando as listas
lista_nome = [str(x) for x in Tabela1['First Name']]
lista_sobrenome = [str(x) for x in Tabela1['Last Name ']]
lista_companhia = [str(x) for x in Tabela1['Company Name']]
funcao_empresa = [str(x) for x in Tabela1['Role in Company']]
lista_endereco = [str(x) for x in Tabela1['Address']]
lista_email = [str(x) for x in Tabela1['Email']]
lista_telefone = [str(x) for x in Tabela1['Phone Number']]

# Clica no botão de start
driver.find_element_by_xpath(dict_xpaths['botao_start']).click()
print('Clicou no botão de start')

# Loop para preencher os campos
for x in range(len(lista_companhia)):

    nome = lista_nome[x]
    sobrenome = lista_sobrenome[x]
    companhia = lista_companhia[x]
    funcao = funcao_empresa[x]
    endereco = lista_endereco[x]
    email = lista_email[x]
    telefone = lista_telefone[x]

    for i in range(1,9):

        xpath_geral = f'/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/div/div[{i}]/rpa1-field/div/label'
        xpath_label = f'/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/div/div[{i}]/rpa1-field/div/input'

        try:
            element = driver.find_element(By.XPATH, xpath_geral)
            label = driver.find_element(By.XPATH, xpath_label)
            print('Procurando o campo: ' + str(i))
            element.click()
            print('Clicou no campo: ' + str(i))

            texto = element.text
            print('Texto do campo: ' + texto)

            if texto == 'First Name':
                print('Fiz o primeiro nome')
                driver.find_element(By.XPATH, xpath_label).send_keys(nome)
                continue

            elif texto == 'Last Name':
                print('Fiz o sobrenome')
                driver.find_element(By.XPATH, xpath_label).send_keys(sobrenome)
                continue

            elif texto == 'Company Name':
                print('Fiz a empresa')
                driver.find_element(By.XPATH, xpath_label).send_keys(companhia)
                continue

            elif texto == 'Role in Company':
                print('Fiz a função')
                driver.find_element(By.XPATH, xpath_label).send_keys(funcao)
                continue

            elif texto == 'Address':
                print('Fiz o endereço')
                driver.find_element(By.XPATH, xpath_label).send_keys(endereco)
                continue

            elif texto == 'Email':
                print('Fiz o email')
                driver.find_element(By.XPATH, xpath_label).send_keys(email)
                continue

            elif texto == 'Phone Number':
                print('Fiz o telefone')
                driver.find_element(By.XPATH, xpath_label).send_keys(telefone)
                continue

        # Caso não encontre o elemento, ele vai para o except
        except NoSuchElementException:
            print(f'Elemento não encontrado para o índice {i}')
        
        # Clica no botão de submit
        driver.find_element_by_xpath(dict_xpaths['botao_submit']).click()
        print('Clicou no botão de submit')

resultado = driver.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[2]/div[2]')
resultado = resultado.text
print(resultado)

driver.quit()

