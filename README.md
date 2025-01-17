# ActivityNet-Video-Downloader

This simple script is for downloading videos of ActivityNet dataset by parsing URLs from given .json file. Therefore, it is required to download the related .json file [here](http://activity-net.org/download.html).

## Using activityNetDownloader

1. Run the script to download videos from YouTube
	``` bash
	python activityNetDownloader.py
	```

2. Run `prepare_data.ipynb` to:
   * check downloaded videos
   * sample videos 
   * resize videos to 256 (not used if slicing frames)
   * extract raw frames
   * prepare annotations

This repo is prepared based on the instructions given in [Data Process](https://github.com/whwu95/MVFNet/blob/main/data_process/DATASETS.md) and [Text4Video](https://github.com/whwu95/Text4Vis/tree/main).
