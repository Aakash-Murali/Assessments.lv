# -*- coding: utf-8 -*-
"""LVADSUSR136_AAKASHMURALI_IA1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14Zs5B1BJg7FDt73dHXnyo7EdVVfBbR9A

AAKASH MURALI 4344 INTERNAL ASSESMENT - 1

LAB SECTION - 1
"""

#1

length=float(input("Enter length in meters :"))
width=float(input("Enter width in meters :"))
area = length * width
category=None;
if(area>1000):
  category = "large"
elif(area>500):
  category = "medium"
else:
  category="small"
print("The property falls under \" "+category+" \" category")

#2

height=float(input("Enter height in cm :"))
weight=float(input("Enter weight in kg :"))

#assuming this is the formula(actual might vary)
bmi=(height/(weight*2))

if(bmi<1):
  print(f"Your bmi is {bmi} and you fall under fat category")
elif(bmi>1 and bmi <2):
  print(f"Your bmi is {bmi} and you fall under normal category")
else:
  print(f"Your bmi is {bmi} and you fall under lean category")

#3

class students:
  def __init__(self,id,name,marks={}):
    self.id=id
    self.name=name
    self.marks=marks

  def printinfo(self):
    print("ID : ",self.id)
    print("Name : ",self.name)
    print("marks : ",self.marks)
    print('--------------------')

records=int(input("Enter No.of records : "))
id=1
lists=[]
for i in range(records):
  name=input("Name : ")
  english=int(input("Marks in english :"))
  maths=int(input("Marks in maths :"))
  science = int(input("Marks in science :"))
  marks={"english":english,"maths":maths,"science":science}
  lists.append(students(id,name , marks))
  id+=1

for i in range(records):
  lists[i].printinfo()

change=int(input("which id to change ? "))
name=input("Name : ")
english=int(input("Marks in english :"))
maths=int(input("Marks in maths :"))
science = int(input("Marks in science :"))
marks={"english":english,"maths":maths,"science":science}
lists[change-1]=students(id,name , marks)

"""LAB SECTION -2"""

#4

age=int(input("Enter age :"))
category=None
if(age>60):
  category="old"
elif(age>30):
  category="adult"
elif(age>18):
  category="teen"
else:
  category="children"
print(category)

#5

id=[1,2,3,4,5,6,7,8,9] #assuming this is the id's from database
even_lists=[]
for i in id:
  if(i%2==0):
    even_lists.append(i)
print(even_lists)

#6

correct_password="123456"
print("Enter the password : ")
while(True):
  password=input()
  if(password==correct_password):
    print("Login successfull")
    break
  else:
    print("wrong password , retry...")

"""LAB SECTION - 3"""

#7

feedbacks=[]
average=0
records=int(input("Enter NO.Of Customers :"))
for i in range(records):
  print("customer -",i+1)
  feedbacks.append(int(input("Feedback Score( 1-5 ): ")))
  average+=feedbacks[i]
average/=records
if(average==5):
  print("Feedback -Excellent")
elif(average>3):
  print("Feedback - Need to improve")
else:
  print("Feedback -Worse")

#8

comment=input("Enter a comment : ")
comment = comment.lower()
vowel_count=0
vowel_count+=comment.count('a')
vowel_count+=comment.count('e')
vowel_count+=comment.count('i')
vowel_count+=comment.count('o')
vowel_count+=comment.count('u')
print("vowel count -",vowel_count)
#can also be done with combination of 'if' and 'or' stmts

#9

import datetime
dt_time_now=datetime.datetime.now()
if(int(str(dt_time_now)[8:10])>20):
  print("urgent")
else:
  print(str(dt_time_now)[8:10]," - no reminders")

"""LAB SECTON - 4"""

#10

outstanding_load=10000
repayment=int(input("Enter amount to repay :"))
try:
  remaining_loan=outstanding_load-repayment
  print("remaining - ",remaining_loan)
except:
  print("Enter proper amount ...")

#11

#let the candidates be numbered from 1 to 5
vote=int(input("Enter your choice :"))
if(type(vote)==int and vote<6 and vote>0):
  print("voted succesfully")
else:
  print("enter correct format")

#12

#lets say (atomicity/acidity) is a formula to to find a scientific result...
from logging import NullHandler
atomicity=float(input("Enter the aotmicity :"))
acidity=float(input("Enter the acidity :"))
try:
  print("result : ",(atomicity/acidity))
except :
  print("can't divide by 0")

"""LAB SECTION - 5"""

#13

#here we uploaded a sample.txt
for i in range(1,4):
  print("shift No - ",i)
  report=input("enter today report (ongoing / finished ) :")
  while(True):
    if(report!="ongoing" and report!="finished"):
      report=input("Enter correct value...")
    else:
      break
  with open("/content/logs.txt","a") as file:
    file.write(report+"\n")
    file.close()

with open("/content/logs.txt","r") as file:
  print(file.read())
  file.close()

#14

with open("/content/logs.txt","r") as file:
  print(file.read())

#15

for i in range(1,4):
  print("day  - ",i)
  report=input("enter today performance (excellent / better ) :")
  while(True):
    if(report!="excellent" and report!="better"):
      report=input("Enter correct value...")
    else:
      break
  with open("/content/company_logs.txt","a") as file:
    file.write(report+"\n")
    file.close()

with open("/content/company_logs.txt","r") as file:
  print(file.read())
  file.close()