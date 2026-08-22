"""Machine Learning Assignment
1. Write a Python program that classifies a new data point using the K-Nearest Neighbors algorithm. 
The algorithm should be implemented manually without using any machine learning library.
The program should:
Calculate Euclidean distance
Sort distances
Select K nearest neighbors
Predict the class based on majority voting
Dataset

Point
XY
Label

A
1 2 Red
B
2 3 Red
c
31 Blue
D
6 5 Blue
Tasks

1. Accept X and Y coordinates of a new point from the user.
2. Compute Euclidean distance from all dataset points.
3. Sort the distances.
4. Select K 3 nearest neighbors.
5. Predict the class label.

Input Format
Enter X coordinate: 2
Enter Y coordinate: 2
Expected Output
Nearest Neighbors:
A Distance: 1.0
B Distance: 1.0
C Distance: 1.41
Predicted Class: Red"""
import math
import numpy as np

def Novamind_Ai_EucDistance(P1,P2):
    Ans = math.sqrt((P1['X'] - P2['X'])**2 + (P1['Y'] - P2['Y'])**2)
    return Ans

def NovaMind_AI_KNN_classifier():
    Border="-"*30
    Data = [
        {'point' : 'A', 'X' : 1, 'Y' : 2, 'label' : 'Red'},
        {'point' : 'B', 'X' : 2, 'Y' : 3, 'label' : 'Red'},
        {'point' : 'C', 'X' : 3, 'Y' : 1, 'label' : 'Blue'},
        {'point' : 'D', 'X' : 6, 'Y' : 5, 'label' : 'Blue'}
    ]
    print(Border)
    print("NovaMind_AI")
    print(Border)
    
    for i in Data:
        print(i)
    
    print(Border)
    new_Point={'X':3,'Y':3}
    
    print("Distances of all points:")
    print(Border)
    for d in Data:
        d['distance']=Novamind_Ai_EucDistance(d,new_Point)
    for d in Data:
        print(d['distance'],d['label'])
    print(Border)
    sorted_Data=sorted(Data,key=lambda item:item['distance'])
    print(Border)
    print("sorted_Data")
    print(Border)
    
    for d in sorted_Data:
        print(d)
    print(Border)
    k=3
    nearest=sorted_Data[:k]
    print(Border)
    print("nearest 3 members are:")
    print(Border)
#Voting 
    votes={}
    for neighbours in nearest:
        label=neighbours['label']
        votes[label]=votes.get(label,0)+1
    print(Border)
    print("Voting Result is:")
    print(Border)
    
    for d in votes:
        print("name:",d,"Number of votes:",votes[d])
    print(Border)
    
    imax=0
    Name=""
    for d in votes:
        if(votes[d]>imax):
            imax=votes[d]
            Name=d
    print("Final Prediction is :",Name)
        
        
  
    
def main():
    NovaMind_AI_KNN_classifier()
if __name__=="__main__":
    main()