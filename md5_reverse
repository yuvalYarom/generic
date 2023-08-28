import urllib.request
import ssl
import time
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
