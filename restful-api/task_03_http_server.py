import http.server
import json
import logging

class MyHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """
    HTTP request handler class that handles GET requests for '/' ,'/data', '/status', '/info' and undefined endpoints.
    """

    def do_GET(self):
        """
        Handles GET requests. Responds with JSON data for '/data' and '/info' endpoints,
        'OK' for '/status' endpoint, and 'Not Found' for undefined endpoints.
        """
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')

        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'OK')

        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(info).encode())

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Endpoint not found')

def run(server_class=http.server.HTTPServer, handler_class=MyHTTPRequestHandler):
    """
    Starts the HTTP server with the specified server class and request handler class.
    """
    logging.basicConfig(level=logging.INFO)
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    logging.info("Starting server on port 8000...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info("Stopping server.")

if __name__ == '__main__':
    run()
