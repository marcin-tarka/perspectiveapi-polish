import pandas as pd


startFileIndx = 1
endFileIndx = 278

composed = pd.DataFrame()
for indx in range(startFileIndx, endFileIndx):
    print("Putting together file ", indx)
    fileName = '../data/attack_annotated_comments_pl.csv.' + str(indx) + '.translated'
    translated = pd.read_csv(fileName, index_col=0, encoding = "ANSI")
    for index, row in translated.iterrows():
        composed = composed.append(row)
composed.to_csv('../data/attack_pl.csv')
