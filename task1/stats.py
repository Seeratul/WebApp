import streamlit as st
import time
import numpy as np
import pandas as pd
from streamlit import session_state as ss

#st.set_page_config(page_title="Plotting Demo", page_icon="📈")

if "restart" not in ss:
    ss.restart = True
    ss.guesses = 0
    ss.games = 0
    ss.gwon = 0
    ss.glost = 0

st.markdown("# Stats")
#st.sidebar.header("Stats")
introMessage = st.chat_message("assistant")
introMessage.write("You already played "+str(ss.games) +" games")
introMessage.write("You already guessed " +str(ss.guesses) +" times this game")

# chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

# st.bar_chart(chart_data)

# progress_bar = st.sidebar.progress(0)
# status_text = st.sidebar.empty()
# last_rows = np.random.randn(1, 1)
# chart = st.line_chart(last_rows)

# for i in range(1, 101):
#     new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
#     status_text.text("%i%% Complete" % i)
#     chart.add_rows(new_rows)
#     progress_bar.progress(i)
#     last_rows = new_rows
#     time.sleep(0.05)

# progress_bar.empty()

# # Streamlit widgets automatically run the script from top to bottom. Since
# # this button is not connected to any other logic, it just causes a plain
# # rerun.
# st.button("Re-run")
