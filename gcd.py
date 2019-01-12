x=8765
y=23485
q=1
r=1
while(r!=0):
	q=y/x;
	r=y%x;
	if(r!=0):
         y=x
		   print("Step is ",y,"=",x,"*",q,"+",r)
			x=r
	else:
         print("Step is ",y,"=",x,"*",q,"+",r)	
print("GCD is ", x)