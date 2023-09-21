import re

onclick = "flytopos('door','121.577002','25.039192','qry_addr.png','臺北市信義區廣居里２９鄰松德路２８號','','','33016');"

pattern1 = re.compile(r"\d+\.\d+")
result = pattern1.finditer(onclick)



for i in result:
    get = i.group()
    print(get)