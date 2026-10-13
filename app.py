
from http.server import HTTPServer, BaseHTTPRequestHandler
import os


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = b"Hello from my DevOps application!\n"

        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        print(f"{self.address_string()} - {format % args}", flush=True)


if __name__ == "__main__":
    host = os.getenv("APP_HOST", "0.0.0.0")
    port = int(os.getenv("APP_PORT", "8000"))

    server = HTTPServer((host, port), Handler)
    print(f"Server listening on {host}:{port}", flush=True)
    server.serve_forever()
