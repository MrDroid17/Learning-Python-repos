import urllib.request

def read_text():
    quotes = open("/home/dell/projectDevelopment/webDev/py-programming/learning-python/quotes.txt")
    content = quotes.read()
    print(content)
    quotes.close()
    profanity_check(content)

def profanity_check(text):
  
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+ text)
    res = connection.read()
    print(res)
    code = connection.code   
    connection.close()
    

    
    
  
read_text()    
