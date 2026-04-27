from flask import Flask, jsonify
from prometheus_client import Counter, Histogram, start_http_server
import time
import threading

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint", "status"],
)

REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "HTTP request latency in seconds",
    ["method", "endpoint"],
)


@app.before_request
def before_request():
    from flask import request
    request._start_time = time.time()


@app.after_request
def after_request(response):
    from flask import request
    latency = time.time() - request._start_time
    REQUEST_COUNT.labels(request.method, request.path, response.status_code).inc()
    REQUEST_LATENCY.labels(request.method, request.path).observe(latency)
    return response


@app.route("/")
def hello():
    return jsonify({"message": "Hello from Skyscrapers!"})


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


def start_metrics_server():
    """Start Prometheus metrics server on a separate port (9090).

    This keeps metrics on an internal port, not exposed via ingress.
    Only Prometheus (via ServiceMonitor) scrapes this port.
    """
    start_http_server(9090)


if __name__ == "__main__":
    start_metrics_server()
    app.run(host="0.0.0.0", port=8080)
else:
    # When running under gunicorn, start metrics server in a thread
    threading.Thread(target=start_metrics_server, daemon=True).start()
