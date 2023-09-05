from requests_html import HTMLSession

sessao = HTMLSession() #1 - cria o objeto html

url = 'https://www.olx.com.br/eletronicos-e-celulares/estado-sp?q=iphone' #2 - acessa a página inicial

resposta = sessao.get(url) # 3 -vai acessar todos os imóveis

anuncios = []
links = resposta.html.find('a[class="sc-dJjYzT dOvWTZ"]')
#links = resposta.html.find('#ad-list li a')
for link in links:
    resposta_iphone = sessao.get(link.attrs['href'])
    titulo = resposta_iphone.html.find('h1', first=True).text
    preco = resposta_iphone.html.find('span[class="ad__sc-1wimjbb-1 hoHpcC sc-jTzLTM kNahTW"]', first=True).text
    anuncios.append({
        'url': link.attrs['href'],
        'titulo': titulo,
        'preco': preco
    })
    
print(anuncios)