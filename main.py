# Importa pandas library for inmporting CSV
import pandas as pd 
from deep_translator import GoogleTranslator

# translated = GoogleTranslator(source='auto', target='pt').translate("=DISODIUM TETRAMETHYLHEXADECENYLCYSTEINE FORMYLPROLINATE")
# translated = translated.replace('=','')


# print(translated)

df = pd.read_csv('.\cosing-ingredients.csv', delimiter=';')



for i in range(len(df)):

    translated = GoogleTranslator(source='auto', target='pt').translate(f"={df['INCI name'][i]}")
    translated = translated.replace('=','')
    df['INCI name'][i] = translated

    translated = GoogleTranslator(source='auto', target='pt').translate(f"={df['Function'][i]}")
    translated = translated.replace('=','')
    df['Function'][i] = translated


df.to_csv('Cosing-ingredients-translated.csv')