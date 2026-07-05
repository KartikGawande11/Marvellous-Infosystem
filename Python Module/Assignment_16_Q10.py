#Write a program which accept name from user and display length of its name.
def namelength(name):
    return len(name)
    
def main():
    name=input("Enter your string")
    length=namelength(name)
    print("length of name",length)
    
    

if __name__=="__main__":
    main()