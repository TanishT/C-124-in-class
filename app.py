from flask import Flask, jsonify, request
app=Flask(__name__)
app.route("/")
task= [
    {
        'id':1,
        'title':u'Buy Groceries',
        'description':u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done':False,
    },
    {
        'id' : 2,
        'title':u'Learn Python',
        'description': u'Find Python tutorial online',
        'done' : False
    }
]
@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide data"
        }, 400)

    task ={
        'id':tasks[-1]['id']+1,
        'title':request.json['title'],
        'description':request.json.get('description',""),
        'done':False
        }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message":"Taks added succesfully"
    })
@app.route("/get-data")
def get_tasl():
    return jsonify({
        "data":tasks
    })



if(__name__ == "__main__"):
    app.run(debug=True)
