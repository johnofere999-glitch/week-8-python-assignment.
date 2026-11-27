# Personal Mini-Toolkit

## What Your Toolkit Does
Personal Mini-Toolkit is a menu-driven Python command-line app with three
tools: **Quick To-Do List** (manage a live list of tasks), **Pass & Grade Checker** 
(check pass status and letter grade from a score), and **Multiplication Table Generator** (print a 1–12 table using a loop).

## How to Run It
1. Make sure Python 3 is installed on your computer.
2. Open a terminal in the project folder (`plp-python-week8`).
3. Run `python toolkit.py` (or `python3 toolkit.py`) and follow the on-screen menu prompts.

## Reflection
Planning the menu structure and tool responsibilities in `toolkit_plan.txt` first made writing `toolkit.py` 
much clearer and helped separate the sub-menu loop from the main menu loop. Keeping track of list
indexing (`enumerate(..., start=1)` vs. zero-based list positions) when removing tasks was the trickiest part
of the build. Making sure non-numeric inputs and out-of-range menu choices print friendly messages instead of raising 
`ValueError` or `IndexError` took the most care to get right. If I had another week, I would save the to-do list to a JSON
or text file so tasks persist across sessions and add a simple calculator tool.
