''' 
Author : Abraar Ibrahim 
IG : @retard.sonn

Developed with basic Python knowledge :)
& This is my first official Python program

'''
 
###### Modules ######
from colorama import Fore
from art import *
####################

tprint("PyCal - v0.1")
print(Fore.RED + "         Developed by Abraar | @retard.sonn \n\n")

a = int(input(Fore.GREEN + "Enter the first no. : "))
  
b = int(input(Fore.GREEN + "\nEnter the second no. : "))


print(Fore.WHITE + " \n\n 1.",Fore.RED + "+",Fore.GREEN + "(Addition)\n",Fore.WHITE + "2.",Fore.RED + "-",Fore.GREEN + "(Subtraction)\n",Fore.WHITE + "3.",Fore.RED + "*",Fore.GREEN + "(Multiplication)\n",Fore.WHITE + "4.",Fore.RED + "/",Fore.GREEN + "(Division)\n")

print(Fore.RED + "\n\n          [TIP]")
op = input(Fore.BLUE + " Select the operator above : ")




######## Defines ##########
def add():
  print("\n", a, "+", b, "=", a+b)
def sub():
  print("\n", a, "-", b, "=", a-b)
def mul():
  print("\n", a, "x", b, "=", a*b)
def div():
  print("\n", a, "/", b, "=", a/b)
###########################



if op == "1":
  add()

elif op == "2":
  sub()

elif op == "3":
  mul()

elif op == "4":
  div()

else:
  print(Fore.RED + "[ERROR]", Fore.WHITE + "Select correct operator!")
  for i in range(1):
  	
  	op = input(Fore.BLUE + "\n Select the operator above : ")
  	if op == "1":
  		add()
  		
  	if op == "2":
  		sub()
  	
  	if op == "3":
  		mul()
  	
  	if op == "4":
  		div()