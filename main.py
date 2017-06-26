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

def get_own_post():
  request_url = (BASE_URL + 'users/self/media/recent?access_token=%s') % (ACCESS_TOKEN)
  print 'Requesting media for: %s' % (request_url)

  recent_post = requests.get(request_url).json()
  if recent_post['meta']['code'] == 200:
    if len(recent_post['data'])>0:
      image_name= recent_post['data'][0]['id']+".jpeg"
      image_url= recent_post['data'][0]['images']['standard_resolution']['url']
      urllib.urlretrieve(image_url,image_name)
    else:
      print "There is no recent post!"
  else:
    print "Status code other than 200 received!"


get_own_post()












