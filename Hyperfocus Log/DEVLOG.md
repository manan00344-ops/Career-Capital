# Development Log

## Day 1 - Initial Concept

Started thinking about how to track my daily work. Wanted something simple that doesn't require a database or cloud service. Decided on JSON for storage.

## Day 2 - Core Logic

Built the scoring system. Tried different formulas but settled on `(hours/16)*10` because it's simple and 16 hours is a solid productive day.

## Day 3 - CLI Version

Created a command-line version first to test the logic. Worked well but felt clunky to use daily.

## Day 4 - GUI Implementation

Switched to Tkinter. First time really using it seriously. Struggled with layout at first but `.pack()` made it easier than I thought.

## Day 5 - Polish

Added error handling, success messages, and the history viewer. Also wrote comprehensive comments.

## Lessons Learned

- Tkinter is actually pretty simple for basic GUIs
- JSON is perfect for simple data storage
- Good comments make a huge difference
- Breaking the project into functions makes testing easier
