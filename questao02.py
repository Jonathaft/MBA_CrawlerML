from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import json
import sys


def finds(browser, by, expression):
    try:
        return browser.find_elements(by, expression)
    except NoSuchElementException as nse:
        return None

def find(browser, by, expression):
    try:
        return browser.find_element(by, expression)
    except NoSuchElementException as nse:
        return None

# Tratamento dos parametros enviados para execução 
# Todo: Inserir parametros de qtd de Páginas que devem ser Escaneadas
if len(sys.argv ) > 1:
    print('Argumento de busca [{}]'.format(sys.argv[1] ))
    busca = sys.argv[1]
else:
    print('Precisa de um  Argumento de busca!!! Bye Bye .... ')
    exit()


# Criando o arquivo de saida no modo escrita 
output  = open('output_ML.json', 'w', encoding='utf-8')

driver = webdriver.Firefox()
#driver = webdriver.Chrome()

# Monta a URL de busca com o Parametro 
url_main = "https://lista.mercadolivre.com.br/{}".format(busca)

# Variaveis de Controle 
log = True # se True exibe os dados coletados durante a execução via "print"
continua = True 
index_produto = 0
qtd_paginas = 0 # Quantidade de paginas que devem ser escaneadas. (0 == ALL) 
pagina = 0

while continua:    
    pagina += 1
    
    # Controle de quantidades de paginas escaneadas
    if (qtd_paginas > 0 and pagina > qtd_paginas):
        break

    
    print('Abrindo pagina [{}] com a url [{}]'.format(pagina, url_main))
    print('*'*100)
    # iniciando a busca 
    driver.get(url_main)
    #items = finds(driver, By.CLASS_NAME, 'ui-search-result__content-wrapper')
    items = finds(driver, By.CLASS_NAME, 'ui-search-result__content') # essa classe possibilita pegar a URL
    for item in items:
        print('-------------------------------------------------------------------')        
        try:
            # Tratamento devido alguns pordutos vir fora do padrao esperado na DIV             
            descricao = find(item, By.CLASS_NAME, 'ui-search-item__title').get_property("textContent")
            desc_url = item.get_property('href')              
            #print('desc_url', desc_url, 'LEN', type(desc_url))
            fraction = find(item, By.CLASS_NAME, 'price-tag-fraction').get_property("textContent").strip()             
            fraction = fraction.replace('.', '')
            percent_ = find(item, By.CLASS_NAME, 'price-tag-cents') #.get_property("textContent").strip() #price-tag-cents
            percent = '00'
            if percent_:
                percent = percent_.get_property("textContent").strip()
                percent = percent.replace('.', '')
        except Exception as err:
            print('EROOO >>>>>>>>>>>>>>>>>>', str(err))
            continue
           
        # preco = find(item, By.CLASS_NAME, 'area-bloco-preco').get_property("textContent")
        # Formatando o valor de preco
        preco = '{}.{}'.format(fraction, percent)
        preco = preco.replace('R$', '')
        preco = preco.replace('\,', '.')
        preco = preco.strip()
        index_produto += 1
        
        if log:
            print(descricao) 
            print(fraction)
            print(percent)
            print(preco)

        # montando o dicionario 
        item = {'index': index_produto, 'descricao': descricao, 'preco': preco, 'pagina': pagina , 'link': desc_url}
        
        # Salvando o dicionario no arquivo 
        output.write(json.dumps(item))
        output.write('\n')

    # Buscando a box de Navegação PROXIMA>>
    proxima_pag = find(driver, By.CLASS_NAME, 'andes-pagination__button--next')
        
    if proxima_pag != None:
        print(' Achou a box proxima. Vamos  para proxiuma pagina >>>... pagina[{}]'.format(pagina))        
        # Coleta a url da box Proxima 
        url_main = find(proxima_pag, By.CLASS_NAME, 'andes-pagination__link').get_attribute('href')                
    else:
        # Não encontramos a box "PROXIMA" o que indica que estamos na ultima página
        print("Ultima pasta, Processo concluido com Sucesso! \n")        
        print("“Em Deus eu acredito, todos os outros tragam-me dados.” - Edward Deming")        
        
        # Encerramos o Loop while 
        break

driver.close()