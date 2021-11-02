import requests
import pandas as pd

class ex05:
    
    def get_file(self, url, filename):
        download = requests.get(url)
        url_content = download.content
        csv = open(filename, 'wb')
        csv.write(url_content)
        csv.close()
   

    def make_df(self, filename):
        df = pd.read_csv(filename, sep=';')
        return df
    
    def return_status(self, marital_stat, df):
        df2 = df[df['CIVILSTAND'].isin([marital_stat])]
        return df2