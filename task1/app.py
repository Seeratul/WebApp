import streamlit as st



# desc of tab
st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)


st.markdown("# Guessing Game")

# init multipage app
pg = st.navigation([st.Page("playboy.py"), st.Page("stats.py")])
pg.run()