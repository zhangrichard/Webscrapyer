import urllib
import re
import requests
from pattern import web
import pandas as pd
from bs4 import BeautifulSoup 
# read the website
defaultUrl = "http://www.whosdatedwho.com/dating/"
sampleUrl = ["http://www.whosdatedwho.com/dating/gregg-sulkin","http://www.whosdatedwho.com/dating/bella-thorne"]
# htmlfile = urllib.urlopen('http://www.whosdatedwho.com/')
# htmltext = htmlfile.read()
# i = 0
# get inside title tag 

testname = "Jake T. Austin"
p = re.split(r'[;,.\s]\s*',testname)
print type("-".join(p))
regex = '<a href="/dating/gregg-sulkin">Gregg Sulkin</a>'
pattern = re.compile(regex)


# return list of relationship
def get_relationship(name):
	link = defaultUrl+name
	r = requests.get(link)
	soup = BeautifulSoup(r.text,"html.parser")
	relations = soup.body.find_all("p",class_="ff-auto-relationships")
	resultSet = []
	# for e in relations:
	# 	resultSet[e.a.get_text()] = {}
	# for k in relations[0].find_all("a")[1:]:
	# 	name = k.get_text().split()
		# print "http://www.whosdatedwho.com/dating/"+name[0]+"-"+name[1]
	for k in relations[0].find_all("a")[:]:
		resultSet.append(k.get_text().split()[0]+"-"+k.get_text().split()[1])

	# print resultSet
	return resultSet
result = {}
result["bella-thorne"] = get_relationship("bella-thorne")
# result["Britt-Robertson"] = temp

# for i in temp:
# 	print i 
# 	result["Britt-Robertson"][str(i)] = get_relationship(i)
print result
def get_relavant_relation(html):
	# dom = web.Element(html)
	### 0. get the website
	### 1. get the relation
	# print dom.by_tag
	r = requests.get(html)
	soup = BeautifulSoup(r.text,"html.parser")

	# bs.find_all("div",class= "ff-current-relationship.ff-has-readmore")
	# print bsText.findall
	# cssSoup = bs("<div class = ff-current-relationship.ff-has-readmore>")
	# print soup.find_all("div")
	### get the css soup
	relations = soup.body.find_all("p",class_="ff-auto-relationships")
	print type(relations)
	print "####\n"

	### get the name of the relations
	resultSet = {}
	# for e in relations:
	# 	resultSet[e.a.get_text()] = {}
	for k in relations[0].find_all("a")[1:]:
		name = k.get_text().split()
		print "http://www.whosdatedwho.com/dating/"+name[0]+"-"+name[1]
	resultSet[relations[0].a.get_text()]= [k.get_text()for k in relations[0].find_all("a")[1:]]

	print resultSet
	return resultSet
	### output to json format
		

	# relation = []
	# return relation

print type(get_relavant_relation("http://www.whosdatedwho.com/dating/Britt-Robertson"))

# parse the relavent content
# for i in range(0,2):
# 	htmlfile = urllib.urlopen(sampleUrl[i])
# 	htmltext = htmlfile.read()
# 	# titles = re.findall(pattern,htmltext)
# 	print htmltext
# structure data in dictionary format


# print htmltext