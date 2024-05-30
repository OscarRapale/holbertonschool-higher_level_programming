import http.server
import json
import logging

class MyHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """
    HTTP request handler class that handles GET requests for '/' ,'/data', '/status', '/info' and undefined endpoints.
    """

    def _set_headers(self, status_code, content_type):
        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def _respond(self, content, content_type='text/plain', status_code=200):
        self._set_headers(status_code, content_type)
        self.wfile.write(content)

    def do_GET(self):
        """
        Handles GET requests. Responds with JSON data for '/data' and '/info' endpoints,
        'OK' for '/status' endpoint, and 'Not Found' for undefined endpoints.
        """
        if self.path == '/':
            self._respond(b'Hello, this is a simple API!')

        elif self.path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}
            self._respond(json.dumps(data).encode(), content_type='application/json')

        elif self.path == '/status':
            self._respond(b'OK')

        elif self.path == '/info':
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self._respond(json.dumps(info).encode(), content_type='application/json')

        else:
            self._respond(b"Endpoint not found", status_code=404)

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
    except Exception as e:
        logging.error(f"Server error: {e}")
    finally:
        httpd.server_close()
        logging.info("Stopping server.")

if __name__ == '__main__':
    run()
