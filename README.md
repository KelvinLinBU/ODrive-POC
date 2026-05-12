# ODrive Data Logger

This project contains a Python script that connects to one ODrive over USB and records:

- Timestamp
- Elapsed time
- Current
- Position
- Velocity

The data is saved to a CSV file in the project folder.

---

## Requirements

Before starting, make sure you have:

- VS Code installed
- Python installed
- Git installed
- One ODrive connected to your computer by USB
- The ODrive powered on
- A USB cable that supports data, not just charging

---

## 1. Open the Project in VS Code

Open VS Code.

Then open the built-in terminal:

```text
Terminal > New Terminal
```

Clone the GitHub repository:

```bash
git clone https://github.com/KelvinLinBU/ODrive-POC
```

Open the cloned folder in VS Code:

```text
File > Open Folder...
```

Select the project folder that was just downloaded.

Example folder name:

```text
odrive_logger
```

---

## 2. Create a Virtual Environment

In the VS Code terminal, run:

```bash
python -m venv venv
```

If you have python3, run:

```bash
python3 -m venv venv
```

This creates a local Python environment inside the project folder.

---

## 4. Activate the Virtual Environment

In the VS Code terminal, run:

### Windows PowerShell

```powershell
venv\Scripts\Activate.ps1
```

### Windows Command Prompt

```cmd
venv\Scripts\activate
```

After activation, your terminal should show:

```text
(venv)
```

---

## 5. Install Dependencies

In the same terminal with the virtual environment, nstall the ODrive package directly:

```bash
pip install odrive 
# or pip3
```

---

## 6. Connect the ODrive

Connect the ODrive to the computer using USB.

Make sure:

- The ODrive is powered
- The motor is safely mounted
- Only one ODrive is connected for this version of the script

---

## 7. Run the Logger in VS Code

In VS Code, open the file:

```text
odrive_logger.py
```

Then run it using either option below.

### Option A: Run from the VS Code Terminal

```bash
python odrive_logger.py
```

or 

```bash
python3 odrive_logger.py
```

### Option B: Run with the VS Code Play Button

Open `odrive_logger.py`.

Click the play button in the top-right corner of VS Code.

Make sure VS Code is using the virtual environment interpreter selected earlier.

---

## 8. Stop the Logger

To stop recording, click into the VS Code terminal and press:

```text
Ctrl + C
```

The CSV file will remain saved in the project folder.

---

## 9. Output File

Each time the script runs, it creates a CSV file with a timestamped name.

Example:

```text
odrive_log_20260512_123001.csv
```

The CSV will contain columns like:

```text
timestamp,elapsed_time_s,current_a,position_turns,velocity_turns_per_s
```

Example row:

```text
2026-05-12T12:30:01,0.000,0.132,0.015,0.000
```

---

## 10. Change the Logging Interval

Open `odrive_logger.py` and find:

```python
LOG_INTERVAL_SECONDS = 1
```

Change the number to control how often data is recorded.

Examples:

```python
LOG_INTERVAL_SECONDS = 0.5  # records twice per second
LOG_INTERVAL_SECONDS = 0.1  # records ten times per second
LOG_INTERVAL_SECONDS = 2    # records once every two seconds
```

---
