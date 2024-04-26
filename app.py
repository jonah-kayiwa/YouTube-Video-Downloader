from pytube import YouTube
from sys import argv #argv takes all commands input to the trminal

try:

#input the link here
    url = input("Enter the Youtube link/url: ")
    yt = YouTube(url)#creates an object from the  youtube link

#lets run a fun test
    print("Title:", yt.title) #this is meant to print the title of the youtube video in the terminal
    print("View:", yt.views) #this is meant to print out the number of views of the video
#print("Duration", yt.duration)

#Lets download the highest quality of the video
    yd = yt.streams.get_highest_resolution()
    yd.download()#this is where you input the folder to which you want the video to download

    print ("Downloaded Succesfully!")

except Exception as e:
    print("Oops, an error occured:", str(e))