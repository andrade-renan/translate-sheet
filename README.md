# Cosing Ingredients Translation Script

> _Note:_ This README was generated with ChatGPT

## Overview

This script reads a CSV file containing cosmetic ingredient data (INCI name, Function, etc.), translates the contents to Portuguese using the Google Translator API, and saves the results in new CSV files. The translations are stored in a JSON file to avoid redundant API calls and improve efficiency when running the script multiple times.

## Requirements

- **Pandas**: To read and manipulate CSV files.
- **Deep Translator**: To perform translations using Google Translator.
- **JSON**: To store the translated terms.
- **OS**: To check for the existence of translation files and handle file paths.

## Features

1. **CSV Conversion**: Converts the input CSV from ISO-8859-1 encoding to UTF-8 to ensure compatibility.
2. **Batch Translation**: Translates INCI name and Function columns from their source language to Portuguese.
3. **Translation Caching**: Saves translations in a JSON file to avoid redundant API calls and improve performance.
4. **Automatic Saving**: Periodically saves the partially translated CSV to ensure data is not lost in case of failure.
5. **Error Handling**: Captures and logs any translation errors, returning the original text if translation fails.

## Files

- **cosing-ingredients.csv**: The original CSV file containing the cosmetic ingredient data.
- **cosing-ingredients-utf-8.csv**: The UTF-8 formatted version of the original CSV file.
- **translations.json**: Stores translations of INCI name and Function fields to avoid redundant API requests.
- **Cosing-ingredients-translated-partial.csv**: Periodically saved version of the CSV with translated fields.
- **Cosing-ingredients-translated.csv**: The final translated CSV file.

## How to Use

### 1. Install Dependencies

To run the script, you need to install the following Python libraries:

```bash
pip install pandas deep-translator
```

### 2. Prepare Your CSV File

Ensure your CSV file is in the root directory and follows the format expected by the script, with at least the following columns:

- `INCI name`
- `Function`

Make sure the original CSV file encoding is ISO-8859-1 if it's not already in UTF-8 format.

### 3. Run the Script

Execute the script to start the translation process. The script will:

1. Convert the original CSV file from ISO-8859-1 encoding to UTF-8.
2. Translate the `INCI name` and `Function` columns into Portuguese.
3. Save the results periodically to prevent data loss.

```bash
python script.py
```

### 4. Review Output Files

The translated CSV files will be saved as:

- `Cosing-ingredients-translated-partial.csv` (intermediate results).
- `Cosing-ingredients-translated.csv` (final translated version).

### 5. Review Translations JSON

The `translations.json` file will store the translated terms for future reuse, allowing the script to avoid re-translating previously translated terms.

## Important Notes

- **API Rate Limit**: The script includes a delay of 0.1 seconds between translation requests to avoid hitting API rate limits. You can adjust this delay if needed.
- **Error Handling**: If any errors occur during translation, the script will print the error and continue with the next row, using the original text in place of a translation.
- **Translation Accuracy**: Automated translations may not always be 100% accurate, especially for specialized terms. Always review the translations.

## Customization

You can customize the following aspects of the script:

- **Translation Source and Target**: The `get_translation` function allows you to specify the source (`src`) and target (`tgt`) languages. By default, it detects the source language automatically and translates to Portuguese (`'pt'`).

```python
get_translation(text, src='auto', tgt='pt')
```

## License

This project is provided as-is without any warranty. Feel free to modify and distribute the script for personal or commercial use.
