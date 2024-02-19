class Class1: 
    def m(self): 
        print("En Class1") 
  
class Class2(Class1): 
    def m(self): 
        print("En Class2") 
        super().m() 
  
class Class3(Class1): 
    def m(self): 
        print("En Class3") 
        super().m() 
  
class Class4(Class2, Class3): 
    def m(self): 
        print("En Class4")    
        super().m() 

if __name__=='__main__':      
    obj = Class4() 
    obj.m() 
    print(Class4.mro())