# day='Monday'
# if day=='Monday':
#     print("Holiday")
# elif day=='Sunday':
#     print("WorkinG")
# else:
#     print("ANUJ")
# name=(input("what is your name: "))
# if name=='Anuj':
#     print("YES")
# elif name=='Gautam':
#     print("NO")
# else:
#     print("Zero")    
# num1=int(input("enter number: "))
# num2=int(input("enter number: "))
# operation=(input("enter operation"))
# if operation=='+':
#     print(num1+num2)
# elif operation=='-':
#     print(num1-num2)
# elif operation=='*':
#     print(num1*num2)
# elif operation=='/':
#     print(num1/num2)
# elif operation=='**':
#     print(num1**num2)
# else:
#     print(num1//num2)
# a=int(input("number one: "))
# b=int(input("number two: "))
# c=int(input("number three: "))
# if a or c>b:
#     print("a is bigger")
# elif b>a or c:
#     print("b is smaller")
# else:
#     print("error")
# num=int(input("enter your number: "))
# if num % 2==0 and num % 5==0:
#     print("divisible by both")
# elif num % 2==0:
#     print("divisible by 2")
# elif num % 5==0:
#     print("divisible by 5")
# else:
#     print("divisible by none")
# for i in range(0,100,2):
#     print(i)
# for i in range(1,101,2):
#     print(i)
# for i in reversed(range(0,100)):
#     print(i)

# for i in range(0,100,4):
# #     print(i)
# for i in range(0,100,4):
#     print(i,end=" ")
# temperature = 15
# if temperature > 25:
#     print("Hot")
# elif temperature >= 15:
#     print("Cool")
# else:
# #     print("Cold")
# colors = ["red", "blue"]
# for color in colors:
#     print(color)
# for number in range(2,10,2):
#     print(number)
# name=input()
# for i in range(1,8):
#     print()
#     for j in range(i):
#         print(j, end=" ")
# total=1
# for i in range(1,11):
#     total=total*i
# print(total)
# i=1
# while True:
#     print(i)
#     i+=1
# i=1
# count=0
# while count<25:
#     if i%2==0:
#         print(i)
#         count+=1
#     else:
#         print("Odd")
# i=0
# while i<100:
#     if i %2!=0:
#         print(i)
#     i+=1
# for i in range(1,8):
#     print()
#     for j in range(i):
#          print(i, end=" ")
# name=""
# count=0
# while name.lower()!="anuj" and count<5:
#     name=(input("enter something: "))
#     print(f"This is {name}")
#     count+=1
# password=""
# count=0
# while password!='python123' and count<3:
#     password=input("enter something: ")
#     if password=="python123":
#         print("access granted")
#     else:
#         print("account locked")
#         count+=1
# say=""
# count=0
# while say.lower()!='yes' and count<5:
#     say=input("tell me: ")
#     print(f"i think {say}")
#     count+=1
# positive=0
# negative=0
# zero=0
# i=0
# while i<10:
#     num=int(input("enter a number: "))

#     if num<0:
#         positive+=1
#     elif num<0:
#         negative+=1
#     else:
#         zero+=1
#     i+=1
# count=0
# while count<10:
#     print(count)
#     count+=1
#     if count==6:
#      break
# a=[1,2,3,4,5,6,7,'hello',123,0]
# a.append('Anuj')
# print(a)
# a=[1,2,3,4,5,6,7,'hello',123,0]
# b=a
# print(b.pop(4))
# print(b)
# secret=19
# attempts=0
# while attempts <7:
#     guess=int(input("Enter your secret: "))
#     attempts+=1
#     if guess ==secret:
#         print("correct")
#     elif guess > secret:
#         print("Too high")
#     else:
#         print("Too low")
#     if guess!=secret:
#         print("you used all 7 attempts")
# ages=[19,22,19,24,20,25,26,24,25,24]
# minimum=min(ages)
# maximum=max(ages)
# average=sum(ages)/len(ages)
# print(minimum)
# print(maximum)
# print(average)

# age_range=maximum-minimum
# print(age_range)
# ages=[19,22,19,24,20,25,26,24,25,24]
# print(ages[::-1])
# a='hello'
# b=15
# try:
#     x=a+b
# except TypeError:
#     print("Not Possible")
# a=9
# b=0
# try:
#     x=a/b
# except ZeroDivisionError as e:
#     print(e)
# def anuj(num):
#     if num<4:
#         result=num/(num-3)
#     print(result)

# try:
#     anuj(0)
#     anuj(1)
#     anuj(3)
#     anuj(2)
# except:
#     print("Not Valid")
# f=open("handling.txt",'a')
# f.write("amigo")
# f.close()

# import requests
# from bs4 import BeautifulSoup
# url = "https://books.toscrape.com/"
# response=requests.get(url)
# soup=BeautifulSoup(response.text, 'html.parser')

# a= (soup.find("div", class_="product_price"))
# print(a.p.text)

























