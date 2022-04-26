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

toughmatch = soup.find_all("div", {'class':'champion-name'})

print(Fore.RED + "Counters")

print(Fore.BLUE + toughmatch[0].get_text())
print(toughmatch[1].get_text())
print(toughmatch[2].get_text())
print(toughmatch[3].get_text())
print(toughmatch[4].get_text())

end = input("")