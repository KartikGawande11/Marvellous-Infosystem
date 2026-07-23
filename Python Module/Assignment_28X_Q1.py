#Assignment_28X_Q1.py

'''def main():
    try:
        count=0
        fobj=open("Demo.txt","r")
        print("file grt open")
        for line in fobj:
         count = count + 1
         print(count) 

        
         
    except FileNotFoundError as fobj:
        print("File is not found ")
    
if __name__=="__main__":
    main()'''
    
filename = input("Enter file name : ")

fobj = open(filename, "r")

count = 0

for line in fobj:
    count = count + 1

print("Total number of lines:", count)

fobj.close()