class India():
    def capital(self):
        print("New Delhi is the capital of India.")
        
    def language(self):
        print("Hindi the primary language of India.")
        print("*"*60)

   
class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")
       
    def language(self):
        print("English is the primary language of USA.")
        print("*"*60)

    
obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
