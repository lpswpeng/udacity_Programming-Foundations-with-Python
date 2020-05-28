"""
work every 2 hours, then take a break to open music on youtube. Total break 3 times
"""

import webbrowser
import time

i = 0
total_break = 3
print("This program started on:" + time.ctime())
while i < total_break:
    time.sleep(2*60*60)
    webbrowser.open("https://www.youtube.com/watch?v=Z2ik7IRkzFU")
    i +=1
