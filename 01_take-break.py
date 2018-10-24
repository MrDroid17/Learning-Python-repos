import webbrowser
import time

# open default browser to play video
x=0
print("program started at: "+ time.ctime())

# use while loop
# notice that indentation matters like the line below while
while x < 3:
    time.sleep(10)
    print("take ",x+1," break at: "+ time.ctime())
    webbrowser.open("https://www.youtube.com/watch?v=7wtfhZwyrcc")
    x+=1
