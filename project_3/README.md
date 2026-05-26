# File Handling & Data Processing System - Task 3

## Overview
A Python-based system designed to process employee salary data. It reads from a CSV, performs filtering and calculations, and generates structured text reports.

## Features
- **Modular Design**: Uses functions to separate reading, processing, and writing logic.
- **Robustness**: Handles `FileNotFoundError` and `PermissionError` exceptions gracefully.
- **Dynamic Reporting**: Allows user input to generate reports for specific departments.
- **Clean Output**: Exports professionally formatted text reports with timestamps.

## Project Structure
- `main.py`: The entry point and core logic.
- `data/`: Contains the `employees.csv` source file and generated `.txt` reports.

## How to Run
1. Ensure you have Python installed.
2. Open your terminal in the `project_3/` directory.
3. Run the application:
   ```bash
   python main.py