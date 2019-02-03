# customer order and payment

class Customer:

    def getCustomerDetail(self):
        self.name = input("Enter customer name : ")
        self.address = input("Enter customer address : ")

    def show(self):
        print("Name : ",self.name)
        print("Address : ",self.address)

class Order(Customer):

    def items(self):
        self.pen = pen
        self.notebook = notebook
        self.book = book
        self.cover = cover

    def show(self):
        super().show()
        print("\n")
        print("=> Item             price")
        print("1- Pen              10")
        print("2- Notebook         20")
        print("3- Book             50")
        print("4- Cover            30")
        print("\n")


class Payment(Order):
    
    def getItem(self):
        self.total = 0
        while(True):
            print("Item details \n\n")
            print("1- Pen \n2- Notebook \n3- Book \n4- Cover \n")
            ch = int(input("Enter details "))
            sum = []

            if ch == 1:
                sum.append(10)
            elif ch == 2:
                sum.append(20)
            elif ch == 3:
                sum.append(50)
            elif ch ==4:
                sum.append(30)
            elif ch >4:
                print("Thank you for shoping ")
                exit()

            for ele in range(0, len(sum)):
                self.total = self.total + sum[ele]

            print("Total cost for items is : ", self.total)
        

            
        



obj = Payment()

obj.getCustomerDetail()
obj.show()
obj.getItem()
        
        
