import urllib.request
import ssl
import time
import pandas as pd
from urllib.error import HTTPError

def reverse_md5(md5_str,sleep=0):
    time.sleep(sleep)
    gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    try:
        contents = str(urllib.request.urlopen("https://md5.gromweb.com/?md5="+md5_str,context=gcontext).read())
    except:
        return "couldnt preform the query"
    start = contents.find('was succesfully reversed into the string:<br/>\\n            <em class="long-content string">')
    end = contents.find('</em></p>\\n        <p>Feel free to provide some other MD5 hashes you would like to try to reverse.')
    if start == -1 or end == -1:
        return "Provided MD5 hash could not be reversed into a string: no reverse string was found."    
    return contents[start+92:end]
df = pd.read_csv("/Users/yyarom/Downloads/bq-results-20230828-132823-1693229330705.csv")
for j,i in enumerate(df['ja3s']):
    if j > -1:
        try: 
            t = reverse_md5(i)
        except HTTPError:
            print("reset")
            time.sleep(60)
            t = reverse_md5(i)
        print(j)
        if t != "Provided MD5 hash could not be reversed into a string: no reverse string was found.":
            print(t)
            res.append(t)
