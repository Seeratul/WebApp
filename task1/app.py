import streamlit as st

#Just a programm to call so multi wpage stuff works
st.markdown("# Guessing Game")

# init multipage app
pg = st.navigation([st.Page("play.py"), st.Page("stats.py")])
pg.run()