import os

print(os.getcwd())  # get current working directory
# change directory where ypu want to save file
os.chdir('E:\\MyWorkPlace\\Python-programming\\File-operations')
print(os.listdir())

f = open('newText.txt','w')  #creating new file
f.write('This is new file.')
f.close()

with open('newText.txt','a') as f:
    f.write("Hi new line is there!!")

print(f.closed)  # return file is closed or not

f = open('newText.txt','r')
print(f.read())
f.close()
print(f.closed)  # return file is closed or not  


# file = open('test.txt','r')  #reding from file
# print(file.read())
# file.close()

with open('test.txt','r') as file:
    file_content = file.readline() # line by line data
    print(file_content)

print(file.closed) #return file is closed or not

with open('test.txt', 'r') as file:
    file_content = file.read()  # read whole data
    print(file_content)






