from http.server import BaseHTTPRequestHandler,HTTPServer

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path=="/":
            self.path="/index.html"
        try:
            f=open(self.path[1:]).read()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(bytes(f, "utf-8"))
        except:
            f="not found"
            self.send_error(400,f)

ADD=("localhost",8080)
httpd=HTTPServer(ADD,Server)
print("http://{}:{}".format(ADD[0],ADD[1]))
httpd.serve_forever()