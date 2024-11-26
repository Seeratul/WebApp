import streamlit as st
import random as rand

st.title("Guess the Number between 1 and 100")

st.write("Guess the Number between 1 and 100")

secret_number = rand.choice(range(101))

st.write("Pssst the Number is ")
st.write(secret_number)
user_guess = st.number_input("Pick a number between 1 and 100")

if st.button("Guess?"):
    if user_guess == secret_number:
        print("Congrats you did it!")
else:
    st.write("Shuttingdown")