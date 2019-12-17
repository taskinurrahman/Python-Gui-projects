

import requests

url="http://example.com"
res=requests.get(url)



print(res.ok)

fp=open("text.txt","w")
fp.write(res.text)
fp.close()

