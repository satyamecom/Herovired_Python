from logging import debug
from flask import Flask, json,jsonify,request

app=Flask(__name__)

@app.route("/ci",methods=["POST"])
def compund_interest():
    data=request.get_json()
    calculate=data["pr_amt"]*(1+(data["rate_int"]/100))**data["time"]
    return jsonify({"compund interest" : calculate})

if __name__ == "__main__":
    app.run(debug=True,port=3000)