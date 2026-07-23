'''Problem Statement:

Write a program which accepts a file name and a word from the user and checks whether that word is present in the file or not

Input:

Demo.txt Marvellous

Expected Output:

Display whether the word Marvellous is found in Demo.txt or not'''

def main():
    Filename=input("Enter your file")
    word=input("Enter your word ")
    try:
        
        fobj=open(Filename,"r")
        Data=fobj.read()
        
        if word in Data:
            print("Worde is present in the file...")
            
        else:
            print("worde is not present in the fail...")
            
        
        
        
    except FileNotFoundError as fobj:
        print("File is not found:")
    
    
if __name__=="__main__":
    main()