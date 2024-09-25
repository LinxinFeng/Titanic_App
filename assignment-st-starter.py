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





st.subheader('Titanic Ticket Price Box Plot by Class')
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




st.subheader('Line Chart of Ticket Prices (Sorted in Descending Order)')
# Sort the ticket prices in descending order
sorted_fares = df['Fare'].sort_values(ascending=False).reset_index(drop=True)

# Create a figure for the line chart
fig, ax = plt.subplots(figsize=(10, 6))
plt.style.use('seaborn-v0_8')

# Plot the sorted fares
ax.plot(sorted_fares, linewidth=2)

# Set the chart title and labels
ax.set_title('Ticket Prices Sorted in Descending Order', fontsize=14)
ax.set_xlabel('Passengers (sorted by ticket price)', fontsize=12)
ax.set_ylabel('Ticket Price ($)', fontsize=12)
ax.grid(True)

# Display the plot in the Streamlit app
st.pyplot(fig)




st.subheader('Distribution of Embarked Ports')
# Create a figure for the histogram
fig, ax = plt.subplots(figsize=(8, 6))
plt.style.use('seaborn-v0_8')

# Plot the histogram for the 'Embarked' column
df['Embarked'].hist(ax=ax)

# Set the chart title and labels
ax.set_title('Distribution of Embarked Ports')
ax.set_xlabel('Embarked Port')
ax.set_ylabel('Number of Passengers')

# Display the plot in the Streamlit app
st.pyplot(fig)


st.subheader('different survival rate by different ticket class')
survival_rate_by_class = df.groupby('Pclass')['Survived'].value_counts(normalize=True) 

fig, ax = plt.subplots()  
survival_rate_by_class.plot.bar() 
plt.title('Survival Rate by Class')  
plt.xlabel('Passenger Class')  
plt.ylabel('Survival Rate')  
plt.xticks(rotation=0)  
 
st.pyplot(fig)  