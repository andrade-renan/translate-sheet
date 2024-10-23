import pandas as pd
from deep_translator import GoogleTranslator
from time import sleep
import json
import os

# capturando a planilha no formato inicial com encoding em iso-8859-1
df = pd.read_csv('.\cosing-ingredients.csv', delimiter=';', encoding='iso-8859-1')

# salvando a planilha com formato utf-8
df.to_csv('.\cosing-ingredients-utf-8.csv', index=False, encoding='utf-8')

# capturando a planilha formatada
df = pd.read_csv('.\cosing-ingredients-utf-8.csv', encoding='utf-8')

# Caminho para o arquivo JSON onde as traduções são armazenadas
translations_path = 'translations.json'

# Tentar carregar traduções existentes
if os.path.exists(translations_path):
    with open(translations_path, 'r', encoding='utf-8') as file:
        translations = json.load(file)
else:
    translations = {}

def get_translation(text, src='auto', tgt='pt'):
    try:
        if text not in translations:
            sleep(0.1)  # Delay para evitar atingir limites de uso da API
            translated_text = GoogleTranslator(source=src, target=tgt).translate(f"={text}")
            translations[text] = translated_text.replace("=", '')
            # Salvar o dicionário atualizado após cada nova tradução
            with open(translations_path, 'w', encoding='utf-8') as file:
                json.dump(translations, file, ensure_ascii=False)
        print(f"Sucesso ao traduzir {text}")
        return translations[text]
    except Exception as e:
        print(f"Erro ao traduzir {text}: {e}")
        return text  # Retorna o texto original em caso de erro

# Aplicando tradução aos dados em lote
for index, row in df.iterrows():
    df.at[index, 'INCI name'] = get_translation(row['INCI name'])
    df.at[index, 'Function'] = get_translation(row['Function'])
    
    # Salvando sempre para evitar perda de dados
    df.to_csv('Cosing-ingredients-translated-partial.csv', index=False, encoding='utf-8', sep=";")

# Salvando o dataframe completo ao final do processo
df.to_csv('Cosing-ingredients-translated.csv', index=False, encoding='utf-8', sep=";")

