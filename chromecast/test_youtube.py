# utilisation youtube
from __future__ import print_function
import time
import pychromecast
from pychromecast import youtube

device = pychromecast.get_chromecast(friendly_name="chromecastsalon")
youtube.play_youtube_video("S1HKmK7aOEA",cast=device)

