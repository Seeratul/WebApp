import streamlit as st
import time
import numpy as np
import random as rand
from streamlit import session_state as ss
from funcs import hinter


# funcs

#streamlit run app.py
#Rebuilt site so it reruns on each button press.


if "restart" not in ss:
    ss.restart = True
    ss.guesses = 0
    ss.games = -1
    ss.gwon = 0
    ss.glost = 0
    

if ss.restart:
    ss.hint = False
    ss.secret_number = rand.randint(1, 10)
    ss.games += 1
    ss.guesses = 0
    ss.restart = False

####
#inits
#This could be one gated if statement

#if "want_hint" not in ss:
#    ss.want_hint = False

# title and desc
if ss.games == 0:
    st.title("Wanna play a game?")
else:
    st.title("Wanna play another game?")


#st.sidebar.success("Select a demo above.")

# init random number

#DO not call all your windows message it can make stuff fail, give each window its own name
# init speaker
introMessage = st.chat_message("assistant")
introMessage.write("Guess the Number between 1 and 10")
# introMessage.write("You already played "+str(ss.games) +" games")
# introMessage.write("You already guessed " +str(ss.guesses) +" times this game")
# introMessage.write("This not always updating as intended is fine as we will just move it all to a different page that can update on switch")


# UI prompt
user_guess = st.number_input("Pick a number between 1 and 10",min_value=1,max_value=10,step=1)



# UI interaction
if st.button("Guess"):
    response = st.chat_message("assistant")
    ss.guesses += 1
    # pos feedback 
    if user_guess == ss.secret_number:
        response.write("Well done :)")
        st.balloons()
        time.sleep(2)
        #ss.games += 1
        ss.restart = True
       

    # neg feedback
    else:
        #ss.wrong = True
        response.write("Wrong number :(")
        #message.markdown("Would you like a hint?")
        ss.hint = True
        hinter(user_guess,ss.secret_number,response)
        


#hint
# if ss.hint:
#     if user_guess > ss.secret_number:
#         response.write("Hint: Pssst the number is smaller")
#     else:
#         response.write("Hint: Pssst the number is larger")
    # The best widget to use when dealing with user input is the form.
    #hint = st.radio('', ['YES', 'NO'], horizontal=True, index=None)
    # if ss.hint:
    #     ss.hint = True
    #     st.write(f"You selected {ss.hint}")
    #st.write("You selected:", hint )



# if ss.hint == "YES":
#     st.write("You selected comedy.")

#     # yes_button = st.button("YES", key=yes_key)
#     # no_button = st.button("NO", key=no_key)

#     # if st.button('Yes'):
#     #     st.session_state.hint = True
#     #     message = st.chat_message("assistant")
#     #     message.write("Hint: Pssst the number is bigger than your guess")
        

#     # if st.button('No'):
#     #     st.session_state.hint = False
#     #     message = st.chat_message("assistant")
#     #     message.write("Alright, good luck")
         

#             #st.write(st.session_state.secret_number)
        
# if ss.hint:

#     message = st.chat_message("assistant")
#     message.write("Hint: Pssst the number is bigger than your guess")
#     if st.session_state.secret_number > user_guess:
#         #with st.chat_message("assistant"):
#         message.write("Hint: Pssst the number is bigger than your guess")
#     else:
#         message.write("Hint: Pssst the number is smaller than your guess")
