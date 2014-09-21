from snapchat import Snapchat

s = Snapchat('snapfaceface', 'slapFace321')

import base64
def sendImg(dataURL):
   jpeg_recovered = base64.decodestring(dataURL)
   f = open("temp.jpeg", "w")
   f.write(jpeg_recovered)
   f.close()
   media_id = s.upload(Snapchat.MEDIA_IMAGE, 'temp.jpeg')
   s.send(media_id, 'pennypunk')

# Get all snaps
#snaps = s.get_snaps()

# Download a snap
#s.get_media(snap['id'])

# Clear snapchat history
#s.clear_feed()