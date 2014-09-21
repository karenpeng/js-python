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

import SimpleHTTPServer
import SocketServer

PORT = 7000

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_POST(self):
      content_len = int(self.headers.getheader('content-length', 0))
      post_body = self.rfile.read(content_len)
      #print post_body
      sendImg(post_body)

Handler = ServerHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()