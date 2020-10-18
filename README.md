
# Crawler
Crawler feito em python que acessa a página do Marcado livre conforme o parametro de busca.


## Questão 2 
O Crawler é executado no arquivo questao02.py. Primeiro ele abre a página de busca do Mercado Livre salvando.
Os dados dos produtos coletados (index do produto, descrição do produto, preço, pagina) são salvos no arquivo output_ML.json. 

### Pré Requisitos

Python3 e bibliotecas selenium.

### Execução
Comando para executar o Crawler:

```
py questao02.py "produto que deve ser procurado"
```

Exemplo:
```
py consulta.py  "processador"
```


### Estrutura do projeto
O projeto é baseado em POO e utiliza threads para otimizar o processo de captura. Cada thread é responsável por 10.000 request para assim capturar os dados no melhor tempo possível.

Antes do início de construção do crawler foi feito uma análise do offers.csv para a verificação de dados nulos ou duplicados. 
Após a captura também foi feita uma pequena análise dos dados.

O arquivo Análises.ipynb contém tais análises.



## Autor

* **Jonatha Fernandes Torquato de Lima* - (https://github.com/Jonathaft)


