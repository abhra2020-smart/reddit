from utils import read_template

app: any


def set_app(a):
    global app
    app = a


def run():
    @app.route("/")
    def home():
        return read_template("index.html")
