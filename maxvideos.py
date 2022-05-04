import pandas as pd
import numpy as np

df = pd.read_csv('TestVideo.csv', infer_datetime_format=True)

df = df.stack().to_frame()
df = df.reset_index(level=1)
df.columns = ['status', 'time']
df = df.sort_values('time')
df['counter'] = np.nan
df = df.reset_index().drop('index', axis=1)



counter = 0

for index, row in df.iterrows():

    if row['status'] == 'Start_Time':
        counter += 1
    else:
        counter -= 1
    df.loc[index, 'counter'] = counter
print(df[df.counter == df.counter.max()])

