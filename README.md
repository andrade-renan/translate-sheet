## README

### Project Overview

This project involves translating a cosmetics ingredients dataset from English to Portuguese. The dataset is in CSV format and contains information about the ingredients used in cosmetic products. The primary goal is to make the dataset more accessible to Portuguese-speaking professionals in the cosmetics industry.

### Files

- `cosing-ingredients.csv`: Original dataset containing cosmetics ingredients in English.
- `Cosing-ingredients-translated.csv`: Translated dataset with cosmetics ingredients in Portuguese.

### Requirements

To run the script, you need Python installed on your system along with the following libraries:

- `pandas`: For data manipulation and analysis.
- `deep_translator`: To perform the translations using Google Translate.

You can install the necessary libraries using pip:

```bash
pip install pandas deep_translator
```

### Script Explanation

The script performs the following steps:

1. Imports the necessary libraries (`pandas` and `deep_translator`).
2. Reads the original CSV file using `pandas`.
3. Iterates through each entry in the dataset, translating both the 'INCI name' and 'Function' columns from English to Portuguese using `GoogleTranslator` from the `deep_translator` package.
4. Replaces the English text with the Portuguese translations in the dataframe.
5. Saves the translated dataset to a new CSV file, `Cosing-ingredients-translated.csv`.

### Usage

To run the script, execute the following command in the terminal:

```bash
python translate-sheet.py
```

Make sure the script file (`translate-sheet.py`) and the CSV file (`cosing-ingredients.csv`) are in the same directory, unless paths are adjusted in the script.

### Note

- Ensure you have an active internet connection as `GoogleTranslator` requires it to function.
- The translation process can take some time depending on the size of the dataset and the speed of your internet connection.
