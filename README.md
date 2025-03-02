# Digital Clock

A modern, customizable digital clock application built with Python and [Qt](https://doc.qt.io/qtforpython-6/index.html). This application displays the current time in a clean, easy-to-read format with customizable features.

## Features

- Clean, modern interface with LCD-style display
- Customizable display color
- Draggable window (click and drag anywhere)
- Frameless window design
- 24-hour time format (HH:MM:SS)
- Color picker for display customization
- Keyboard shortcuts for quick actions

## Requirements

- Python 3.8 or higher
- PySide6 and related packages (specified in requirements.txt)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/sindhu2698/DigitalClock.git
cd DigitalClock
```

2. Create and activate a virtual environment (optional) :
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/macOS
python -m venv .venv
source .venv/bin/activate
```

3. Install required packages (recommended):
```bash
python -m pip install -r requirements.txt
```

## Usage

1. Run the application:
```bash
python DigitalClock.py
```
    A digital clock showing the current time will appear on your screen.

2. Controls:
   - Click and drag anywhere on the clock to move it
   - Click "Change Color" button to customize the display color
   - Press `Esc` to close the application

## Customization

The clock comes with several customizable features:
- Display color can be changed using the color picker
- Window size is adjustable in the code (default: 1000x300)
- Default color is set to green (can be modified in the code)

## Development

To modify the code:
1. The main application logic is in `DigitalClock.py`
2. The UI is built using PySide6 (Qt for Python)
3. The clock updates every second using QTimer

## License

[MIT License](https://choosealicense.com/licenses/mit/)
