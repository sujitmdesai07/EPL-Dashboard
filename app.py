import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("dataset - 2020-09-24.csv")

st.title("⚽ Football Player Dashboard")

# Sidebar filters
st.sidebar.header("Filter Data")

club = st.sidebar.selectbox("Select Club", df["Club"].dropna().unique())
position = st.sidebar.selectbox("Select Position", df["Position"].dropna().unique())

filtered_df = df[(df["Club"] == club) & (df["Position"] == position)]

# Show data
st.subheader("Filtered Player Data")
st.dataframe(filtered_df)

# KPIs
st.subheader("Key Statistics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Players", len(filtered_df))
col2.metric("Total Goals", int(filtered_df["Goals"].sum()))
col3.metric("Total Assists", int(filtered_df["Assists"].sum()))

# Top Players by Goals
st.subheader("Top Players by Goals")

top_players = filtered_df.sort_values(by="Goals", ascending=False).head(10)

fig, ax = plt.subplots()
ax.barh(top_players["Name"], top_players["Goals"])
ax.set_xlabel("Goals")
ax.set_ylabel("Player")
ax.invert_yaxis()

st.pyplot(fig)

# Age Distribution
st.subheader("Age Distribution")

fig2, ax2 = plt.subplots()
ax2.hist(filtered_df["Age"].dropna(), bins=10)
ax2.set_xlabel("Age")
ax2.set_ylabel("Count")

st.pyplot(fig2)

# Passes vs Assists
st.subheader("Passes vs Assists")

fig3, ax3 = plt.subplots()
ax3.scatter(filtered_df["Passes"], filtered_df["Assists"])
ax3.set_xlabel("Passes")
ax3.set_ylabel("Assists")

st.pyplot(fig3)
