class Demo:
     # Class variable
    value=100
    
    
     # Constructor
    def __init__(self,no1,no2):
        self.no1=no1
        self.no2=no2
        
    #instance methods:
    def fun(self):
        print("Inside instance  Fun methods:")
        print("No1",self.no1)
        print("no2",self.no2)
    # Instance method    
    def gun(self):
        print("inside instance gun  methods:")
        print("no1",self.no1)
        print("no2",self.no2)
        
 # Creating objects
obj1=Demo(11,21)
obj2=Demo(51,101)
    
 # Calling methods
obj1.fun()
obj2.fun()

 # Calling methods  
obj1.gun()
obj2.gun()
    

   

    