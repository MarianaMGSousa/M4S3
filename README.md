<span align="center">

# M4S3

</span>

Atividade do Módulo 4 da Semana 3 do curso da Ultima School - Web Scraping


Exercício:


Para fazer um Web Scraper, além de acessar o site através de um programa, precisamos analisar o HTML desse site para encontrar a informação que desejamos. Para testar essa busca, iremos acessar o site:

'https://www.olx.com.br/eletronicos-e-celulares/estado-sp?q=iphone'

- O propósito nesse website é pegar todos os nomes (modelos) dos iPhones disponíveis. Para isso, usaremos o código da biblioteca requests_html para acessar uma página da web, encontrar todos os links de anúncios na página e extrair o título de cada anúncio. 
- O próximo passo é, para cada anúncio encontrado, acessar seu respectivo link, para que possamos coletar outros dados  nessas páginas.
- Extrair o título e o preço de cada anúncio.
- Adiciona as informações do anúncio na lista de anúncios, em um dicionário com as chaves url, titulo e preco.
- Imprime a lista de anúncios na tela.


