
    
import requests
from bs4 import BeautifulSoup as bs

def getNumberOfContributors(url):
    """ Dado  uma URL de um repositório do GitHub, retorna o número de contribuidores do repositório """

    # Fazendo uma requisição HTTP
    req = requests.get(url)

    # Lendo o conteúdo HTML da página requisitada
    soup = bs(req.content,"html.parser")

    # Salvando uma lista com o conteúdo de todas as tags da classe "Counter" da página
    counters = soup.find_all('span', {'class' : "Counter"})

    # O número de contribuidores é o título da última tag de classe "Counter da página"
    nContrib = counters[-1]['title']
    
    # Retornando o numero de contribuidores + 1(o próprio criador do repositorio)
    return nContrib + 1