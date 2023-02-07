import threading
import time
from flask import Flask

app = Flask(__name__)
value = 0

def read_function():
    global value
    while True:
        value+=1
        time.sleep(1)

x = threading.Thread(target = read_function, args = ())
x.start()


@app.route("/")
def hello_world():
    return str(value)

if __name__ == '__main__':
    app.run()    