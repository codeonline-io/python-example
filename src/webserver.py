
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "0.0.0.0"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.end_headers()
    self.wfile.write(bytes("Hello World", "utf-8"))

if __name__ == "__main__":        
  webServer = HTTPServer((hostName, serverPort), MyServer)
  print("Webserver is listening on https://code.codeonline.io/proxy/%s" % (serverPort))

  try:
    webServer.serve_forever()
  except KeyboardInterrupt:
    pass

  webServer.server_close()
  print("Server stopped.")