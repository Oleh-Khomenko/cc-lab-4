from flask import Flask, Response
from random import random
from prometheus_client import CollectorRegistry, Gauge, generate_latest

app = Flask(__name__)

registry = CollectorRegistry()
gs = [Gauge(f'generated_metric_{i + 1}', f'Generated metric {i + 1}', registry=registry) for i in range(10)]

@app.route('/metrics')
def metrics():
    for g in gs:
        g.set(round(random() * 100))
    return Response(generate_latest(registry), mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9091)
