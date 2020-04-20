from flask import Flask

from config import config

# If running as a package replace by a relative import:
# from .config import config

app = Flask(__name__)

try:
    config.load_json("config.json")
except FileNotFoundError:
    print("config.json file not found. Using the default configuration")

# Update Flask config
app.config.update(
    SECRET_KEY=config["secret"]
)

print("Connecting to database %s" % config["db"])


@app.route('/')
def hello_world():
    return config["text"]


def main():
    app.run('0.0.0.0', debug=False)


if __name__ == '__main__':
    main()
