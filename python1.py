# print("hello world")
# print("jyotiraditya Khatua")
# print("I am a student of B.Tech in Computer Science and Engineering", "currently studying in the final year of my course.")
# name="Jyotiraditya Khatua"
# age=22
# cgpa=8.5
# isstudent=True
# print(name,age,cgpa,isstudent)
# print(type(name),type(age),type(cgpa),type(isstudent))

# name=input("enter your name:")
# print("hello"+name)


# f_name=input("enter your first name:")
# l_name=input("enter your last name:")
# print("hello "+f_name+" "+l_name)
# age=int(input("enter your age:"))
# height=float(input("enter your height:"))
# print("your age is",age,"and your height is",height)


# age=int(input("enter your age:"))
# print("your age is",age)


# age=int(input("enter your age:"))
# new_age=age+1
# print("your age after one year will be",new_age)


# age=int(input("enter your age:"))
# new_age=int(age)
# new_age1=float(new_age)
# new_age2=str(new_age1)
# print(new_age2)
# print("your age after one year will be",new_age2)

# num=1.4
# new_num=1.0+int(num)
# print(new_num)



# a=int(input("enter your first number:"))
# b=int(input("enter your second number:"))
# sum=a+b
# subs=a-b
# mul=a*b
# div=a/b
# mod=a%b
# floor=a//b

# print("the sum of two numbers is",sum)
# print("the difference of two numbers is",subs)
# print("the product of two numbers is",mul)
# print("the quotient of two numbers is",div)
# print("the remainder of two numbers is",mod)
# print("the floor division of two numbers is",floor)


# a="i am Jyotiraditya Khatua"
# print(a.upper())
# print(a.lower())
# print(a.endswith("a"))
# print(a.startswith("i"))
# print(a.replace("i","I"))
# print(a.capitalize())
# print(a.find("a"))
# print(a.count("a"))
# print(a.lstrip())
# print(a.rstrip())
# print(a.strip())
# print(a.split(" "))
# print(a.isalnum())
# print(a.center(50))
# print(a.title())
# print(a.swapcase())
# print("r" in a)


# product_a=float(input("enter the price of product A:"))
# product_b=float(input("enter the price of product B:"))
# product_c=float(input("enter the price of product C:"))

# total_price=product_a+product_b+product_c
# average_price=total_price/3

# print("the total price of three products is",total_price)
# print("the average price of three products is",average_price)

# super_hero=input("enter your favorite superhero:")
# print(super_hero.startswith("s"))
# print(super_hero.startswith("S"))


# print(2+3)
# print(2-3)
# print(2*3)
# print(2/3)
# print(2%3)
# print(2**3)
# print(2//3)



# x=2
# x=x+3
# print(x)
# x+=3
# x+=2
# print(x)
# x-=3
# x=x-1
# x-=1
# print(x)
# x*=3
# x/=3
# x//=3
# x**=3
# print(x)




# a=10
# b=20
# print(a==b)
# print(a!=b)
# print(a>b)
# print(a<b)
# print(a>=b)
# print(a<=b)

# a=90
# b=80
# print(a and b)
# print(a or b)
# print(not a)
# print(not b)
# print(a and not b)


# print(True)
# print(not True)



# marks=int(input("enter your marks:"))

# if marks>=90 and marks<=100:
#     print("you got A grade")
# elif marks>=80 and marks<90:
#     print("you got B grade")
# elif marks>=70 and marks<80:
#     print("you got C grade")
# elif marks>=60 and marks<70:
#     print("you got D grade")
# elif marks>=50 and marks<60:
#     print("you got E grade")
# else:
#     print("failed")



# age=int(input("enter your age:"))
# if age>25:
#     print("you are eligible for marriage")
# elif age>18 and age<=25:
#     print("you are not eligible for marriage")
# else:
#     print("you are not eligible for marriage")

# age=int(input("enter your age:"))
# if age>=18 and age<=100:
#     print("you are eligible for voting")
# elif age>0 and age<18:
#     print("you are not eligible for voting")
# else:
#     print("invalid age")


# c=int(input("enter your age:"))
# if c>=25 and c<=48:
#     print("you are eligible for marriage")
# elif c>=18 and c<25:
#     print("you are not eligible for marriage")
# else:
#     print("invalid age")


# num1=int(input("enter your first number:"))
# num2=int(input("enter your second number:"))
# operation=input("enter your operation(+,-,*,/):")

# while True:

#    if operation=="+":
#        print("the sum of two numbers is",num1+num2)
#    elif operation=="-":
#        print("the difference of two numbers is",num1-num2)
#    elif operation=="*":
#     print("the product of two numbers is",num1*num2)
#    elif operation=="/":
#     if num2==0:
#         print("division by zero is not allowed")
#     else:
#         print("the quotient of two numbers is",num1/num2)
#    else:
#     print("invalid operation")

