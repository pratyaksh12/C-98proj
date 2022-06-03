def swap():
    myfile=input('enter name of the file')
    myfile2=input('enter name of file 2')

    with open(myfile,'r') as a:
        data_a=a.read()
    with open(myfile2,'r') as b:
        data_b=b.read()
    with open(myfile,'w') as a:
        a.write(data_b)
    with open(myfile2,'w') as b:
        b.write(data_a)
swap()
        
