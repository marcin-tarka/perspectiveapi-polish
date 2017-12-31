import pandas as pd


comments = pd.read_csv('../data/attack_annotated_comments.tsv', sep='\t', index_col=0)
comments['comment'] = comments['comment'].apply(lambda x: x.replace("NEWLINE_TOKEN", " "))
comments['comment'] = comments['comment'].apply(lambda x: x.replace("TAB_TOKEN", " "))

rows, _ = comments.shape
print("Read", rows, "rows")

CHAR_LIMIT = 100000
charCount = 0
partIndx = 0
plFrame = pd.DataFrame()
for index, row in comments.iterrows():
    if charCount + len(row['comment']) > CHAR_LIMIT:
        partIndx += 1
        print("Storing part number ", partIndx)
        plFrame.to_csv('../data/attack_annotated_comments_pl.csv.' + str(partIndx))
        plFrame = pd.DataFrame()
        charCount = 0
    charCount += len(row['comment'])
    plFrame = plFrame.append(row)
