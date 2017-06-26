import requests
from keys import *
import urllib

BASE_URL = "https://api.instagram.com/v1/"


def self_info():
  request_url = (BASE_URL + 'users/self/?access_token=%s') % (ACCESS_TOKEN)
  print 'Requesting info for:' + request_url
  my_info = requests.get(request_url).json()
  print 'My info is:\n', my_info['data']['username']

self_info()















