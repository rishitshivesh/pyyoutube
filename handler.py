from pytube import YouTube
import pick

def downloadHighest(youtubeObject):
  youtubeObject = youtubeObject.streams.get_highest_resolution()
  try:
      youtubeObject.download()
  except:
    print("There has been an error in downloading your youtube video")
  print("This download is complete!")

def downloadLowest(youtubeObject):
  youtubeObject = youtubeObject.streams.get_lowest_resolution()
  try:
      youtubeObject.download()
  except:
    print("There has been an error in downloading your youtube video")
  print("This download is complete!")

def getAudio(youtubeObject):
  youtubeObject = youtubeObject.streams.get_audio_only()
  try:
    print("Grab your audio file at \n\n"+youtubeObject.url)
  except:
    print("There has been an error in downloading your youtube video")
  print("This download is complete!")


if __name__ == "__main__":
    print("Welcome to the youtube downloader!\n")
    link = input("Put your youtube link here!! URL: ")
    ytObj = YouTube(link)
    options = ["Download the highest resolution", "Download the lowest resolution", "Download the audio", "Exit"]
    option, choice = pick.pick(options, ytObj.title, indicator='=>', default_index=0)
    if choice == 0:
        downloadHighest(ytObj)
    elif choice == 1:
        downloadLowest(ytObj)
    elif choice == 2:
        getAudio(ytObj)
    elif choice == 3:
        exit()
    else:
        print("Invalid choice")
