#Write a program which accepts radius of circle and prints area of circle.
def Display(radius):
    area=(3.14*radius*radius)
    print("rea of circle",area)
    pass
def main():
    radius=int(input("Enter your radius"))
    Display(radius)
    
    pass
if __name__=="__main__":
    main()