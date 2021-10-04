import requests
from bs4 import BeautifulSoup

URL = "https://projecteuler.net/problem="

for url in range(1, 101):

	page = requests.get(URL + str(url))
	content = page.content
	soup = BeautifulSoup(content, "html.parser")

	number = soup.find("h3").text
	title = soup.find("h2").text
	problem = soup.find_all("p")

	for line in problem:
		with open(f"{number} - {title}.py", "w") as file:
			for line in problem:
				file.write(f'# {line.text} \n')
