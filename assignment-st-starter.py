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

# Create a bar plot for survival rates by ticket class
st.subheader('Survival Rate by Ticket Class')

# Plot the survival rate
fig, ax = plt.subplots()
ax.bar(survival_rate_by_class.index, survival_rate_by_class.values)
ax.set_title('Survival Rate by Ticket Class', fontsize=14)
ax.set_xlabel('Ticket Class', fontsize=12)
ax.set_ylabel('Survival Rate (%)', fontsize=12)

# Display the plot in the Streamlit app
st.pyplot(fig)

# Displaying descriptive statistics for the Titanic dataset
st.subheader('Descriptive Statistics')
st.write(df.describe())
