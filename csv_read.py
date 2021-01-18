import pandas
file = r"C:\Users\Administrator\Documents\6.csv"


def file_read():
    df  = pandas.read_csv(file,index_col=0,usecols=['CompanyName'])
    cmpList = list(df.index)
    #print(cmpList[298749])
    #print(len(cmpList[431027:700000]))
    return cmpList
    
file_read()