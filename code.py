myfile=open('txt1.txt','r')
str=[myfile.read()]
myfile2=open('txt2.txt','r')
str2=[myfile2.read()]
myfile.clear()
myfile2.clear()
print(str)
print(str2)

def swap(x,y):
    x=open('txt1','w')
    global str
    global str2
    x.write(str2)    
    y=open('txt2','w')
    y.write(str)

swap()




