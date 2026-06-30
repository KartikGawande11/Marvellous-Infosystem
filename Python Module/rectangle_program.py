#Write a program which accepts length and width of rectangle and prints area.
def rectangle(length,width):
    area=length*width
    print("area of ractangle",area)
    
def main():
    length=int(input("Enter your length"))
    width=int(input("Enter your width"))
    rectangle(length,width)
if __name__=="__main__":
    main()