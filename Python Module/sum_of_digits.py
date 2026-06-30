#Write a program which accepts one number and prints sum of digits
def counts(no):
    sum = 0

    while no > 0:
        digit = no % 10
        sum = sum + digit
        no = no // 10

    print(sum)

def main():
    num = int(input("Enter your number: "))
    counts(num)

if __name__ == "__main__":
    main()