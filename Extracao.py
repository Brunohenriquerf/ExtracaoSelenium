# Importar bibliotecas
from selenium import webdriver
from time import sleep
import selenium
from selenium.webdriver.chrome.options import Options
import pandas as pd
from pandas import DataFrame
from IPython.display import display

# Definir tamanho da janela e ignorar erros
options = Options()
options.headless = True
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('window-size=1200,800')


# Selecionar navegador e opções
navegador = webdriver.Chrome(options=options)

# Acessar o site
navegador.get("LINK DO SITE A SER EXPLORADO")

# Esperar a pagina carregar
sleep(3)

# Preparar array para receber informações
receptor = []

# Passa por cada pagina
for h in range(1,20):
    print('\n')
    print("Pagina" + str(h) +"!")
    print('\n')
    navegador.get("LINK DO SITE A SER EXPLORADO" + str(h) + "/PAGINA QUE INICIAREMOS A COLETA")
        # Passa por cada linha de anúncio
    for i in range(1,8):
        # Passa por cada fileira
        for j in range(1,4):
            # Para suportar as exceções e erros
            try:
                col1 = str(navegador.find_element_by_xpath('/html/body/div[1]/div[4]/div[' + str(i) + ']/div[' + str(j) + ']/div/div/h4[1]').text)                   
                col2 = str(navegador.find_element_by_xpath('/html/body/div[1]/div[4]/div[' + str(i) + ']/div[' + str(j) + ']/div/div/h4[2]').text)
                col3 = str(navegador.find_element_by_xpath('/html/body/div[1]/div[4]/div[' + str(i) + ']/div[' + str(j) + ']/div/div/h4[3]').text)
                col4 = str(navegador.find_element_by_xpath('/html/body/div[1]/div[4]/div[' + str(i) + ']/div[' + str(j) + ']/div/div/ul/li[1]').text)
                col5 = str(navegador.find_element_by_xpath('/html/body/div[1]/div[4]/div[' + str(i) + ']/div[' + str(j) + ']/div/div/ul/li[2]').text)                  
                col6 = str(navegador.find_element_by_xpath('/html/body/div[1]/div[4]/div[' + str(i) + ']/div[' + str(j) + ']/div/div/ul/li[3]').text)
                col7 = str(navegador.find_element_by_xpath('/html/body/div[1]/div[4]/div[' + str(i) + ']/div[' + str(j) + ']/div/div/ul/li[4]').text)
                # Coletar e jogar as informações na tabela
                receptor.append((col1,
                                    col2,
                                    col3,
                                    col4,
                                    col5,
                                    col6,
                                    col7))
            # Exceção para as páginas com anuncios faltantes
            except:
                print("############## Pulei ##############")   
            display(receptor)              

for h in range(1,7):
    print('\n')
    print("Pagina" + str(h) +"!")
    print('\n')
    navegador.get("LINK DO SITE A SER EXPLORADO" + str(h) + "/PAGINA QUE INICIAREMOS A COLETA")
    for i in range(1,8):
        for j in range(1,4):
            try:
                col1 = str(navegador.find_element_by_xpath('/html/body/div[1]/div[4]/div[' + str(i) + ']/div[' + str(j) + ']/div/div/h4[1]').text)                   
                col2 = str(navegador.find_element_by_xpath('/html/body/div[1]/div[4]/div[' + str(i) + ']/div[' + str(j) + ']/div/div/h4[2]').text)
                col3 = str(navegador.find_element_by_xpath('/html/body/div[1]/div[4]/div[' + str(i) + ']/div[' + str(j) + ']/div/div/h4[3]').text)
                col4 = str(navegador.find_element_by_xpath('/html/body/div[1]/div[4]/div[' + str(i) + ']/div[' + str(j) + ']/div/div/ul/li[1]').text)
                col5 = str(navegador.find_element_by_xpath('/html/body/div[1]/div[4]/div[' + str(i) + ']/div[' + str(j) + ']/div/div/ul/li[2]').text)                  
                col6 = str(navegador.find_element_by_xpath('/html/body/div[1]/div[4]/div[' + str(i) + ']/div[' + str(j) + ']/div/div/ul/li[3]').text)
                col7 = str(navegador.find_element_by_xpath('/html/body/div[1]/div[4]/div[' + str(i) + ']/div[' + str(j) + ']/div/div/ul/li[4]').text)
                receptor.append((col1,
                                    col2,
                                    col3,
                                    col4,
                                    col5,
                                    col6,
                                    col7))
            except:
                print("############## Pulei ##############")   
            display(receptor)

for h in range(1,17):
    print('\n')
    print("Pagina" + str(h) +"!")
    print('\n')
    navegador.get("LINK DO SITE A SER EXPLORADO" + str(h) + "/PAGINA QUE INICIAREMOS A COLETA")
    for i in range(1,8):
        for j in range(1,4):
            try:
                col1 = str(navegador.find_element_by_xpath('/html/body/div[1]/div[4]/div[' + str(i) + ']/div[' + str(j) + ']/div/div/h4[1]').text)                   
                col2 = str(navegador.find_element_by_xpath('/html/body/div[1]/div[4]/div[' + str(i) + ']/div[' + str(j) + ']/div/div/h4[2]').text)
                col3 = str(navegador.find_element_by_xpath('/html/body/div[1]/div[4]/div[' + str(i) + ']/div[' + str(j) + ']/div/div/h4[3]').text)
                col4 = str(navegador.find_element_by_xpath('/html/body/div[1]/div[4]/div[' + str(i) + ']/div[' + str(j) + ']/div/div/ul/li[1]').text)
                col5 = str(navegador.find_element_by_xpath('/html/body/div[1]/div[4]/div[' + str(i) + ']/div[' + str(j) + ']/div/div/ul/li[2]').text)                  
                col6 = str(navegador.find_element_by_xpath('/html/body/div[1]/div[4]/div[' + str(i) + ']/div[' + str(j) + ']/div/div/ul/li[3]').text)
                col7 = str(navegador.find_element_by_xpath('/html/body/div[1]/div[4]/div[' + str(i) + ']/div[' + str(j) + ']/div/div/ul/li[4]').text)
                receptor.append((col1,
                                    col2,
                                    col3,
                                    col4,
                                    col5,
                                    col6,
                                    col7))
            except:
                print("############## Pulei ##############")   
            display(receptor)
                
# Definir as colunas que receberão os dados
cols=['col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7']
# Preparar o dataframe
df = pd.DataFrame(receptor, columns=cols)
# Mostrar o dataframe no VS Code
display(df) 
# Converter e salvar a tabela em CSV no local raiz deste código
df.to_csv(path_or_buf='NOME DA TABELA QUE SERÁ SALVA', sep=',', na_rep='', float_format=None, columns=None, header=True, index=True, index_label=None, mode='w', encoding=None, compression='infer', quoting=None, quotechar='"', line_terminator=None, chunksize=None, date_format=None, doublequote=True, escapechar=None, decimal='.', errors='strict', storage_options=None)        
                
