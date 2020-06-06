from urllib import request


url = "https://home.cnblogs.com/u/1094968"
headers = {
    "Accept": "text/plain, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36 Edg/83.0.478.44",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cookie":""
    }

req = request.Request(url,headers=headers)
repsonse = request.urlopen(req)
print(repsonse.read().decode())