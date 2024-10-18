# Importing Pandas and Deep Translator library
import pandas as pd 
from deep_translator import GoogleTranslator

df = pd.read_csv('.\cosing-ingredients.csv', delimiter=';') # Creating a database



for i in range(len(df)):

    translated = GoogleTranslator(source='auto', target='pt').translate(f"={df['INCI name'][i]}")
    translated = translated.replace('=','')
    df['INCI name'][i] = translated

    translated = GoogleTranslator(source='auto', target='pt').translate(f"={df['Function'][i]}")
    translated = translated.replace('=','')
    df['Function'][i] = translated


df.to_csv('Cosing-ingredients-translated.csv')