##7. Write a lambda function using filter() which accepts a list of strings and returns a list of strings having length greater than 5.
String=lambda str:len(str)>5
    
def main():
    Data=["kartik","ram","om","Rutu","prem","som","tom"]
    print("Given Data of list",Data)
    FData=list(filter(String,Data))
    print("strings having length greater than 5.",FData)
    
if __name__=="__main__":
    main()
    