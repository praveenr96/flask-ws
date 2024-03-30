from flask import Flask, request, jsonify
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)


@app.route("/webhooks/answer")
def answer_call():
    ncco = [
        {
            "action": "talk",
            "text": "We will now connect you to the echo server, wait a moment then start speaking.",
        },
        {
            "action": "connect",
            "from": "Vonage",
            "endpoint": [
                {
                    "type": "websocket",
                    "uri": f"wss://{request.host}/socket",
                    "content-type": "audio/l16;rate=16000",
                }
            ],
        },
    ]

    return jsonify(ncco)


if __name__ == "__main__":
    docker_deploy = False
    if docker_deploy:
        app.run(port = 80, host = "0.0.0.0")
    else:
        app.run(port = 3000)
