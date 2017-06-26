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


def get_user_id(username):
  request_url = (BASE_URL + 'users/search?q=%access_token=%s') % (username, ACCESS_TOKEN)
  print 'Get request url: %s' % (request_url)

  user_info=requests.get(request_url).json()
  if user_info['meta']['code'] == 200:
    if len(user_info['data'])>0:
      return user_info['data'][0]['id']
    else:
       print ""

       return None
  else:
    print 'status code other than 200 recieved'
exit()

id_var= get_user_id('shelly katoch')


def get_users_post(username):
  user_id = get_user_id(username)
  request_url = (BASE_URL + 'users/%s/media/recent?access_token=%s') % (user_id,ACCESS_TOKEN)
  print '//Requesting media for: %s' % (request_url)

  recent_post = requests.get(request_url).json()
  if recent_post['meta']['code'] == 200:
    if len(recent_post['data'])>0:
      image_name = recent_post['data'][0]['id'] + ".jpeg"
      image_url = recent_post['data'][0]['images']['standard_resolution']['url']
      urllib.urlretrieve(image_url, image_name)
    else:
      print "There is no recent post!"
  else:
    print "Status code other than 200 received!"

get_users_post('ishita')

def get_post_id(insta_username):
 user_id= get_user_id(insta_username)
 request_url=(BASE_URL + 'users/%s/media/recent?access_token=%s') % (user_id,ACCESS_TOKEN)
 print 'Requesting data for: %s' % (request_url)

 user_media= requests.get(request_url).json()
 if user_media['meta']['code']==200:
   if len(user_media['data']):
     return user_media['data'][0]['id']
   else:
     print 'post does not exists:'
 else:
   print 'Status code other than 200 received!'
   return None

 get_post_id('ishita')













