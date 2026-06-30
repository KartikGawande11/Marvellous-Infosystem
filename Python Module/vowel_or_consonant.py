#Write a program which accepts one character and checks whether it is vowel or consonant.
def Display(ch):
    if ch in ("a","e","i","o","u","A","E","I","O","U"):
        print("Given character is vowel")
    else:
        print("Given character is consonant")    
    pass
def main():
    vocon=(input("Enter your character"))
    Display(vocon)
    
    if vocon==1 and vocon.isalpha:
        Display(vocon)
    else:
        print("Enter only one alphabets")    
    
if __name__=="__main__":
    main()