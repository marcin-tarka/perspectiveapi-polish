from googleapiclient.discovery import build
import pandas as pd

key = 'your-googleapi-key'

service = build('translate', 'v2', developerKey=key)
startFileIndx = 289
endFileIndx = 490

for indx in range(startFileIndx, endFileIndx):
    print("Translating file ", indx)
    translated = pd.DataFrame()
    fileName = '../data/attack_annotated_comments_pl.csv.' + str(indx)
    comments = pd.read_csv(fileName, index_col=0, encoding="ISO-8859-1")
    for index, row in comments.iterrows():
        translations = service.translations().list(source='en', target='pl', q=row['comment']).execute()
        row['comment'] = translations['translations'][0]['translatedText']
        translated = translated.append(row)
    translated.to_csv(fileName + '.translated')
