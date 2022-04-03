import socket
from flask import *
from content import *

ip = socket.gethostbyname(socket.gethostname())
app = Flask("reddit")

set_app(app)
run()

app.run(port=80)
