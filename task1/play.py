import streamlit as st
import time
import numpy as np
import random as rand
from streamlit import session_state as ss
from funcs import hinter

#Rebuilt site so it reruns on each button press.

#Innit and restart being defined
#Works as Innit
if "restart" not in ss:
    ss.restart = True
    ss.guesses = 0
    ss.games = -1
    ss.gwon = 0
    ss.glost = 0
    ss.effectiveness = [0]
    
#Restarts the game if needed
if ss.restart:
    ss.secret_number = rand.randint(1, 100)
    ss.games += 1
    ss.guesses = 0
    ss.min = 0
    ss.max = 0
    ss.restart = False



# title and desc adaptive to wheter its the first game
if ss.games == 0:
    st.title("Wanna play a game?")
else:
    st.title("Wanna play another game?")



# init speaker
introMessage = st.chat_message("assistant")
introMessage.write("Guess the Number between 1 and 100")

# UI prompt
user_guess = st.number_input("Pick a number between 1 and 100",min_value=1,max_value=100,step=1)



# UI interaction
if st.button("Guess"):
    response = st.chat_message("assistant")
    ss.guesses += 1
    # pos feedback 
    if user_guess == ss.secret_number:
        response.write("Well done :)")
        st.balloons()
        ss.effectiveness.append(ss.guesses)
        ss.restart = True
        time.sleep(2)
       
    # neg feedback
    else:
        #ss.wrong = True
        response.write("Wrong number :(")
        #message.markdown("Would you like a hint?")
        hinter(user_guess,ss.secret_number,response)
        