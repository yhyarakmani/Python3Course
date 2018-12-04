s1,s2,i1,f1 = "yyy","rrr",5,0.5
vars = [s1 ,s2,i1,f1]
print ("the type of list (vars) is: " +str(type(vars))+"\n" +"type of the first element is:"+str(type(vars[0]))+"\n" +"type of the second element is:"+str(type(vars[1]))+"\n" +"type of the third element is:"+str(type(vars[2]))+"\n" +"type of the fourth element is:"+str(type(vars[3])) )
print("the first element is: " +vars[0] +"\nthe last element is: " +str(vars[-1]) )
vars[-1] = 4.3
print (vars[-1])
input("press enter to exit")