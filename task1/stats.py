import streamlit as st
import time
import numpy as np
import pandas as pd
import random as rand
from streamlit import session_state as ss

#Having the Innit her to to prevent bugs, TBD move to app

if "restart" not in ss:
    ss.restart = True
    ss.guesses = 0
    ss.games = -1
    ss.gwon = 0
    ss.glost = 0
    ss.effectiveness = [0]

if ss.restart:
    ss.secret_number = rand.randint(1, 100)
    ss.games += 1
    ss.guesses = 0
    ss.min = 0
    ss.max = 0
    ss.restart = False

st.markdown("# Stats")
# Writing the stats
introMessage = st.chat_message("assistant")
introMessage.write("You already played "+str(ss.games) +" games")
introMessage.write("You already guessed " +str(ss.guesses) +" times this game")
#Plotting the Graph
st.bar_chart(ss.effectiveness)
