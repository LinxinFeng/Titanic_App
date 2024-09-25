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
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
plt.style.use('seaborn-v0_8')

# Subplot 1: Ticket prices for 1st class
axes[0].boxplot(df[df['Pclass'] == 1]['Fare'])
axes[0].set_title('Ticket Price (1st Class)')
axes[0].set_xlabel('PClass=1')
axes[0].set_xticks([1])
axes[0].set_xticklabels(['Fare'])
axes[0].set_ylabel('Ticket Price ($)')

# Subplot 2: Ticket prices for 2nd class
axes[1].boxplot(df[df['Pclass'] == 2]['Fare'])
axes[1].set_title('Ticket Price (2nd Class)')
axes[1].set_xlabel('PClass=2')
axes[1].set_xticks([1])
axes[1].set_xticklabels(['Fare'])
axes[1].set_ylabel('Ticket Price ($)')

# Subplot 3: Ticket prices for 3rd class
axes[2].boxplot(df[df['Pclass'] == 3]['Fare'])
axes[2].set_title('Ticket Price (3rd Class)')
axes[2].set_xlabel('PClass=3')
axes[2].set_xticks([1])
axes[2].set_xticklabels(['Fare'])
axes[2].set_ylabel('Ticket Price ($)')

# Adjust layout
plt.tight_layout()

# Display the plot in Streamlit app
st.pyplot(fig)