#    print("do you want to continue? yes or no")
#    if input()=="yes":
#       num1=int(input("enter your first number:"))
#       num2=int(input("enter your second number:"))
#       operation=input("enter your operation(+,-,*,/):")
#    else:
#       break
# print("thank you for using the calculator")


# num=int(input("enter a number:"))
# num1=int(input("enter a number:"))
# operation=input("enter your operation(+,-,*,/):")

# if operation=="+":
#     print("the sum of two numbers is",num+num1)
# elif operation=="-":
#     print("the difference of two numbers is",num-num1)
# elif operation=="*":
#     print("the product of two numbers is",num*num1)
# elif operation=="/":
#     if num1==0:
#         print("division by zero is not allowed")
#     else:
#         print("the quotient of two numbers is",num/num1)
# else:
#     print("invalid operation")


# nums=range(5,16)
# print(nums)



# from operator import index


# count=0
# while count<=5:
#     print("apna college")
#     count+=1
#     print("end of loop")


# i=5
# while i>=0:
#     print(i*"hello")
#     i-=1

# nums=range(5)
# for i in nums:
#     print(i)

# for i in range(5):
#     print(i)

# for i in range(1,5001):
#     print(i)



# for i in range(1,11):
#     if i%2==0:
#         print(i,"is even")
#     else:
#         print(i,"is odd")

# for i in range(2,11,2):
#     print(i,"is even")


# for i in range(1,51):
#     if i%3==0:
#         print(i,"is divisible by 3")
#         if i==21:
#           break
#           print("loop is broken")


# for i in range(1,21):
#     if i%2!=0:
#         print(i,"is odd")
#     else:
#         print(i,"is even")

# i=1
# while i<=10:
#     print(57*i)
#     i+=1


# for i in range(1,51):
#     if i%3==0:
#         print(i,"is divisible by 3")

#         if i==15:
#             i+=1
#             continue
#             print("loop is broken")
#         i+=1

# a=int(input("enter your first number:"))
# b=int(input("enter your second number:"))
# for i in range(1,1001):
#     if i%a==0 and i%b==0:
#         print(i,"is divisible by both",a,"and",b)
#     else:
#         print(i,"is not divisible by both",a,"and",b)


# marks=[90,80,70,60,50,40,30,20,10,"A"]
# marks.append(100)
# print(marks)

# marks=[90,80,70,60,50,40,30,20,10,"A"]
# marks1=["B", "C", "D"]
# marks.extend(marks1)
# print(marks)

# marks=[90,80,70,60,50,40,30,20,10]
# marks.sort()
# print(marks)


# marks=[90,80,70,60,50,40,30,20,10]
# marks.reverse()
# print(marks)


# marks=[90,80,70,60,50,40,30,20,10]
# marks.clear()
# print(marks)

# marks=[90,80,70,60,50,40,30,20,10,"A"]
# print(marks[0:3])
# print(marks[:])
# print(marks[3:])


# marks=[90,80,70,60,50,40,30,20,10,"A"]
# for i in marks:
#     print(i)


# b=(1,2,3,4,5)
# print(b.count(2))

# b=(1,2,3,4,5)
# print(b.index(3))

# m={1,2,3,4,5}
# print(m.add(6))
# print(m)


# marks={"maths":80,"physics":90,"chemistry":70}
# marks["biology"]=60
# print(marks["maths"])
# print(marks)

# marks={"maths":80,"physics":90,"chemistry":70}
# for key in marks:
#     print(key,marks[key])


# l=[101,102,103,104,105,101]
# p=set(l)
# q=list(p)
# print(q)


# employee=[(101,"Alice",50000),
#           (102,"Bob",60000),
#           (103,"Charlie",70000)]
# print(employee.index((101,"Alice",50000)))


# def greet(name):
#     print("hello",name)

# greet("jyotir")

# def sum(a,b):
#     sum=a+b
#     print(sum)

# sum(3,4)

# def gst(price):
#     return price*0.18
    

# print(gst(990))

# def calc_price(usd_val):
#     inr_val=usd_val*88
#     print("usd_val",usd_val,"inr_val",inr_val)

# calc_price(90)

# b=["l","o","m","n","p","q"]
# def lambai(list):
#     return len(list)

# print(lambai(b))


# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#         print(fact)

# factorial(7)


# def fibonacci(n):
#     if n==0 or n==1:
#         return n
#     else:
#       return fibonacci(n-1)+fibonacci(n-2)

# print(fibonacci(8))


# def fibbonacci(n):
#     a=0
#     b=1
#     count=0
#     while count<n:
#         print(a,end="")

#         c=a+b
#         a=b
#         b=c

#         count+=1

# fibbonacci(10)


def sum(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
        print(sum)
        i+=1

sum(10)


def hello():
    print("good morning")

hello()


import math


print(dir(math))



import random

print(random.randint(1,10))