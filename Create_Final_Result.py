
# This code takes Book1.csv as an input
# This code writes Final_result.csv
# Book1.csv must contain the true values and predicted values of the license plate detections


# Flow of Evaluating TROCR Character Detection
# ------------------------------------------------------------------------------------------------
# run Create_Final_Result.py  to get Final_Result.csv
# run Test.py  to get DataFrame_New.csv
# run Confusion_matrix_display.py to display and save Confusion Matrix and Classification Report

# -------------------------------------------------------------------------------------------------
import pandas as pd
import numpy as np

# Book1.csv contains true & predicted values of Number Plate characters
DataFrame = pd.read_csv("Book1.csv")
print(DataFrame)
print(DataFrame.columns)


true_values = DataFrame['TRUE']
predicted_values = DataFrame['Predicted']

true_values = list(true_values) # True values of Number plate
predicted_values = list(predicted_values) # Predicted values of Number plate

# Create Final DataFrame where True & Predicted values will be saved
Final_DataFrame = pd.DataFrame(columns=["True_values","Predicted_values"])

Final_DataFrame_index = 0 # DataFrame row index, used to enter corresponding data wrt Columns


# this for loop will compare true values with predicted values and will do respective operations

for i in range(len(true_values)):
    print(true_values[i])
    temp_true = [*true_values[i]]
    temp_predicted = [*predicted_values[i]]
    if len(temp_true) == len(temp_predicted):
        for j in range(len(temp_true)):
            # Enter row in Final_DataFrame
            Final_DataFrame.loc[Final_DataFrame_index] = [temp_true[j],temp_predicted[j]]
            Final_DataFrame_index += 1
    elif len(temp_true) != len(temp_predicted):
        temp_true_length = len(temp_true)
        temp_predicted_length = len(temp_predicted)
        if temp_true_length > temp_predicted_length:
            for m in range(len(temp_true)):
                diff1 = temp_true_length-temp_predicted_length
                # fill the difference with '$' in temp_predicted
                for hh in range(diff1):
                    temp_predicted.append('$')
                # Enter row in Final_DataFrame
                Final_DataFrame.loc[Final_DataFrame_index] = [temp_true[m],temp_predicted[m]]
                Final_DataFrame_index += 1

        if temp_true_length < temp_predicted_length:
            for b in range(len(temp_predicted)):
                diff2 = temp_predicted_length - temp_true_length
                # fill the difference with '$' in temp_true
                for hh in range(diff2):
                    temp_true.append('$')
                # Enter row in Final_DataFrame
                Final_DataFrame.loc[Final_DataFrame_index] = [temp_true[b],temp_predicted[b]]
                Final_DataFrame_index += 1



print(Final_DataFrame)
# Save Final_DataFrame to csv
Final_DataFrame.to_csv("Final_result.csv",index=False)