# def Anuj(name):
#     print(name," says be cool")

# name=input("enter a name: ")
# Anuj("Anuj")
# def is_even():
#     num=int(input("enter your number: "))
#     if num %2==0:
#         return f"{num} is even"
#     else:
#         return f"{num} is not even"
# print(is_even())
# class Modelling:
#     def __init__(self,skincolour):
#         self.skincolour=skincolour
#         self.hair='black'

# class male():
#     def __init__(self,job):
#         self.job=job

# class female(Modelling,male):
#     def __init__(self, skincolour,job,height):
#         super().__init__(skincolour)
#         self.job=job
#         self.height=height
#     def output(self):
#         print(f"{self.skincolour} {self.hair} {self.job} {self.height}")

# o=female('brown','runway',"above 5'9")
# o.output()
# class father:
#     def __init__(self):
#         self.__salary =100000

#     def __deposit(self, amount):
# import requests
# web_url="https://www.skyscanner.net/flights?market=uk&locale=en-gb&currency=gbp&referralServiceVersion=meeseeks-referral-service-v1&associateid=AFF_TRA_19354_00001&campaign_id=2283642&adid=1477112&click_timestamp=1793599891888&irmweb=&afsrc=1"
# response=requests.get(web_url)
# response.headers
# print(response.headers)
import requests
from bs4 import BeautifulSoup
url = "https://books.toscrape.com/"
response=requests.get(url)
soup=BeautifulSoup(response.text, 'html.parser')

a = soup.find("div", class_="cover-item-content__title")
print(a)


















