"""
Compound Effect Tracker - GUI Application
A simple time tracking app to measure daily productive hours.
"""

import json
from datetime import date
import tkinter as tk
from tkinter import messagebox


def calculate_score(minutes):
    """
    Calculate daily score based on total productive hours.

    Formula: Score = (Total Hours / 16) × 10

    Args:
        minutes (dict): Dictionary with minutes per category

    Returns:
        float: Score from 0-10, rounded to 1 decimal place

    Example:
        >>> calculate_score({'dsa': 480, 'project': 0, ...})
        5.0
    """
    total_minutes = sum(minutes.values())
    total_hours = total_minutes / 60
    score = (total_hours / 16) * 10

    # Cap at 10 to prevent scores above maximum
    if score > 10:
        score = 10

    return round(score, 1)


def save_log(dsa, project, code_read, college, ml_learn, writing, notes):
    """
    Save daily log entry to logs.json file.

    Creates a new entry with today's date and all tracking data.
    If logs.json doesn't exist, it creates it automatically.

    Args:
        dsa (int): Minutes spent on DSA practice
        project (int): Minutes spent on projects
        code_read (int): Minutes spent reading code
        college (int): Minutes spent on college work
        ml_learn (int): Minutes spent learning ML
        writing (int): Minutes spent writing
        notes (str): Text notes about the day

    Returns:
        tuple: (total_hours, score) for display purposes
    """
    # Bundle all minutes into a dictionary for easy processing
    minutes = {
        'dsa': dsa,
        'project': project,
        'code_read': code_read,
        'college': college,
        'ml_learn': ml_learn,
        'writing': writing
    }

    # Calculate statistics
    total_hours = sum(minutes.values()) / 60
    score = calculate_score(minutes)

    # Create log entry with all data
    log_entry = {
        'date': str(date.today()),
        'minutes': minutes,
        'total_hours': round(total_hours, 1),
        'score': score,
        'notes': notes
    }

    # Load existing logs from file
    try:
        with open('logs.json', 'r') as f:
            logs = json.load(f)
    except FileNotFoundError:
        # If file doesn't exist yet, start with empty list
        logs = []

    # Append new entry and save back to file
    logs.append(log_entry)

    with open('logs.json', 'w') as f:
        json.dump(logs, f, indent=2)

    return total_hours, score


def on_save_click():
    """
    Event handler for Save Log button.

    Validates user input, saves the log, shows success message,
    and clears all input fields for next entry.
    """
    try:
        # Get values from entry boxes (use 0 if empty)
        dsa = int(entry_dsa.get() or 0)
        project = int(entry_project.get() or 0)
        code_read = int(entry_code.get() or 0)
        college = int(entry_college.get() or 0)
        ml_learn = int(entry_ml.get() or 0)
        writing = int(entry_writing.get() or 0)
        notes = entry_notes.get()

        # Save the log and get results
        total_hours, score = save_log(dsa, project, code_read, college,
                                      ml_learn, writing, notes)

        # Show success popup
        messagebox.showinfo("Success!",
                            f"Saved!\nTotal: {total_hours}h\nScore: {score}/10")

        # Clear all input fields
        entry_dsa.delete(0, tk.END)
        entry_project.delete(0, tk.END)
        entry_code.delete(0, tk.END)
        entry_college.delete(0, tk.END)
        entry_ml.delete(0, tk.END)
        entry_writing.delete(0, tk.END)
        entry_notes.delete(0, tk.END)

    except ValueError:
        # Show error if user entered non-numeric values
        messagebox.showerror("Error", "Please enter valid numbers!")


def on_view_history():
    """
    Event handler for View History button.

    Opens a new window displaying all logged entries
    in reverse chronological order (newest first).
    """
    try:
        # Load logs from file
        with open('logs.json', 'r') as f:
            logs = json.load(f)

        # Create new window for displaying history
        history_window = tk.Toplevel(window)
        history_window.title("History")
        history_window.geometry("500x400")

        # Add scrollable text widget
        text = tk.Text(history_window, wrap=tk.WORD, width=60, height=20)
        text.pack(padx=10, pady=10)

        # Display each log entry
        for log in reversed(logs):  # Show newest first
            text.insert(tk.END, f"Date: {log['date']}\n")
            text.insert(
                tk.END, f"Score: {log['score']}/10 ({log['total_hours']}h)\n")
            text.insert(tk.END, f"Notes: {log['notes']}\n")
            text.insert(tk.END, "-" * 50 + "\n\n")

    except FileNotFoundError:
        # Handle case where no logs exist yet
        messagebox.showinfo("No History", "No logs found yet!")


# ==================== GUI SETUP ====================

# Create main application window
window = tk.Tk()
window.title("Compound Effect Tracker")
window.geometry("400x500")

# Header
title = tk.Label(window, text="COMPOUND EFFECT TRACKER",
                 font=("Arial", 16, "bold"))
title.pack(pady=20)

# Input fields for each category
tk.Label(window, text="DSA Practice (minutes):").pack()
entry_dsa = tk.Entry(window, width=30)
entry_dsa.pack(pady=5)

tk.Label(window, text="Project Work (minutes):").pack()
entry_project = tk.Entry(window, width=30)
entry_project.pack(pady=5)

tk.Label(window, text="Code Reading (minutes):").pack()
entry_code = tk.Entry(window, width=30)
entry_code.pack(pady=5)

tk.Label(window, text="College Work (minutes):").pack()
entry_college = tk.Entry(window, width=30)
entry_college.pack(pady=5)

tk.Label(window, text="ML Learning (minutes):").pack()
entry_ml = tk.Entry(window, width=30)
entry_ml.pack(pady=5)

tk.Label(window, text="Writing (minutes):").pack()
entry_writing = tk.Entry(window, width=30)
entry_writing.pack(pady=5)

# Notes field
tk.Label(window, text="Notes:").pack()
entry_notes = tk.Entry(window, width=30)
entry_notes.pack(pady=5)

# Button container
button_frame = tk.Frame(window)
button_frame.pack(pady=20)

# Save button - calls on_save_click when pressed
save_button = tk.Button(button_frame, text="Save Log", command=on_save_click,
                        bg="green", fg="white", width=15)
save_button.pack(side=tk.LEFT, padx=5)

# History button - calls on_view_history when pressed
history_button = tk.Button(button_frame, text="View History",
                           command=on_view_history,
                           bg="blue", fg="white", width=15)
history_button.pack(side=tk.LEFT, padx=5)

# Start the GUI event loop
# This keeps the window open and responsive to user actions
window.mainloop()
