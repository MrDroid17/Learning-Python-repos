from urllib.request import urlopen, HTTPError

def read_text():
    quotes = open("/home/dell/projectDevelopment/webDev/py-programming/learning-python/quotes.txt")
    content = quotes.read()
    print(content)
    quotes.close()
    profanity_check(content)

def profanity_check(text):
    try:
        connection = urlopen("http://www.wdylike.appspot.com/?q="+ text)
        res = connection.read()
        print(res)
        code = connection.code   
        connection.close()
    
    except HTTPError as error:
        code = error.code 

read_text()    
