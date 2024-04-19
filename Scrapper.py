import requests
from bs4 import BeautifulSoup
import apiIA

# URL de la page à récupérer
url = "https://www.infosecurity-magazine.com/risk-management/"  # Remplacez cette URL par l'URL de la page que vous souhaitez parser

# Récupérer la page web

def recupLastPage(url):
    response = requests.get(url)
    # Assurer que la requête a réussi
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all divs with class "content-info"
        all_content_info_divs = soup.find_all('div', class_='content-info')

        # Check if there are any divs found
        if all_content_info_divs:
            # Get the last div
            last_content_info_div = all_content_info_divs[0]
            a_tag = last_content_info_div.find('a')
            href_value = a_tag["href"]
            # Print or process the found div
            return href_value
        else:
            print("No 'content-info' divs found on the page.")
    else:
        print("Failed to retrieve the webpage")



def loadData(url):
    response = requests.get(url)
    # Assurer que la requête a réussi
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all divs with class "content-info"
        all_content_info_divs = soup.find_all('div', class_='page-content')
        return all_content_info_divs
 

def div_to_text(data_load):
        # Extraire le texte de chaque balise <p> et les concaténer avec des sauts de ligne
    paragraphs = [p.get_text() for p in data_load.find_all('p')]
    text = '\n\n'.join(paragraphs)
    return text

def to_site(url_sujet):
    urlToScrapp = recupLastPage(url)
    data = loadData(urlToScrapp)
    text = div_to_text(data[0])  # Ne pas appeler data[0] comme une fonction, data[0] est déjà un objet Tag
    post=apiIA.toAI(text)
    return post

if __name__ == '__main__':
    urlToScrapp = recupLastPage(url)
    print(urlToScrapp)
    data = loadData(urlToScrapp)

    text = div_to_text(data[0])  # Ne pas appeler data[0] comme une fonction, data[0] est déjà un objet Tag

    post=apiIA.toAI(text)
    print(post)