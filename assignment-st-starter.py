# import packages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# show the title
st.title('Titanic App by Linxin Feng')

# read csv and show the dataframe
df = pd.read_csv('train.csv')


# create a figure with three subplots, size should be (15, 5)
# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
# a sample diagram is shown below

st.subheader('Titanic Dataset')
st.dataframe(df)  # Display the DataFrame in a scrollable table

# Group the data by ticket class and calculate the survival rate for each class
survival_rate_by_class = df.groupby('Pclass')['Survived'].mean() * 100

# Creating a figure with three subplots for box plots of ticket prices across different classes
plt.figure(figsize=(15, 5))
plt.style.use('seaborn-v0_8')

# Subplot 1: Ticket prices for 1st class
plt.subplot(1, 3, 1)
plt.boxplot(df[df['Pclass'] == 1]['Fare'])
plt.title('Ticket Price (1st Class)')
plt.xlabel('PClass=1')
plt.xticks([1], ['Fare'])
plt.ylabel('Ticket Price ($)')

# Subplot 2: Ticket prices for 2nd class
plt.subplot(1, 3, 2)
plt.boxplot(df[df['Pclass'] == 2]['Fare'])
plt.title('Ticket Price (2nd Class)')
plt.xlabel('PClass=2')
plt.xticks([1], ['Fare'])
plt.ylabel('Ticket Price ($)')

# Subplot 3: Ticket prices for 3rd class
plt.subplot(1, 3, 3)
plt.boxplot(df[df['Pclass'] == 3]['Fare'])
plt.title('Ticket Price (3rd Class)')
plt.xlabel('PClass=3')
plt.xticks([1], ['Fare'])
plt.ylabel('Ticket Price ($)')

# Display the figure
plt.tight_layout()
plt.show()

