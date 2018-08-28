import webbrowser
import time
loops = 0

while (loops < 3):
    time.sleep(10)
    webbrowser.open("https://www.google.com")
    loops = loops + 1


