# Hourly Data Consumption Analyzer

## Project Overview

This Python tool analyzes timestamped data consumption logs from JSON files to calculate total consumption within valid 1-hour time blocks. The program ensures data continuity by discarding any 1-hour block that contains gaps exceeding 15 minutes between consecutive samples.

---

## Features

- **Automatic detection** of continuous 1-hour blocks based on timestamps.
- **Gap validation:** Discards blocks where consecutive data points have gaps greater than 15 minutes.
- Supports JSON files containing data values labeled as either `data` or `balance`.
- Processes multiple JSON files in a directory and outputs detailed consumption reports.
- Robust error handling for corrupted or malformed input files.
- Outputs results as JSON files with per-block consumption details and total consumption summary.

---

## Project Structure

├── Attendance_gps_logs/ # Input JSON files directory
│ ├── example1.json
│ ├── example2.json
│ └── ...
├── output/ # Directory for output result files
│ ├── hourly_usage_example1.json
│ ├── hourly_usage_example2.json
│ └── ...
├── src/
│ ├── data_analyzer.py # Core analysis logic and validation
│ └── utils.py # Helper functions for date parsing and time calculations
├── main.py # Main script to run the analyzer on all input files
└── README.md # This file — project documentation



---

## Input Data Format

Input JSON files must contain a list of records, each with:

- A `date` field in ISO 8601 UTC format: `"YYYY-MM-DDTHH:MM:SS.sssZ"`.
- A numeric data field: either `data` or `balance`.
- Optional: a `timestamp` field (milliseconds since epoch) for sorting.

Example:

```json
[
  {
    "timestamp": 1749198569471,
    "balance": 91.06,
    "date": "2025-06-06T08:29:29.471Z"
  },
  {
    "timestamp": 1749200376914,
    "balance": 90.82,
    "date": "2025-06-06T08:59:36.914Z"
  }
]
