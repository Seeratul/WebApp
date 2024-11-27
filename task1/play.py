import streamlit as st
import time
import numpy as np
import random as rand
from streamlit import session_state as ss


# funcs






####



# init global boolean
ss.wrong = False
ss.want_hint = False
ss.hint = False

# title and desc
st.title("Wanna play a game?")


#st.sidebar.success("Select a demo above.")

# init random number
if 'secret_number' not in ss:
    ss.secret_number = rand.randint(1, 10)


# init speaker
message = st.chat_message("assistant")
message.write("Guess the Number between 1 and 10")

# UI prompt
user_guess = st.number_input("Pick a number between 1 and 10")



# UI interaction
if st.button("Guess"):
    message = st.chat_message("assistant")
    # pos feedback 
    if user_guess == ss.secret_number:
        message.write("Well done :)")
        st.balloons()

    # neg feedback
    else:
        ss.wrong = True
        message.write("Wrong number :(")
        message.markdown("Would you like a hint?")
        ss.want_hint = True
        


# hint
if ss.want_hint:

    # The best widget to use when dealing with user input is the form.
    hint = st.radio('', ['YES', 'NO'], horizontal=True, index=None)
    # if ss.hint:
    #     ss.hint = True
    #     st.write(f"You selected {ss.hint}")
    st.write("You selected:", hint )



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
