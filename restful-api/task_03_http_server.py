import http.server
import socketserver
import json

class MyHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """
    HTTP request handler class that handles GET requests for '/data', '/status', and undefined endpoints.
    """
    def do_GET(self):
        """
        Handles GET requests. Responds with JSON data for '/data' endpoint, 'OK' for '/status' endpoint,
        and 'Not Found' for undefined endpoints.
        """
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(bytes('Hello, this is a simple API!', "utf-8"))

        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(bytes(json.dumps(data), "utf-8"))

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(bytes('OK', "utf-8"))

        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(bytes(json.dumps(info), "utf-8"))

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(bytes('404 Not Found', "utf-8"))

def run(server_class=http.server.HTTPServer, handler_class=MyHTTPRequestHandler):
    """
    Starts the HTTP server with the specified server class and request handler class.
    """
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

run()
