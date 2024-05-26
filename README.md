# WineClassifier

## Overview
**WineClassifier** is a data science project aimed at predicting the quality of wine based on physicochemical and sensory variables. By leveraging various machine learning techniques, this project classifies wines into three quality categories: low, medium, and high. Additionally, users can create an SQLite database with classification results from a CSV file containing wine records by running a simple script.

## Features
- **Wine Quality Prediction**: Classify wines as low, medium, or high quality based on input variables.
- **Data Ingestion**: Convert wine records from a CSV file into an SQLite database using the `ingestion.py` script.

## Data Source
This project uses the Wine Quality dataset from the UCI Machine Learning Repository. You can find more information about the dataset [here](https://archive.ics.uci.edu/dataset/186/wine+quality).

## Installation
To get started with WineClassifier, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/WineClassifier.git
    cd WineClassifier
    ```

2. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage
### Predicting Wine Quality
To predict the quality of a wine, you'll need to prepare your input data (physicochemical and sensory variables). You can use the provided model to make predictions on this data.

### Ingesting Data
To create an SQLite database from a CSV file containing wine records, run the `ingestion.py` script with the path to your CSV file:
```bash
python ingestion.py path/to/your/wine_records.csv
