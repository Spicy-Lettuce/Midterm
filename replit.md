# Python Programs Collection

## Overview
This is a collection of three Python programs imported from a GitHub repository. The project includes:
- A duplicate number finder that sorts and analyzes data
- A prime number finder
- A GUI-based memory matching game

## Project Structure
```
.
├── main.py              # Main menu runner script
├── FindDuplicates.py    # Sorts data and finds duplicates
├── prime.py             # Finds prime numbers in a range
├── MatchinGame.py       # GUI matching game (tkinter)
├── p2.txt              # Data file (100,000 numbers)
└── .gitignore          # Python gitignore
```

## Programs

### 1. Find Duplicates (FindDuplicates.py)
- Loads 100,000 numbers from `p2.txt`
- Implements quicksort algorithm to sort the data
- Identifies and counts duplicate numbers
- Console-based output

### 2. Prime Number Finder (prime.py)
- Searches for prime numbers in a configurable range (default: 1,000 to 40,000)
- Displays each prime number found
- Shows execution time in milliseconds

### 3. Matching Game (MatchinGame.py)
- GUI-based memory matching game using tkinter
- Configurable grid size (default: 5x6)
- Color-based matching pairs
- **Note:** Requires a graphical display environment to run

## How to Run

The project uses a main menu system. When you run the project, you'll see:
```
1. Find Duplicates - Sort and find duplicate numbers
2. Prime Number Finder - Find prime numbers in a range
3. Matching Game - GUI memory matching game (requires display)
4. Exit
```

Simply enter the number of the program you want to run.

## Technical Details

### Languages & Tools
- Python 3.11
- tkinter (for GUI game - requires display)

### Workflow
- **Main Menu**: Console-based menu system that launches individual programs

### Limitations
- The Matching Game requires a graphical display environment (X11/display server)
- In console-only environments, the game may not function properly

## Recent Changes
- **2025-10-06**: Imported from GitHub and set up Replit environment
  - Added main.py menu runner
  - Configured Python 3.11
  - Added .gitignore for Python
  - Set up workflow for console menu

## Architecture Notes
- Each program is standalone and can be run independently
- The main.py script uses subprocess to launch programs
- Data file (p2.txt) contains 100,000 integers for duplicate analysis
