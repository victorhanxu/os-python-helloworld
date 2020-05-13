from flask import Flask
application = Flask(__name__)

@application.route("/")
def root():
    return "Hello! This is an Openshift Python App! path: root"

@application.route("/hello")
def hello():
    return "Openshift Python App! path: hello"


if __name__ == "__main__":
    application.run()
