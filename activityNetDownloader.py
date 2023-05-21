import os
import json
from pprint import pprint
# from tqdm import tqdm
from pytube import YouTube


# specify download directory
directory = '../data/ActivityNet_200/'
videoCounter = 0

# open json file
with open('activity_net.v1-3.min.json') as data_file:    
    data = json.load(data_file)

# take only video informations from database object
videos = data['database']

total_videos = len(videos)
# iterate through dictionary of videos
for id, key in enumerate(videos):
	# take video
	video = videos[key]

	# find video subset
	subset = video['subset']

	# find video label
	annotations = video['annotations']
	label = ''
	if len(annotations) != 0:
		label = annotations[0]['label']
		label = '/' + label.replace(' ', '_')

	# create folder named as <label> if does not exist
	label_dir = directory + subset + label
	if not os.path.exists(label_dir):
		os.makedirs(label_dir)
		print('Created directory: ' + label_dir)

	# take url of video
	url = video['url']	
	try:
		# Create a YouTube object with the provided URL
		yt = YouTube(url)
		
		# Filter the available video streams to get the highest resolution
		video = yt.streams.get_highest_resolution()
		
		# Download the video to the specified output path, rename the video as the key
		video.download(label_dir, key+'.mp4')
		videoCounter += 1		
		print("{}/{}/{} Video downloaded successfully! {} {}".format(id+1, total_videos, videoCounter, key, url))
		

	except Exception as e:
		print("{}/{}/{} Error: {}! {} {}".format(id+1, total_videos, videoCounter, str(e), key, url))


	stop


print('Downloaded ' + str(videoCounter) + ' videos.')
