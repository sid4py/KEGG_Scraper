from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://www.kegg.jp/kegg/catalog/org_list.html'

html = urlopen(url).read()

htmlFile = BeautifulSoup(html, "html.parser")

tagList = htmlFile('a')

FH = open('orgList.txt')
OUT = open('orgCode.txt', 'w')

for org in FH :
	org = org.rstrip()
	for i in range(len(tagList)) :
		if tagList[i].contents[0] == org :
			print (tagList[i-1].contents[0], end='\t')
			print (org)
			OUT.write(tagList[i-1].contents[0] + '\t' + org + '\n')

FH.close()
OUT.close()
