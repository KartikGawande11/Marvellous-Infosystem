def main():
    
    ret=input("Enter your file name:-")
    
    ret1=input("Enter your worde for count :-")
    
    fobj=open(ret,"r")
    
    data = fobj.read()
    
    count = data.count(ret1)

    print("Count = ",count)
    
    

if __name__=="__main__":
    main()