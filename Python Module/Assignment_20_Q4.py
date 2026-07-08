"""Design a Python application that creates three threads named Small, Capital, and Digits.

All threads should accept a string as input.

The Small thread should count and display the number of lowercase characters.

The Capital thread should count and display the number of uppercase characters.

The Digits thread should count and display the number of numeric digits.

Each thread must also display:

Thread ID

Thread Name"""""
import threading
def Small(str):
    s=0
    for chr in str:
        if 'a'<= chr <= 'z':
            s+=1
    print(" lowercase characters.",s)       
    
    
def capital(str):
    c=0
    for chr in str:
        if 'A'<= chr <='Z':
            c+=1
    print("uppercase characters:-",c)
            
    

def digits(str):
    d=0
    for chr in str:
        if '0'<= chr <='9':
            d+=1
    print("numeric digits.",d)


def main():
    chr=input("Enter your Data:-")
    small=threading.Thread(target=Small,args=(chr,))
    Capita=threading.Thread(target=capital,args=(chr,))
    Digites=threading.Thread(target=digits,args=(chr,))
    
    
    small.start()
    Capita.start()
    Digites.start()
    
    small.join()
    Capita.join()
    Digites.join()
    
if __name__=="__main__":
    main()