lang = input("length of list\n")
list = []
for i in range (0 , int(lang)):
	list.append(int(input("element "+str(i)+"\n")))
sum = 0
t = []
max = list[0]
min = list[0]
for i in range (int(lang)):
	if list[i] > max:
		max = list[i]
	if list[i] < min:
		min = list[i]
	sum = sum + list[i]
	med = sum / int(lang)

for  i in range (int(lang)-1,-1 ,-1):
	t.append(list[i])
	
	
print (t)
input("")