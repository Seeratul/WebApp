import streamlit as st
import random
import openai
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Initialize OpenAI API
openai.api_key = "YOUR_OPENAI_API_KEY"

# Initialize session state variables
if 'games_played' not in st.session_state:
    st.session_state['games_played'] = 0
    st.session_state['total_guesses'] = 0
    st.session_state['guess_count'] = []

def guess_game():
    animals = ["dog", "cat", "bird", "elephant", "giraffe"]
    answer = random.choice(animals)
    guesses = 0

    # Placeholder for chat messages
    chat_placeholder = st.empty()

    while True:
        user_input = st.text_input("Guess the animal:")
        if user_input:
            guesses += 1
            st.session_state.total_guesses += 1
            st.session_state.guess_count.append(guesses)

            # Call to OpenAI LLM for evaluation
            # response = openai.ChatCompletion.create(
            #   model="gpt-3.5-turbo",
            #   messages=[
            #         {"role": "user", "content": f"Is it a {user_input}?"}
            #     ]
            # )
            response = "No Key found"
            answer_text = response['choices'][0]['message']['content']

            # Update chat messages
            chat_placeholder.text(f"Guess #{guesses}: {answer_text}")

            # Check if the guess is correct
            if user_input.lower() == answer:
                st.success(f"Correct! The animal was a {answer}.")
                st.session_state.games_played += 1
                st.session_state.guess_count[-1] = guesses  # Update count for current game
                break

            elif guesses >= 5:  # Consider 5 guesses max
                st.error("Out of guesses! The animal was a {answer}.")
                st.session_state.games_played += 1
                break

def display_stats():
    st.write(f"Total games played: {st.session_state['games_played']}")
    if st.session_state['games_played'] > 0:
        avg_guesses = st.session_state['total_guesses'] / st.session_state['games_played']
        st.write(f"Average guesses per game: {avg_guesses:.2f}")

        # Display a bar chart
        plt.figure(figsize=(10, 5))
        plt.bar(range(1, len(st.session_state['guess_count']) + 1), st.session_state['guess_count'])
        plt.title('Number of Guesses per Game')
        plt.xlabel('Game Number')
        plt.ylabel('Number of Guesses')
        st.pyplot()

# Main app
st.title("Guessing Game App")

menu = ["Play", "Stats"]
choice = st.sidebar.selectbox("Select Page", menu)

if choice == "Play":
    guess_game()
elif choice == "Stats":
    display_stats()
