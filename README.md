
# Crawler
* Questão 01 - Crawler que coleta a cotação atual do dolar no site da UOL.
* Questão 02 - Crawler feito em python que acessa a página do Marcado livre conforme o parametro de busca.


## Questão 1 
O Crawler é executado no arquivo questao01.py. Primeiro ele abre a página do Mercado Livre aplicando a busca do produto informado no parametro de execução. Em seguida os dados coletados dos produtos (index do produto, descrição do produto, preço, pagina) são salvos no arquivo output_ML.json. 


## Questão 2 
O Crawler é executado no arquivo questao02.py. Primeiro ele abre a página do Mercado Livre aplicando a busca do produto informado no parametro de execução. Em seguida os dados coletados dos produtos (index do produto, descrição do produto, preço, pagina) são salvos no arquivo output_ML.json. 

### Pré Requisitos

Python3 e bibliotecas selenium. 
Navegador Firefox

### Execução
Comando para executar o crawler - Questão 01:

```
scrapy runspider questao01.py --nolog
OU
scrapy runspider questao01.py -s LOG_ENABLED=False
```

Comando para executar o Crawler - Questão 02:

```
py questao02.py "produto que deve ser procurado"
```


## Autor

* **Jonatha Fernandes Torquato de Lima* - (https://github.com/Jonathaft)


