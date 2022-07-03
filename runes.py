from bs4 import BeautifulSoup
import requests
import colorama
from colorama import Fore
colorama.init()

print("champion:")
champion = input("")

print("role:")
print("(top/jungle/middle/adc/support)")
role = input("")

url = "https://u.gg/lol/champions/" + champion + "/build?role=" + role 
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data,'html5lib')
list1 = ''

mainrunediv = soup.find("div", {"class": "perk keystone perk-active"})
print(Fore.RED + "Main")

print(Fore.YELLOW + mainrunediv.find('img').attrs['alt'])

secrunediv = soup.find_all("div", {"class": "perk perk-active"})

print(secrunediv[0].find('img').attrs['alt'])
print(secrunediv[1].find('img').attrs['alt'])
print(secrunediv[2].find('img').attrs['alt'])

print(Fore.RED + "Secondary")

print(Fore.GREEN + secrunediv[3].find('img').attrs['alt'])
print(secrunediv[4].find('img').attrs['alt'])

shards = soup.find_all("div", {"class": "shard shard-active"})

print(Fore.RED + "Shards")
print(Fore.WHITE + shards[0].find('img').attrs['alt'])
print(shards[1].find('img').attrs['alt'])
print(shards[2].find('img').attrs['alt'])

summsdiv = soup.find("div", {"class": "content-section_content summoner-spells"})
summsnr = summsdiv.find_all("img", {"class": ""})

skillpath = soup.find("div", {"class": "skill-priority-path"})
skillorder = skillpath.find_all("div", {"class": "champion-skill-with-label"})

print(Fore.RED + "Skill Order")


print(Fore.MAGENTA + skillorder[0].find('img').attrs['alt'] + " ->")
print(skillorder[1].find('img').attrs['alt'] + " ->")
print(skillorder[2].find('img').attrs['alt'])


print(Fore.RED + "Summoners")

print(Fore.CYAN + summsnr[0].attrs['alt'])
print(summsnr[1].attrs['alt'])


urlmatch = "https://u.gg/lol/champions/" + champion + "/matchups?role=" + role 
rmatch = requests.get(urlmatch)
datamatch = rmatch.text
soup1 = BeautifulSoup(datamatch,'html5lib')


toughwrcheck = soup1.find_all("div", {"class":"rt-td winrate"})

toughwrcheckcount = 0
while toughwrcheck[-1].find('b').getText() == "0.00%" :
  del toughwrcheck[-1]
  toughwrcheckcount -= 1

toughname = soup1.find_all("strong")


print(Fore.RED + "Counters")

print(Fore.BLUE + toughname[-1 + toughwrcheckcount].getText() + " - " + toughwrcheck[-1 + toughwrcheckcount].find('b').getText() )
print(toughname[-2 + toughwrcheckcount].getText() + " - " + toughwrcheck[-2 + toughwrcheckcount].find('b').getText())
print(toughname[-3 + toughwrcheckcount].getText() + " - " + toughwrcheck[-3 + toughwrcheckcount].find('b').getText())
print(toughname[-4 + toughwrcheckcount].getText() + " - " + toughwrcheck[-4 + toughwrcheckcount].find('b').getText())
print(toughname[-5 + toughwrcheckcount].getText() + " - " + toughwrcheck[-5 + toughwrcheckcount].find('b').getText())

end = input("")