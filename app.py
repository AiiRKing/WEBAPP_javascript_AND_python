import execjs
import subprocess
from flask import Flask, render_template
from flask import Flask, jsonify
import plotly.graph_objects as go
from flask import Flask, render_template
from flask_socketio import SocketIO


# Define JavaScript code
js_code = """
function add(a, b) {
    return a + b;
}
"""
# Create a JavaScript context
ctx = execjs.compile(js_code)

# Call the JavaScript function
result = ctx.call("add", 3, 5)
print(result)  # Output: 8

# Run the JavaScript file using Node.js
result = subprocess.run(["node", "script.js"], capture_output=True, text=True)

# Print the output
print(result.stdout)  # Output: 8

#Using JavaScript in Web Development (Flask/Django)
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/data.json")
def get_data():
    return jsonify({"message:"})

# Python script to generate a Plotly chart
fig = go.Figure(data=[go.Bar(y=[2, 3, 1])])
fig.show()  # Opens an interactive JavaScript-based chart in the browser

#Flask app with WebSocket support
app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def home():
    return render_template("index.html")

@socketio.on("message")
def handle_message(data):
    print("Received message:", data)
    socketio.emit("response", {"message": "Hello from Python!"})

if __name__ == "__main__":
    app.run(debug=True)
