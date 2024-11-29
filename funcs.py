import streamlit as st
import time
import numpy as np
import random as rand
from streamlit import session_state as ss


def hinter(input,target,cbox):
    #hint = st.chat_message("assistant")
    if input > target:
        cbox.write("Hinter: Pssst the number is smaller")
    else:
        cbox.write("Hinter: Pssst the number is larger")