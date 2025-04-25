# Speedboard Leaderboard

Leaderboard frontend and backend for tracking runner times, built with Python.

---

## Table of Contents

- [Features](#features)  
- [Compatibility](#compatibility)  
- [Requirements](#requirements)  
- [Installation](#installation)  
  - [Pre-Built](#pre-built)  
  - [From Source](#from-source)  
- [Getting Started](#getting-started)  
- [Usage](#usage)  
- [Troubleshooting](#troubleshooting)  
- [Credits](#credits)  
- [Author](#author)  

---

## Features

- 💻 GUI-based leaderboard frontend for speedrun timing and submission  
- 🔧 Backend logic for sorting and saving leaderboard entries  
- 📄 HTML output via `leaderboard.html`  
- 🧩 Modular design using a frontend/backend split  
- 🏁 Quick packaging via PyInstaller into a standalone executable  

---

## Compatibility

- Tested on **Windows 10/11**  
- Python 3.9–3.11 compatible  
- Requires basic system terminal or CMD for running from source  

---

## Requirements

To run from source, you’ll need the following Python libraries:

```
PyQt6
```

You can install all dependencies with:

```bash
pip install -r requirements.txt
```

Your `requirements.txt` should look like:

```
PyQt6
```

---

## Installation

### Pre-Built

A standalone Windows executable can be created using PyInstaller.  
Once built, run `main.exe` from the `dist` folder. No Python installation required.

Steps:

1. Download the file from the releases tab
2. Extract and double click on the file and the GUI should popup
3. Click the save all and update leaderboard button to 

---

### From Source

1. Download and unzip this repository  
2. *(Optional)* Create a virtual environment  
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the app:

```bash
python main.py
```

---

## Getting Started

The application consists of:

- `main.py`: Entry point  
- `src/leaderboard_backend.py`: Backend logic  
- `src/leaderboard_frontend.py`: PyQt6 GUI  
- `leaderboard.html`: HTML output used for display or saving  

You can run `main.py` to launch the full frontend and backend interface.

---

## Usage

- Add or update leaderboard entries via the GUI  
- Times are sorted and saved through backend logic  
- Output is formatted and stored in `leaderboard.html` which can be added to OBS by copy-pasting the absolute path
- You can view or embed the HTML file externally for sharing leaderboard standings  

---

## Troubleshooting

- If the app fails to import modules, make sure you’re running from the root folder and have used the `--paths=src` flag for PyInstaller  
- If `leaderboard.html` is not updating automatically, you will have to click 
- For missing dependencies, reinstall with `pip install -r requirements.txt`  

---

## Credits

- Tkitner for the frontend GUI  
- Python’s built-in libraries for backend logic  
- PyInstaller for packaging  

---

## Author
GhostTSR

