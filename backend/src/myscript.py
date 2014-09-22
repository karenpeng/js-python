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

#well, the api is banned:(

import threading
import webbrowser
import SimpleHTTPServer
import SocketServer

FILE = '../../index.html'

PORT = 7000

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_POST(self):
      content_len = int(self.headers.getheader('content-length', 0))
      post_body = self.rfile.read(content_len)
      #print post_body
      sendImg(post_body)

def open_browser():
    """Start a browser after waiting for half a second."""
    def _open_browser():
        webbrowser.open('http://localhost:%s/%s' % (PORT, FILE))
    thread = threading.Timer(0.5, _open_browser)
    thread.start()

def start_server():
    """Start the server."""
    server_address = ("", PORT)
    server = BaseHTTPServer.HTTPServer(server_address, TestHandler)
    server.serve_forever()

if __name__ == "__main__":
    open_browser()
    start_server()

#Handler = ServerHandler

#httpd = SocketServer.TCPServer(("", PORT), Handler)

#print "serving at port", PORT
#httpd.serve_forever()