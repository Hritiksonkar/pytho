x=10
y=20
temp=x
x=y
y=temp  
print(y,x)
 
# without using third variable
x=10
y=20    
x,y=y,x
print(x,y)   