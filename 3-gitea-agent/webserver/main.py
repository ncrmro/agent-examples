from flask import Flask, request, jsonify
import json
app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify(status='UP'), 200

@app.route('/webhooks/gitea', methods=['POST'])
def gitea_webhook():
    """Gitea webhook endpoint."""
    print("GITEA WEB HOOK")
    data = request.json
    if data is None:
        return jsonify(error='Invalid payload'), 400

    # TODO: Process the Gitea webhook payload
    # Example: log the event
    event_type = request.headers.get('X-Gitea-Event')
    print(f"Received Gitea event: {event_type}, payload: {json.dumps(data)}")

    return jsonify(status='Processed'), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
