f=open('student.txt','r')
n=int(input("enter the number of lines"))
for i in range(n):
      data=f.readline()
      print(data)
f.close()
