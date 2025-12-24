# 📈 Compound Effect Tracker

A simple Python application to track daily productive hours across multiple categories and visualize the compound effect of consistent work over time.

## 🎯 Motivation

1.Inspired by Darren Hardy's book _The Compound Effect_, this tracker helps me stay accountable by logging daily work hours. The idea is simple: **small, consistent efforts compound into massive results over time.**
2.Inspired by Chris Bailey's _Hyperfocus_, this tracker helps to keep track of hyperfocus state and also supports scatterfocus.

Instead of just working hard, I wanted to **measure** my efforts and see the compound effect in action.

## ✨ Features

- ✅ Track time across 6 categories (DSA, Projects, College, ML, Code Reading, Writing)
- ✅ Automatic score calculation (16 hours = 10 points)
- ✅ View complete history of all logged days
- ✅ Simple, clean GUI built with Tkinter
- ✅ JSON-based storage (no database needed)
- ✅ Cross-platform (Windows, Mac, Linux)

### Prerequisites

- Python 3.8 or higher
- Tkinter

## 📖 How It Works

### Scoring System

The app uses a simple linear scoring formula:

```
Score = (Total Hours / 16) × 10
```

- **4 hours** = 2.5 points
- **8 hours** = 5.0 points
- **12 hours** = 7.5 points
- **16+ hours** = 10.0 points (maxed out!)

Just honest tracking.

### Data Storage

All logs are stored in `logs.json` in this format:(eg:)

```json
{
  "date": "2024-12-24",
  "minutes": {
    "dsa": 120,
    "project": 60,
    "code_read": 30,
    "college": 180,
    "ml_learn": 20,
    "writing": 10
  },
  "total_hours": 7.0,
  "score": 4.4,
  "notes": "Solved 3 LC problems, worked on portfolio"
}
```

## 🖥️ Usage

### Logging Your Day

1. Open the app
2. Enter minutes for each category
3. Add optional notes about what you accomplished
4. Click "Save Log"

### Viewing History

Click "View History" to see all your past entries with dates, scores, and notes.

## 🛠️ Technical Details

### Built With

- **Python 3** - Core language
- **Tkinter** - GUI framework (built-in)
- **JSON** - Data storage format

### Key Learning Points

While building this project, I learned:

- How to create GUI applications with Tkinter
- File I/O operations (reading/writing JSON)
- Event-driven programming (button clicks, user input)
- Data validation and error handling
- Designing simple but effective scoring systems

## 🔮 Future Enhancements

Ideas for v2.0:

- [ ] Weekly/monthly statistics dashboard
- [ ] Data visualization (charts and graphs)
- [ ] Export logs to CSV/Excel
- [ ] Edit/delete past entries
- [ ] Streak tracking (consecutive days)
- [ ] Custom categories
- [ ] advanced UI

## 🤔 Why This Matters

This isn't just a time tracker. It's about **building a habit of measurement**.

> "You can't manage what you don't measure." - Peter Drucker

By logging daily work hours, I can:

- Stay accountable to myself
- Identify productive vs unproductive patterns
- See the compound effect in real data
- Build consistency over time

## 📝 License

MIT License - feel free to use this for your own tracking!

## 🙏 Acknowledgments

- Darren Hardy's _The Compound Effect_ for the inspiration
- Chris Bailey's _Hyperfocus_ for the inspiration
- The Python community for excellent documentation

**Made with ☕ and Python**
