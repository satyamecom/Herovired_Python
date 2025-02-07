from flask import Flask,jsonify,request

app=Flask(__name__)

@app.route('/hello', methods=["GET"])
def hello():
    return jsonify({"msg":"Hello world..!"})

@app.route("/contact/<string:name>",methods=["GET"])
def contact(name):
    return name

@app.route('/about',methods=["POST","PUT","GET"])
def about():
    data=request.get_json()
    # print(data)
    # print(data["name"])
    # print(type(data))
    # print(type(data["name"]))
    # print(type(data["age"]))
    if data["age"] > 18:
        return "Eligible"
    else:
        # return data["name"]
        return "Not Eligible"

if __name__ == "__main__":
    app.run(debug=True,port=5000)