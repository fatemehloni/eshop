from flask import Flask, Blueprint

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


from mod_User import users

app.register_blueprint(users)

if __name__ == '__main__':
    app.run()
