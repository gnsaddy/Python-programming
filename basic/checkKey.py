dict_d1 = { 
    'First_Name' : "Aditya",
    'Last_Name' : "Raj",
    'Age' : 20,
    'College' : "RVCE",
    'Course' : "MCA",
    'City' : 'Banglore'
}

def check_key(keys):
    if keys in dict_d1:
        print("Key found: ",keys)
    else:
        print("key not found\n")

check_key('First_Name')
check_key('Address')