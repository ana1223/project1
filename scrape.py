from bs4 import BeautifulSoup
import urllib2
print ("starting to scrape")

#Use code below when file to import is on web server :
response = urllib2.urlopen("http://www.goheels.com/SportSelect.dbml?DB_OEM_ID=3350&SPID=12965&SPSID=667867&SITE=UNC&DB_OEM_ID=3350")
html = response.read()

soup = BeautifulSoup(html)

tabledata = soup.find("table", {"id" : "roster-table"})
player_names = []
player_links = []
player_position = []

for link in tabledata.find_all('a'):
    player_links.append(link.get('href'))
    player_names.append (link.get('title'))

print player_names

for position in tabledata.find_all("td", {"class" : "position"}):
    player_position.append(position.text.strip())

print player_position