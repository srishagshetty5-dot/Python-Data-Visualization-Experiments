# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""#write a program to implement matplotlib and pandas library in python
import pandas as pd 
import matplotlib.pyplot as plt

#create student dataset
data={
      "name":["arun","bala","charan","divya","esha","farhan","gita","hair"],
      "marks":[85,72,90,65,78,88,95,70],
      "attendance":[90,85,95,75,80,92,98,78]
      }
#create Dataframe
df=pd.DataFrame(data)
print("student dataset:")
print(df)

#barchart
plt.figure()
plt.bar(df["name"],df["marks"])
plt.xlabel("student name")
plt.ylabel("marks")
plt.title("student marks-bar chart")
plt.show()

#line chart-student marks
plt.figure()
plt.plot(df["name"],df["marks"],marker="o")
plt.xlabel("student name")
plt.ylabel("marks")
plt.title("student marks-line chart")
plt.show()

#3.pie chart
plt.figure()
plt.pie(df["marks"],labels=df["name"],autopct="%1.1f%%")
plt.title("student marks-pie chart")
plt.show()

# scatter plot
plt.figure()
plt.scatter(df["attendance"],df["marks"])
plt.xlabel("attendance")
plt.ylabel("marks")
plt.title("attendance vs marks-scatter plot")
plt.show()

#histogram-distribution of marks
plt.figure()
plt.hist(df["marks"],bins=5)
plt.xlabel("marks")
plt.ylabel("number of student")
plt.title("student marks-histogran")
plt.show()