import http.server

PORT = 8000

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello, this is a simple API!")

        with socketserver.TCPServer(("", PORT), RequestHandler) as httpd:
            print("Serving on port, {PORT}")
            httpd.serve_forever()
            
            
        