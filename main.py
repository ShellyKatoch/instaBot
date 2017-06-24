import requests
from keys import *
import urllib

BASE_URL = "https://api.instagram.com/v1/"


def self_info():
  request_url = (BASE_URL + 'users/self/?access_token=%s') % (ACCESS_TOKEN)
  print 'Requesting info for:' + request_url
  my_info = requests.get(request_url).json()
  print 'My info is:\n', my_info['data']['username']

#self_info()

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


 def get_like_list(insta_username):
   post_id = get_post_id(insta_username)
   request_url = (BASE_URL + '/media/%s/likes?access_token=%s') % (post_id, ACCESS_TOKEN)
   print 'Requesting data for: %s' % (request_url)
   likes_info= requests.get(request_url).json()
   if likes_info['meta']['code']==200:
    if len(likes_info['data']):
       for x in range(0 ,len(likes_info['data'])):
         print likes_info['data'][x]['username']
       else:
         print 'no user has liked the post yet!'
    else:
      print 'status code other than 200 received!'

 get_like_list('ishita')


 def like_a_post(insta_username):
          media_id= get_post_id(insta_username)
          request_url=(BASE_URL+ 'media/%s/likes')%(media_id)
          payload={"access_token":ACCESS_TOKEN}
          print 'post request url:%s'%(request_url)
          post_a_like= requests.post(request_url,payload).json()

          if post_a_like['meta']['code']== 200:
           print 'like was successfull !'
          else:
            print 'your like was unsuccessful.Try again !'

   like_a_post('ishita')

 def post_a_comment(insta_username):
     media_id = get_post_id(insta_username)
     comment_text= raw_input("your comment:")
     request_url = (BASE_URL + 'media/%s/comments') % (media_id)
     payload = {"access_token": ACCESS_TOKEN ,"text": comment_text}
     print 'post request url:%s' % (request_url)
     make_comment = requests.post(request_url, payload).json()

     if make_comment['meta']['code'] == 200:
         print 'Successfully added a new comment!'
     else:
         print 'Unable to add comment.Try again'

 post_a_comment('prashant')


 def delete_negative_comment(insta_username):
     media_id = get_post_id(insta_username)
     request_url = (BASE_URL + 'media/%s/cooments/?access_token=%s') % (media_id)

     print 'GET request url:%s' % (request_url)
     comment_info = requests.post(request_url).json()

     if comment_info['meta']['code'] == 200:
         if len(comment_info['data']):

           print 'like was successfull !'
         else:
           print 'There are no existing comments on the post!'
     else:
       print 'Status code other than 200 received'

 delete_negative_comment('ishita')















