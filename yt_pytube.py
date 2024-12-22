import pytube

# Ask the user to enter url of YouTube video
video_url = input('Enter YouTube video URL: ')

# Create an instance of YouTUbe video
video_instance = pytube.YouTube(video_url)
stream = video_instance.streams.filter(progressive=True, file_extension='mp4')
# stream = video_instance.streams.get_highest_resolution()

#download
stream.download()