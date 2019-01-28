from collections import Counter
import pandas as pd

with open('text.txt') as fin:
    counter = Counter(fin.read().strip().split())

numbers = sorted(counter.most_common(), key=lambda student: student[1], reverse=True)
top15 = numbers[0:15]
text = []
number = []
for i in top15:
   text.append(i[0])
   number.append(i[1])
rawdata = {'words': text, 'frequency': number}
df = pd.DataFrame(rawdata, columns = ['words', 'frequency'])

print(df)

