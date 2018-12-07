leng= int(input("input length\n"))
list =[]
for i in range(0,leng):
	list.append(int(input("input element "+str(i)+"\n")))
print(list)
for i in range(0,leng-1):
	for j in range(i+1,leng):
		if list[i] < list[j] :
			t=list[i]
			list[i]=list[j]
			list[j]=t
print(list)
	
input("")
