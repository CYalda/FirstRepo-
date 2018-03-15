import pyautogui as pg
import webbrowser

videos = {"https://www.youtube.com/watch?v=fsT5SyBLlIg","https://www.youtube.com/watch?v=8P0aaIOnYiE"}

music = {"https://www.spotify.com/us/","https://soundcloud.com/"}

news = {"https://www.nytimes.com/","https://www.washingtonpost.com/"}

answer = pg.prompt (
"""
Which Would you rather do?
a)Watch videos
b)Listen to music
c)Read the news 

"""
    )

if answer == "A":
    for i in videos:
        webbrowser.open(i)
elif answer == "B":
    for i in music:
        webbrowser.open(i)
elif answer == "C":
    for i in news:
        webbrowser.open(i)
    
