# -*- coding: utf-8 -*-
"""Species_Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1g2XRXTZarJ79hxx4_4n9Pe43jCngXNsp

# Initialized Variables/Libraries
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

wheat_seeds = np.genfromtxt("seeds_dataset.txt")
Y = wheat_seeds[:,-1]
X = wheat_seeds[:,0:-1]

df = pd.read_csv("seeds_dataset.txt", header=None,sep='\t')
df.columns = ["Area", "Perimeter", "Compactness", "Length", "Width", "Asymmetry coefficient", "Length kernel groove", "Species"]



area = df["Area"]
perimeter = df["Perimeter"]
compactness = df["Compactness"]
length = df["Length"]
width = df["Width"]
assym_coeff = df["Asymmetry coefficient"]
length_kernel_groove = df["Length kernel groove"]
species = df["Species"]

def s_plot():
    sns.swarmplot(data=df,split=True)
    plt.xlim(0,6)
    plt.show()
s_plot()

def dist_plot(*columns):
    for column in columns:
        sns.displot(column,color='turquoise')
        plt.show()
dist_plot(area,perimeter,compactness,length,width,assym_coeff,length_kernel_groove,species)

sns.pairplot(df,hue="Species")
plt.show()

def mean(area,perimeter,compactness,length,width,assym_coeff,length_kernel_groove):
    mean_vals = [np.mean(area), np.mean(perimeter),np.mean(compactness),np.mean(length),np.mean(width),np.mean(assym_coeff),np.mean(length_kernel_groove)]
    plt.figure(figsize=(15,5))
    xlabels = np.array(['Area','Perimeter','Compactness','Length','Width','Asymmetry Coefficient','Length of Kernel Groove'])
    ylabels = np.array(mean_vals)
    plt.figure(figsize=(15,5))
    plt.barh(xlabels,ylabels,color='black')
    plt.title("Mean of the Dataset")
    plt.show()
mean(area,perimeter,compactness,length,width,assym_coeff,length_kernel_groove)

def std(area,perimeter,compactness,length,width,assym_coeff,length_kernel_groove):
    std_vals = [np.std(area), np.std(perimeter),np.std(compactness),np.std(length),np.std(width),np.std(assym_coeff),np.std(length_kernel_groove)]
    plt.figure(figsize=(15,5))
    xlabels = np.array(['Area','Perimeter','Compactness','Length','Width','Asymmetry Coefficient','Length of Kernel Groove'])
    ylabels = np.array(std_vals)
    plt.bar(xlabels,ylabels,color='darkgrey')
    plt.title("Standard Deviation of the Dataset")
    plt.show()
std(area,perimeter,compactness,length,width,assym_coeff,length_kernel_groove)

def median(area,perimeter,compactness,length,width,assym_coeff,length_kernel_groove):
    med_vals = [np.median(area), np.median(perimeter),np.median(compactness),np.median(length),np.median(width),np.median(assym_coeff),np.median(length_kernel_groove)]
    plt.figure(figsize=(15,5))
    xlabels = np.array(['Area','Perimeter','Compactness','Length','Width','Asymmetry Coefficient','Length of Kernel Groove'])
    ylabels = np.array(med_vals)
    plt.figure(figsize=(15,5))
    plt.barh(xlabels,ylabels,color='lightslategray')
    plt.title("Median of the Dataset")
    plt.show()
median(area,perimeter,compactness,length,width,assym_coeff,length_kernel_groove)

def percentile(dataset,area,perimeter,compactness,length,width,assym_coeff,length_kernel_groove):
    plt.figure(figsize=(20,6))
    plt.boxplot([area,perimeter,compactness,length,width,assym_coeff,length_kernel_groove],labels=['Area','Perimeter','Compactness','Length','Width','Asymmetry Coefficient','Length of Kernel Groove'])
percentile(df,area,perimeter,compactness,length,width,assym_coeff,length_kernel_groove)

def variance(*columns):
    column_num = 1
    for column in columns:
        print(f"Column {column_num} Variance: {np.var(column)}")
        column_num+=1
variance(column_one,column_two,column_three,column_four,column_five,column_six,column_sev)

"""# K-Nearest Neighbors """

X_Train, X_Test, Y_Train, Y_Test = train_test_split(X,Y,test_size=0.2) #20% of the data will be used for testing and 80% is used for training

model = KNeighborsClassifier(n_neighbors=20,p=2,metric='euclidean')

model.fit(X_Train,Y_Train)
predictions = model.predict(X_Test)
accuracyScore = accuracy_score(Y_Test,predictions)
print(f"Accuracy Score = {accuracyScore}")

def knnAVS():
  neighbors_range = np.arange(1,51)
  accuracy_scores = []
  valid_scores = []
  training_scores = []
  X_T, X_Te, Y_T, Y_Te = train_test_split(X,Y,test_size=0.2) #20% of the data will be used for testing and 80% is used for training

  for num in neighbors_range:
    mod = KNeighborsClassifier(n_neighbors=num,p=2,metric='euclidean')
    mod.fit(X_T,Y_T)
    
    valid_pred = mod.predict(X_Te)
    valid_acc = accuracy_score(Y_Te, valid_pred)
    valid_scores.append(valid_acc)

    training_pred = mod.predict(X_T)
    training_acc = accuracy_score(Y_T, training_pred)
    training_scores.append(training_acc)

  plt.title("Accuracy and Validation Scores")
  plt.xlabel("Number of Neighbors")
  plt.ylabel("Accuracy Scores")
  plt.plot(neighbors_range,valid_scores,color='red',label="Valid Accuracy")
  plt.plot(training_scores, color='teal',label="Training Accuracy")
  plt.legend()
  plt.show()
knnAVS()

"""# Naive Bayes"""

model2 = GaussianNB()

model.fit(X_Train,Y_Train)
predictions = model.predict(X_Test)
accuracyScore = accuracy_score(Y_Test,predictions)
print(f"Accuracy Score = {accuracyScore}")