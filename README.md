# TIC-TAC-TOE Game
A simple Tic-Tac-Toe game with a Python backend and a Tkinter frontend. The game supports two players taking turns to play as Player X and Player O.

Features
Two-Player Mode: Players take turns to play as X and O.

Win/Draw Detection: The game automatically detects when a player wins or if the game is a draw.

Reset Game: Players can reset the game at any time to start a new match.

Backend-Frontend Architecture: The backend handles game logic, while the frontend provides a graphical interface.

Technologies Used
Backend: Python (Flask)

Frontend: Python (Tkinter)

Communication: HTTP requests (using requests library)

How to Run the Project
Prerequisites
Python 3.x: Make sure Python is installed on your system.

Flask: Install Flask for the backend.

Tkinter: Tkinter is included with Python by default.

requests: Install the requests library for the frontend.

Install Dependencies
Run the following commands to install the required libraries:
pip install flask requests
Steps to Run the Project
Clone the Repository
git clone https://github.com/your-username/tic-tac-toe.git
cd tic-tac-toe
Start the Backend

Navigate to the project directory and run the backend:
python backend.py
Start the Frontend

Open a new terminal window and run the frontend:
python frontend.py
A Tkinter window will open, allowing you to play the game.

Play the Game

Player X starts the game.
Click on any button to make a move.
The turn alternates between Player X and Player O.
The game will announce the winner or a draw when the game ends.
Use the "Reset" button to start a new game.


Project Structure
tic-tac-toe/
│
├── backend.py          # Backend logic (Flask server)
├── frontend.py         # Frontend GUI (Tkinter)
├── README.md           # Project documentation
└── requirements.txt    # List of dependencies

Contributions are welcome!
