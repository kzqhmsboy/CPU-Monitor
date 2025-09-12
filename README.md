# CPU Monitor

A simple Python script to monitor your system's CPU usage and print a warning if it goes above 80%.

## Features

- Continuously monitors CPU usage using `psutil`
- Prints current CPU usage at regular intervals
- Displays a warning when CPU usage exceeds 80%

## Requirements

- Python 3.x
- [psutil](https://pypi.org/project/psutil/)

## Installation

Install `psutil` with pip:

```bash
pip install psutil
```

## Usage

Run the script:

```bash
python cpu_monitor.py
```

You will see the current CPU usage printed every few seconds. If the usage goes above 80%, a warning will be shown.

Press `Ctrl+C` to stop monitoring.

## License

This project is licensed under the MIT License.
