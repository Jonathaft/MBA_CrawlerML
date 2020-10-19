import scrapy

class UolSpider(scrapy.Spider):
    """
    Classe que coleta a cotação do dolar no site da UOL 
    Para executar :
        - scrapy runspider questao01.py --nolog
        ou
        - scrapy runspider questao01.py -s LOG_ENABLED=False
    """
    name = 'uol_spider'
    start_urls = ['https://www.uol.com.br']
    
    def parse(self, response):
        dolar = response.css('.HU_currency__quote::text')
        print('--------------------------------------')
        
        
        valor_dolar =  dolar[0].extract().strip()
        if valor_dolar != "":
            #yield {'titulo': titulo}
            print('| O valor do dolar é:', valor_dolar, '         |' )
        print('--------------------------------------')
    


