import streamlit as st
import time
import random
import os

# Game choices
choices = ["Rock", "Paper", "Scissors"]

# Helper function to determine the winner
def determine_winner(hand1, hand2):
    if hand1 == hand2:
        return "Draw"
    elif (
        (hand1 == "Rock" and hand2 == "Scissors") or
        (hand1 == "Paper" and hand2 == "Rock") or
        (hand1 == "Scissors" and hand2 == "Paper")
    ):
        return "Computer"
    else:
        return "Player"

# Smart computer strategy
def smart_computer_strategy(player_left, player_right):
    # Analyze player choices and counter them
    counter_left = "Paper" if player_left == "Rock" else ("Scissors" if player_left == "Paper" else "Rock")
    counter_right = "Paper" if player_right == "Rock" else ("Scissors" if player_right == "Paper" else "Rock")
    
    # Computer randomly decides which counter to play
    return counter_left, counter_right

import os

image_dir = r"C:\Users\sisir\Rock paper scissor"  # Use your absolute path here
rock_img = os.path.join(image_dir, "rock.png")
paper_img = os.path.join(image_dir, "paper.png")
scissors_img = os.path.join(image_dir, "scissors.png")

# Ensure files exist
if not os.path.exists(rock_img):
    raise FileNotFoundError(f"File not found: {rock_img}")
if not os.path.exists(paper_img):
    raise FileNotFoundError(f"File not found: {paper_img}")
if not os.path.exists(scissors_img):
    raise FileNotFoundError(f"File not found: {scissors_img}")

# Ensure files exist
if not os.path.exists(rock_img):
    raise FileNotFoundError(f"File not found: {rock_img}")
if not os.path.exists(paper_img):
    raise FileNotFoundError(f"File not found: {paper_img}")
if not os.path.exists(scissors_img):
    raise FileNotFoundError(f"File not found: {scissors_img}")

image_mapping = {"Rock": rock_img, "Paper": paper_img, "Scissors": scissors_img}

# Initialize session state
if 'computer_left' not in st.session_state:
    st.session_state.computer_left = "Rock"
if 'computer_right' not in st.session_state:
    st.session_state.computer_right = "Rock"
if 'player_left' not in st.session_state:
    st.session_state.player_left = "Rock"
if 'player_right' not in st.session_state:
    st.session_state.player_right = "Rock"
if 'round_started' not in st.session_state:
    st.session_state.round_started = False

# Streamlit UI
st.title("Rock Paper Scissors - Dual Hands")

st.write("### Player: Select your choices")
player_left = st.selectbox("Player Left Hand", choices, key="player_left_widget")
player_right = st.selectbox("Player Right Hand", choices, key="player_right_widget")

if st.button("Start Round"):
    st.session_state.player_left = player_left
    st.session_state.player_right = player_right

    # Computer makes smart choices
    computer_left, computer_right = smart_computer_strategy(player_left, player_right)
    st.session_state.computer_left = computer_left
    st.session_state.computer_right = computer_right
    st.session_state.round_started = True

if st.session_state.round_started:
    st.write("### Choices made")
    st.image([image_mapping[st.session_state.computer_left], image_mapping[st.session_state.computer_right]], width=150, caption=["Computer Left", "Computer Right"])
    st.image([image_mapping[st.session_state.player_left], image_mapping[st.session_state.player_right]], width=150, caption=["Player Left", "Player Right"])

    # Simulate 5-second delay for decision-making
    st.write("### Players have 5 seconds to decide which hand to take out...")
    time.sleep(5)

    st.write("### Decisions")
    
    # Computer decides which hand to keep strategically
    if (
        st.session_state.computer_left == st.session_state.player_left or 
        st.session_state.computer_left == st.session_state.player_right
    ):
        computer_decision = "Left"
    else:
        computer_decision = "Right"

    computer_final = (
        st.session_state.computer_left if computer_decision == "Left" else st.session_state.computer_right
    )

    # Player decides which hand to keep
    player_decision = st.radio(
        "Player, which hand will you keep?", ["Left", "Right"], key="player_decision"
    )
    player_final = (
        st.session_state.player_left if player_decision == "Left" else st.session_state.player_right
    )

    if st.button("Finalize Choices"):
        st.write(f"Computer keeps: {computer_final}")
        st.image(image_mapping[computer_final], width=200, caption="Computer Final Choice")
        st.write(f"Player keeps: {player_final}")
        st.image(image_mapping[player_final], width=200, caption="Player Final Choice")

        # Determine the winner
        winner = determine_winner(computer_final, player_final)
        if winner == "Draw":
            st.write("### It's a Draw!")
        elif winner == "Player":
            st.write("### Congratulations! You win!")
        else:
            st.write("### 🗨✨ You're killed! 😠")

        # Reset round state
        st.session_state.round_started = False
