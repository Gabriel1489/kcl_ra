from http.server import BaseHTTPRequestHandler, HTTPServer
import os 


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            file_path = f"{os.getcwd()}/index.html" #This is current working directory, which gets the index.html 
            file = open(file_path, "rb") 
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(file.read())

# Below is the get request, which will print the message from helloworld by calling helloworld.html
        elif self.path == "/helloworld":
            file_path = f"{os.getcwd()}/hello_world.html" # Our server will be calling this html page when we use /helloworld get request and then print the content in the file
            file = open(file_path, "rb") 
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(file.read())

        elif self.path == "/echo": # This is just to ensure that /echo is ONLY for post request, using it for get request will just throw the string 
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write("THIS IS A POST REQUEST. DONT USE IT FOR GET".encode())

    def do_POST(self): # This is a post request, whereas using in PostMan with POST method with /echo, it prints the message which is there is the message string
        if self.path == "/echo":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            message = "Hello, World! Here is a POST response"
            self.wfile.write(bytes(message, "utf8"))


PORT = 8000 # Program starts on 8000 port 
with HTTPServer(('', PORT), handler) as server:
    print("Server started on ", PORT)
    server.serve_forever()
