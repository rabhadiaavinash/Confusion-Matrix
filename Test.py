

# This code writes the DataFrame.csv file with True Values and predicted values
# uses Final_results.csv with True and predicted values
# DataFrame.csv contains the true values from [$ 0 1 2 3 4 ________A B C _______Z ] and corresponding predicted values.

import pandas as pd

char_alphabets = ['$', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B',
                  'E', 'K', 'M', 'H', 'O', 'P', 'C', 'T', 'Y', 'X']

DataFrame = pd.read_csv("Final_result.csv")

true_values = DataFrame['True_values']
predicted_values = DataFrame['Predicted_values']

# Converting Pandas Series into List
true_values = list(true_values)
predicted_values = list(predicted_values)

print("true_values",true_values)
print("predicted_values",predicted_values)

print("true_values",len(true_values))
print("predicted_values",len(predicted_values))

Final_true_values = []
Final_Predicted_values = []

DataFrame_New = pd.DataFrame(columns=["True","Predicted"])
DataFrame_New_index = 0
for char in char_alphabets:
    # print('char:',char)
    for i in range(len(true_values)):
        # print(true_values[i])
        if true_values[i] == char and predicted_values[i] != ' ':
            Final_true_values.append(true_values[i])
            Final_Predicted_values.append(predicted_values[i])
            DataFrame_New.loc[DataFrame_New_index] = [true_values[i],predicted_values[i]]
            DataFrame_New_index += 1

print(Final_true_values)
print(Final_Predicted_values)

print(len(Final_true_values))
print(len(Final_Predicted_values))

print(DataFrame_New)

# Write DataFrame into csv file
DataFrame_New.to_csv("DataFrame_New4.csv",index=False)