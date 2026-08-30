'''Machine Learning Assignment

Fraudulent Transaction Detection

Models:
1. Decision Tree
2. Bagging Classifier
3. Random Forest Classifier
4. AdaBoost Classifier
5. Voting Classifier

Evaluation:
Accuracy
Precision
Recall
F1 Score
Confusion Matrix
'''

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import (
    BaggingClassifier,
    RandomForestClassifier,
    AdaBoostClassifier,
    VotingClassifier
)

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)


def main():

    Border = "-" * 60

    ###########################################################################
    # Step 1: Load the Dataset
    ###########################################################################

    print(Border)
    print("Step 1: Load the Dataset")
    print(Border)

    df = pd.read_csv("Fraudulent_Transaction_Detection.csv")

    print(df)
    print("Dataset Shape:", df.shape)


    ###########################################################################
    # Step 2: Check for Missing Values
    ###########################################################################

    print("\n" + Border)
    print("Step 2: Check for Missing Values")
    print(Border)

    print(df.isnull().sum())


    ###########################################################################
    # Step 3: Separate Input and Output Variables
    ###########################################################################

    print("\n" + Border)
    print("Step 3: Separate Input and Output Variables")
    print(Border)

    X = df[
        [
            'TransactionAmount',
            'TransactionHour',
            'AccountAgeMonths',
            'PreviousTransactions',
            'LocationDifferenceKm',
            'DeviceType',
            'FailedLoginAttempts'
        ]
    ]

    Y = df['Fraud']

    # Convert DeviceType into numerical values
    X = pd.get_dummies(
        X,
        columns=['DeviceType'],
        drop_first=True
    )

    print("X Shape:", X.shape)
    print("Y Shape:", Y.shape)

    print("\nInput Variables:")
    print(X.head())

    print("\nOutput Variable:")
    print(Y.head())


    ###########################################################################
    # Step 4: Split the Dataset into Training and Testing Data
    ###########################################################################

    print("\n" + Border)
    print("Step 4: Split the Dataset")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42,
        stratify=Y
    )

    print("X_train shape:", X_train.shape)
    print("X_test shape :", X_test.shape)

    print("Y_train shape:", Y_train.shape)
    print("Y_test shape :", Y_test.shape)


    ###########################################################################
    # Step 5: Decision Tree
    ###########################################################################

    print("\n" + Border)
    print("Step 5: Decision Tree Classifier")
    print(Border)

    model = DecisionTreeClassifier(
        random_state=42
    )

    model.fit(X_train, Y_train)

    Y_pred_dt = model.predict(X_test)

    print("Decision Tree Creation Successful")


    ###########################################################################
    # Step 6: Bagging Classifier
    ###########################################################################

    print("\n" + Border)
    print("Step 6: Bagging Classifier")
    print(Border)

    model1 = BaggingClassifier(
        estimator=DecisionTreeClassifier(),
        n_estimators=10,
        random_state=42
    )

    model1.fit(X_train, Y_train)

    Y_pred_bagging = model1.predict(X_test)

    print("Bagging Classifier Creation Successful")


    ###########################################################################
    # Step 7: Random Forest Classifier
    ###########################################################################

    print("\n" + Border)
    print("Step 7: Random Forest Classifier")
    print(Border)

    model2 = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model2.fit(X_train, Y_train)

    Y_pred_rf = model2.predict(X_test)

    print("Random Forest Classifier Creation Successful")


    ###########################################################################
    # Step 8: AdaBoost Classifier
    ###########################################################################

    print("\n" + Border)
    print("Step 8: AdaBoost Classifier")
    print(Border)

    model3 = AdaBoostClassifier(
        n_estimators=100,
        random_state=42
    )

    model3.fit(X_train, Y_train)

    Y_pred_ada = model3.predict(X_test)

    print("AdaBoost Classifier Creation Successful")


    ###########################################################################
    # Step 9: Voting Classifier
    ###########################################################################

    print("\n" + Border)
    print("Step 9: Voting Classifier")
    print(Border)

    voting_model4 = VotingClassifier(
        estimators=[
            (
                'DecisionTree',
                DecisionTreeClassifier(
                    random_state=42
                )
            ),
            (
                'RandomForest',
                RandomForestClassifier(
                    n_estimators=100,
                    random_state=42
                )
            ),
            (
                'AdaBoost',
                AdaBoostClassifier(
                    n_estimators=100,
                    random_state=42
                )
            )
        ],

        voting='hard'
    )
    voting_model4.fit(X_train, Y_train)

    Y_pred_voting = voting_model4.predict(X_test)

    print("Voting Classifier Creation Successful")

    ###########################################################################
    # Step 10: Model Evaluation
    ###########################################################################

    print("\n" + Border)
    print("Step 10: Model Evaluation")
    print(Border)

    ###########################################################################
    # Decision Tree Evaluation
    ###########################################################################

    print("\nDecision Tree Classifier")
    print("------------------------")
    print("Accuracy :", accuracy_score(Y_test, Y_pred_dt))
    print("Precision:", precision_score(Y_test, Y_pred_dt, zero_division=0))
    print("Recall   :", recall_score(Y_test, Y_pred_dt, zero_division=0))
    print("F1 Score :", f1_score(Y_test, Y_pred_dt, zero_division=0))

    print("Confusion Matrix:")
    print(confusion_matrix(Y_test, Y_pred_dt))

    ###########################################################################
    # Bagging Evaluation
    ###########################################################################

    print("\nBagging Classifier")
    print("------------------")
    print("Accuracy :", accuracy_score(Y_test, Y_pred_bagging))
    print("Precision:", precision_score(Y_test, Y_pred_bagging, zero_division=0))
    print("Recall   :", recall_score(Y_test, Y_pred_bagging, zero_division=0))
    print("F1 Score :", f1_score(Y_test, Y_pred_bagging, zero_division=0))

    print("Confusion Matrix:")
    print(confusion_matrix(Y_test, Y_pred_bagging))

    ###########################################################################
    # Random Forest Evaluation
    ###########################################################################

    print("\nRandom Forest Classifier")
    print("------------------------")

    print("Accuracy :", accuracy_score(Y_test, Y_pred_rf))
    print("Precision:", precision_score(Y_test, Y_pred_rf, zero_division=0))
    print("Recall   :", recall_score(Y_test, Y_pred_rf, zero_division=0))
    print("F1 Score :", f1_score(Y_test, Y_pred_rf, zero_division=0))

    print("Confusion Matrix:")
    print(confusion_matrix(Y_test, Y_pred_rf))


    ###########################################################################
    # AdaBoost Evaluation
    ###########################################################################
    print("\nAdaBoost Classifier")
    print("-------------------")
    print("Accuracy :", accuracy_score(Y_test, Y_pred_ada))
    print("Precision:", precision_score(Y_test, Y_pred_ada, zero_division=0))
    print("Recall   :", recall_score(Y_test, Y_pred_ada, zero_division=0))
    print("F1 Score :", f1_score(Y_test, Y_pred_ada, zero_division=0))

    print("Confusion Matrix:")
    print(confusion_matrix(Y_test, Y_pred_ada))


    ###########################################################################
    # Voting Classifier Evaluation
    ###########################################################################
    print("\nVoting Classifier")
    print("-----------------")
    print("Accuracy :", accuracy_score(Y_test, Y_pred_voting))
    print("Precision:", precision_score(Y_test, Y_pred_voting, zero_division=0))
    print("Recall   :", recall_score(Y_test, Y_pred_voting, zero_division=0))
    print("F1 Score :", f1_score(Y_test, Y_pred_voting, zero_division=0))

    print("Confusion Matrix:")
    print(confusion_matrix(Y_test, Y_pred_voting))


    ###########################################################################
    # Step 11: Comparison
    ###########################################################################
    print("\n" + Border)
    print("Step 11: Model Comparison")
    print(Border)

    results = pd.DataFrame({
        'Model': [
            'Decision Tree',
            'Bagging',
            'Random Forest',
            'AdaBoost',
            'Voting Classifier'
        ],

        'Accuracy': [
            accuracy_score(Y_test, Y_pred_dt),
            accuracy_score(Y_test, Y_pred_bagging),
            accuracy_score(Y_test, Y_pred_rf),
            accuracy_score(Y_test, Y_pred_ada),
            accuracy_score(Y_test, Y_pred_voting)
        ],

        'Precision': [
            precision_score(Y_test, Y_pred_dt, zero_division=0),
            precision_score(Y_test, Y_pred_bagging, zero_division=0),
            precision_score(Y_test, Y_pred_rf, zero_division=0),
            precision_score(Y_test, Y_pred_ada, zero_division=0),
            precision_score(Y_test, Y_pred_voting, zero_division=0)
        ],

        'Recall': [
            recall_score(Y_test, Y_pred_dt, zero_division=0),
            recall_score(Y_test, Y_pred_bagging, zero_division=0),
            recall_score(Y_test, Y_pred_rf, zero_division=0),
            recall_score(Y_test, Y_pred_ada, zero_division=0),
            recall_score(Y_test, Y_pred_voting, zero_division=0)
        ],

        'F1 Score': [
            f1_score(Y_test, Y_pred_dt, zero_division=0),
            f1_score(Y_test, Y_pred_bagging, zero_division=0),
            f1_score(Y_test, Y_pred_rf, zero_division=0),
            f1_score(Y_test, Y_pred_ada, zero_division=0),
            f1_score(Y_test, Y_pred_voting, zero_division=0)
        ]
    })

    print(results)


    ###########################################################################
    # Step 12: Recommendation
    ###########################################################################

    best_model = results.loc[
        results['F1 Score'].idxmax(),
        'Model'
    ]

    print("\n" + Border)
    print("Recommendation")
    print(Border)

    print("Best Model based on F1 Score:", best_model)


if __name__ == "__main__":
    main()