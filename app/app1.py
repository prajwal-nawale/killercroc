from flask import Flask, request, jsonify 

app = Flask(__name__)

todos = [
    {
        "username":1,
        "tasks":[
            {
                "task1":"Complete flask asap",
                "priority":"high"
            },
            {
                "task2":"Create a Portfolio website",
                "priority":"medium"
            },
            {
                "task3":"Learn creating Agents",
                "priority":"Medium"
            }
        ]
    }
]

username={}
todos={
    1:{
        "task1":"Complete flask backend asap",
        "priority":"❌❌❌"
    },
    2:{
        "task2":"Create a MVP hiring platform",
        "priority":"❌❌"
    },
    3:{
        "task3":"Learn creating Agents",
        "priority":"❌❌❌"
    }
}


@app.get("/todos")
def get_todos():
    return {"todos":todos}

@app.post("/todos")
def create_user():
    data=request.get_json()
    a={"username":data["username"],"tasks":[]}
    todos.append(a)
    return {"message":"Username added successfully"},201

@app.post("/todos/<string:username>/task")
def add_task(username):
    data=request.get_json()
    for i in todos:
        if i["username"]==username:
            i["tasks"].append(data)
            return {"message":"Task added successfully"},201
    return {"message":"Username not found"},404

@app.get("/todos/<username>/tasks")
def get_tasks(username):
    for i in todos:
        if i["username"]==username:
            return {"tasks":i["tasks"]}
    return {"message":"Username not found"},404
     


