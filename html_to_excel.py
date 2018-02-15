import pandas as pd
url = 'http://www.moia.gov.il/Hebrew/InformationAndAdvertising/Statistics/Documents/2010/OLIM1A.htm'

for i, df in enumerate(pd.read_html(url)):
    df.to_excel('olim2010_%s.xls' % i)

