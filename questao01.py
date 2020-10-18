import scrapy

class UolSpider(scrapy.Spider):
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
    


