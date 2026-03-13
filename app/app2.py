import uuid
from flask import Flask , request, jsonify
from flask_smorest import abort
from db import stores,items

app =Flask(__name__)

#1 - Get all stores
@app.get("/stores")
def get_stores():
    return {"stores":stores}

#2 - Get a store by id
@app.get("/stores/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        abort(404,message="Store not found") # flask smorest bettter way to hanadle errors

#3 - Create a store    
@app.post("/store")
def create_store():
    data=request.get_json()
    store_id=uuid.uuid4().hex
    new_store={**data}
    stores[store_id]=new_store
    return new_store,201

#4 - Create an item
@app.post("/item")
def create_item():
    data=request.get_json()
    if data["store_id"] not in stores:
        return {"message":"Store not found"},404
    item_id=uuid.uuid4().hex
    item={**data,"id":item_id}
    items[item_id]=item
    return item,201

#5 - Get all items
@app.get("/items")
def get_items():
    return {"items":list(items.values())}

#6 - Get an item by id
@app.get("/items/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        return {"message":"Item not found"},404


