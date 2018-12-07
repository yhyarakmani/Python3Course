NumOfStd = int(input("please input the number of students\n"))
std_list =[]
for i in range (0,NumOfStd):
	std_list.append([input("input student "+str(i)+" name\n") ,int(input("input his/her mark\n"))])
i = 0

while i<NumOfStd:
	evaluate ="F"
	if std_list[i][1] >95:
		evaluate ='A+'
	elif (std_list[i][1] <=95 & std_list[i][1] >90):
		evaluate="A"
	elif (std_list[i][1] <=90 & std_list[i][1] >85):
		evaluate="A-"
	elif (std_list[i][1] <=85 & std_list[i][1] >80):
		evaluate="B+"
	elif (std_list[i][1] <=80 & std_list[i][1] >75):
		evaluate="B"
	elif (std_list[i][1] <=75 & std_list[i][1] >70):
		evaluate="B-"
	elif (std_list[i][1] <=70 & std_list[i][1] >65):
		evaluate="D"
	elif (std_list[i][1] <=65 & std_list[i][1] >60):
		evaluate="D-"
	elif std_list[i][1] <=60:
		evaluate="F"
	print(std_list[i][0],std_list[i][1],evaluate,sep=' ',end='\n')
	i = i+1
input("press enter to exit")