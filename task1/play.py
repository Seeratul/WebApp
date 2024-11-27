import streamlit as st
import time
import numpy as np
import random as rand

# title and desc
st.title("Wanna play a game?")
st.write("Guess the Number between 1 and 100")

#st.sidebar.success("Select a demo above.")

# init random number
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = rand.randint(1, 100)

# hint
st.write("Pssst the Number is ")
st.write(st.session_state.secret_number)

# UI prompt
user_guess = st.number_input("Pick a number between 1 and 100")

# UI interaction
if st.button("Guess"):

    # pos feedback 
    if user_guess == st.session_state.secret_number:
        st.write("Well done :)")
        st.balloons()

    # neg feedback
    else:
        st.write("Wrong number :(")

