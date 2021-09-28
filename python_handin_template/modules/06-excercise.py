import requests

class TextComparer:
    def __init__(self, url_list):
        return self

    def download(self, url, filename):
        try:
            list = requests.get(url) 
            with open(filename, 'wb') as output:
                output.write(list.content)
            df = pd.read_csv(filename)  
            if(list.status_code == 404):
                raise Exception('Not found')
        except Exception as e:
            print(e)

    def multi_download(self, listOfUrls, file):
        #make threadpool gen


