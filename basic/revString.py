# reversing of string
str1 = input("enter first name \t")
str2 = input("enter second name \t")
name = str1+str2
print('-'*30)


# using extended slice syntax
print(" ".join(name[::-1]))
print('-'*30)


for i in reversed(name):
    print(i,end=" ")

print("\n",'-'*30)

# join reversed method
print(' '.join(reversed(name)))

print("\n",'-'*30)

def str_rev(fullName):
    rev_s = ''
    index = len(fullName)
    while index > 0:
        rev_s += fullName[ index -1]
        index = index -1
    print(' '.join(rev_s))
str_rev(name)


