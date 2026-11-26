from flask import Flask, request, render_template_string
import socket

app = Flask(__name__)

form_html = """
<!doctype html>
<title>Send Message</title>
<h1>Send a message to the socket server</h1>
<form method="post">
  <textarea name="message"></textarea><br>
  <input type="submit" value="Send">
</form>
{% if response %}
  <h2>Response from socket server:</h2>
  <p>{{ response }}</p>
{% endif %}
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    response = None
    if request.method == 'POST':
        message = request.form['message']
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('socket_server', 12345))
        client_socket.sendall(message.encode())
        response = client_socket.recv(1024).decode()
        client_socket.close()
    return render_template_string(form_html, response=response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)