import tkinter as tk
import random

# Game logic
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    
    if (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "scissors" and computer_choice == "paper") or \
       (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

def on_choice(choice):
    # Computer's random choice
    computer_choice = random.choice(["rock", "paper", "scissors"])
    
    # Determine the winner
    result = determine_winner(choice, computer_choice)
    
    # Update scores
    if result == "You win!":
        update_score("user")
    elif result == "You lose!":
        update_score("computer")
    
    # Display choices and result
    label_computer_choice.config(text=f"Computer chose: {computer_choice.capitalize()}")
    label_result.config(text=result)

def update_score(winner):
    global user_score, computer_score
    
    if winner == "user":
        user_score += 1
    elif winner == "computer":
        computer_score += 1
    
    # Update score display
    label_user_score.config(text=f"Your Score: {user_score}")
    label_computer_score.config(text=f"Computer's Score: {computer_score}")

def play_again():
    label_computer_choice.config(text="")
    label_result.config(text="")

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")

# Initialize scores
user_score = 0
computer_score = 0

# Create and place widgets
label_title = tk.Label(root, text="Rock, Paper, Scissors", font=("Arial", 18))
label_title.pack(pady=10)

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

button_rock = tk.Button(frame_buttons, text="Rock", width=10, command=lambda: on_choice("rock"))
button_rock.grid(row=0, column=0, padx=5)

button_paper = tk.Button(frame_buttons, text="Paper", width=10, command=lambda: on_choice("paper"))
button_paper.grid(row=0, column=1, padx=5)

button_scissors = tk.Button(frame_buttons, text="Scissors", width=10, command=lambda: on_choice("scissors"))
button_scissors.grid(row=0, column=2, padx=5)

label_user_score = tk.Label(root, text=f"Your Score: {user_score}", font=("Arial", 14))
label_user_score.pack(pady=5)

label_computer_score = tk.Label(root, text=f"Computer's Score: {computer_score}", font=("Arial", 14))
label_computer_score.pack(pady=5)

label_computer_choice = tk.Label(root, text="", font=("Arial", 14))
label_computer_choice.pack(pady=5)

label_result = tk.Label(root, text="", font=("Arial", 14))
label_result.pack(pady=5)

button_play_again = tk.Button(root, text="Play Again", command=play_again, font=("Arial", 14))
button_play_again.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
