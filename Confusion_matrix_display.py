
# This code is to display the Confusion Matrix with the help of the Dataframe


import pandas as pd
from sklearn.metrics import confusion_matrix,accuracy_score,ConfusionMatrixDisplay,plot_confusion_matrix,classification_report
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
# Read DataFrame
DataFrame = pd.read_csv("DataFrame_New4.csv")
print(DataFrame.columns)

# Calculate Confusion matrix
confusion_matrix1 = confusion_matrix(DataFrame["True"],DataFrame["Predicted"])
print("confusion_matrix1:",confusion_matrix1)


# Calculate Accuracy
accuracy = accuracy_score(DataFrame["True"],DataFrame["Predicted"])
accuracy = accuracy * 100
accuracy = round(accuracy,2)
print("Accuracy: {} %".format(accuracy))

x_labels = ['$','0','1','2','3','4','5','6','7','8','9','А','В','Е','К','М','Н','О','Р','С','Т','У','Х']


y_labels = ['$','0','1','2','3','4','5','6','7','8','9','А','В','Е','К','М','Н','О','Р','С','Т','У','Х']


print("----------------------------------------------------------------------------------------------")
# Display Confusion Matrix
plt.figure(figsize=(100,100))
fx=sns.heatmap(confusion_matrix1,annot= True,fmt=" ",cmap="GnBu")

fx.set_title(f'Confusion Matrix with Accuracy: {accuracy} % \n')
fx.set_xlabel('\n Predicted Values\n')
fx.set_ylabel('Actual Values\n')
fx.xaxis.set_ticklabels([])
fx.yaxis.set_ticklabels([])
fx.xaxis.set_ticklabels(x_labels)
fx.yaxis.set_ticklabels(y_labels)
plt.show()

print("Classification Report")

print("-----------------------------------------------------------------------------------------------")

report = classification_report(DataFrame["True"],DataFrame["Predicted"])

print(classification_report(DataFrame["True"],DataFrame["Predicted"]))
