from http.client import HTTPConnection
s = input("Enter Url : ")

conn =HTTPConnection(s)
conn.request("GET", "/")  
result = conn.getresponse()
# retrieves the entire contents.  
contents = result.read() 
print(contents)
