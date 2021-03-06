import requests
from bs4 import BeautifulSoup
url = "https://www.occ.com.mx/empleos"
page= requests.get(url)
#Ver el resultado desde la terminal
print(page.content) 
#Ver el resultado en estructura
#soup= BeautifulSoup(page.content, 'html.parser')
#results = soup.find('Business Intelligence',class_='sol_Keywords')
#print(results.prettify())
#job_elems = results.find('Business Intelligence', class_='sol_Keywords')