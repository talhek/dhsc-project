import pandas as pd
import goslate as tr
import urllib2

df = pd.read_excel("myfile_0.xls")
gs = tr.Goslate()
#print(gs.translate(df[0][0],'en'))

for x, row in df.iterrows():
    for i in range(0, len(row)-1):
        var = df[i][x]
        if type(var) is unicode:
            try:
                trans = gs.translate(var,'en')
                df.loc[i,x] = trans
            except urllib2.HTTPError as err:
                df.loc[i,x] = -1
# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('output.xls', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

# Get the xlsxwriter objects from the dataframe writer object.
workbook  = writer.book
worksheet = writer.sheets['Sheet1']

print(worksheet)