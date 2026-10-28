import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello, Streamlit !")
st.write(":streamlit: This is your first streamlit app" )
st.text("Lets get started")

#conditional logic with widgets

name = st.text_input("Enter your name:")
if st.button("Great"):
    st.success(f"Hello, {name}!")

#Displaying data and charts
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 2), columns=['A', 'B'])

print(df)
st.line_chart(df)
st.bar_chart(df)

#Flie uploading and caching

upload_file = st.file_uploader("upload a csv", type='cv')
if upload_file:
    df = pd.read_csv(upload_file)
    st.dataframe(df)

st.title("Text and Markdown Demo")
st.header("This ia a header")
st.subheader("This is a subheader")
st.markdown("**Bold**, *Itallic*, `code`, [Link](https:streamlit.io)")
st.code("for i in range(5): print(i)", language="python")

st.text_input("What's your name?")
st.text_area("Write something...")
st.number_input("Pick a number", min_value=0, max_value=100)
st.slider("Choose a range", 0, 100)
st.selectbox("Select a fruit", ["Apple", "Banana", "Mango"])
st.multiselect("Choose toppings", ["Cheese", "Tomato", "Onion"])
st.radio("Pick one", ["Option A", "Option B"])
st.checkbox("I agree to the terms")

if st.checkbox("Show Details"):
    st.info("Here are more details...")

option = st.radio("Choose view", ["Show Chart", "Show Table"])
if option == "Show Chart":
    st.write("Chart would appear here")
else:
    st.write("Table would appear here")

with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Login")

    if submitted:
        st.success(f"Welcome, {username}!")

st.image("https://via.placeholder.com/300", caption="Sample Image", use_column_width=True)
st.video("https://www.youtube.com/watch?v=VqgUkExPvLY")