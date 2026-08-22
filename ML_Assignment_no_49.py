import pandas as pd
import numpy as np
import math

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import confusion_matrix


def main():

    # -------------------------------------------------
    # 1. Calculate Mean using NumPy
    # -------------------------------------------------

    Data = [6, 7, 8, 9, 10, 11, 12]

    mean = np.mean(Data)

    print("Mean of the dataset using NumPy:", mean)


    # -------------------------------------------------
    # 2. Calculate Variance and Standard Deviation
    # -------------------------------------------------

    variance = np.var(Data)

    print("Variance of the dataset:", variance)

    standard_deviation = np.std(Data)

    print("Standard deviation of the dataset:", standard_deviation)


    # -------------------------------------------------
    # 3. StandardScaler Feature Scaling
    # -------------------------------------------------

    Standard_Data = [
        [25, 20000],
        [30, 40000],
        [35, 80000]
    ]

    scaler = StandardScaler()

    Scaler_Data = scaler.fit_transform(Standard_Data)

    print("\nStandardScaler to perform feature scaling:")
    print(Scaler_Data)


    # -------------------------------------------------
    # 4. Euclidean Distance BEFORE Feature Scaling
    # -------------------------------------------------

    P1 = [10, 100]
    P2 = [20, 200]

    Distance_before = math.sqrt(
        (P2[0] - P1[0])**2 +
        (P2[1] - P1[1])**2
    )

    print("\nDistance before scaling:", Distance_before)


    # -------------------------------------------------
    # 5. Min-Max Feature Scaling
    # -------------------------------------------------

    data = np.array([P1, P2])

    minmax_scaler = MinMaxScaler()

    scaled_data = minmax_scaler.fit_transform(data)

    print("\nScaled Data:")
    print(scaled_data)


    # Scaled points
    P1_scaled = scaled_data[0]
    P2_scaled = scaled_data[1]


    # -------------------------------------------------
    # 6. Euclidean Distance AFTER Feature Scaling
    # -------------------------------------------------

    Distance_after = math.sqrt(
        (P2_scaled[0] - P1_scaled[0])**2 +
        (P2_scaled[1] - P1_scaled[1])**2
    )

    print("\nDistance after scaling:", Distance_after)

    # -------------------------------------------------
    # 8. TP,TN,FP,FN confusion_matrix
    # -------------------------------------------------
    actual = [1, 1, 1, 1, 0, 0, 0, 0]
    predicted = [1, 1, 0, 1, 0, 1, 0, 0]

    cm = confusion_matrix(actual, predicted)

    TN, FP, FN, TP = cm.ravel()

    print("True Positive (TP):", TP)
    print("True Negative (TN):", TN)
    print("False Positive (FP):", FP)
    print("False Negative (FN):", FN)

if __name__ == "__main__":
    main()