def read_text():
    quotes = open("/home/dell/projectDevelopment/webDev/py-programming/learning-python/quotes.txt")
    content = quotes.read()
    print(content)
    quotes.close()

read_text()    
