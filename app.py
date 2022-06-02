from flask import Flask

app=Flask(__name__)

@app.route("/hello",methods=['GET'])
def hello():
    return "Hello Word, This is cinmoy"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)
