import random
num = random.randint(1,20)
i = int(input("input number\n"))
while i>0:
	if i==num:
		print("perfect, congratulation this is the number")
		break
	elif i>num:
		print("no, number is lower, input again",end="\n")
	else:
		print("no, number is higher, input again",end="\n")
	i = int(input(""))
		
if (i <0):
	print("you lose, sol:",num,sep=" ")
input("")