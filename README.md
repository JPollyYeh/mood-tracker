# Mood Tracker

A small desktop app for recording how you feel each day.

I built this project while learning Python and used outside guidance to help me understand and assemble parts of the code. It is an early practice project—not a finished health or analytics tool—but it gave me hands-on experience with graphical interfaces, functions, CSV files, and user input.

## What the app does

The app opens a simple Tkinter window with three tabs:

- **Mood:** Choose Happy, Sad, Angry, or Hurt and save the response with the current date.
- **Fun:** A placeholder for a future choose-your-own-adventure feature.
- **Personality Quiz:** Record a simple Introvert or Extrovert response.

Mood entries are stored locally in `moods.csv`, while personality responses are stored in `personality.csv`. The app creates these files automatically in the folder where it is run.

## Built with

- Python
- Tkinter and ttk
- Python’s built-in `csv` module
- Python’s built-in `datetime` module

No external packages are required.

## How to run it

1. Download or clone this repository.
2. Make sure Python 3 is installed.
3. Open a terminal in the project folder.
4. Run:

   ```bash
   python "today mood v 1.0.0.01.py"

   — generated with chatgpt
