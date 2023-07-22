import http.server
import random
from prometheus_client import start_http_server
from prometheus_client import Counter # 1.

# 1. Tracks the number of times "Hello World" has been requested
## Counter is defined as "hello_worlds_total, with the helper string "Hellow Worlds requested" that will show on the /metrics page to show what that metric actually means
REQUESTS = Counter('hello_worlds_total',
        'Hello Worlds requested.')
EXCEPTIONS = Counter('hello_world_exceptions_total',
        'Exceptions serving Hellow World.')

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        REQUESTS.inc() # 1. Call the metric object. inc method increments the counters value by 1
        with EXCEPTIONS.count_exceptions():
            if random.random() < 0.2:
                raise Exception
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello World")

if __name__ == "__main__":
    start_http_server(8000) # Starts up an HTTP server on port 8000 to serve metrics to Prometheus
    server = http.server.HTTPServer(('localhost', 8001), MyHandler)
    server.serve_forever()


#  1 Counters can be used to track errors and unexpected situations. Knowing how errors are trending over time is good for debugging. Knowing the popular features or code paths of an application helps to optimize and allocate dev efforts.