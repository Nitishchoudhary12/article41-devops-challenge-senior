from flask import Flask, jsonify, request
from datetime import datetime


app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_time_info():

  """
  Returns the current UTC timestamp and the client's IP address in JSON format.
  Uses 'X-Forwarded-For' if available, otherwise falls back to remote_addr.
  Timestamp is formatted as 'DD-MM-YYYY HH:MM:SSZ' in UTC.
  """

  client_ip = request.headers.get("X-Forwarded-For", request.remote_addr)
  timestamp_utc = datetime.utcnow().strftime("%d-%m-%Y %H:%M:%S") + "Z"

  response = {
    "timestamp": timestamp_utc,
    "ip": client_ip
  }

  return jsonify(response), 200

# Run the Flask app on all interfaces, port 5050
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5050)