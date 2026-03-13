import uuid
from flask import request
from flask_smorest import Blueprint, abort
from flask.views import MethodView


from schemas import StoreSchema

blp=Blueprint("Stores",__name__,description="Operations on Stores")

@blp.route("/store")
class Store(MethodView):
    @blp.arguments(StoreSchema)
    @blp.response(201,StoreSchema)
    def post(self,data):
        
        store_id=uuid.uuid4().hex
        new_store={**data,"id":store_id}
        stores[store_id]=new_store
        return new_store,201
    def get(self):
        return {"stores":stores}
    
@blp.route("/store/<string:store_id>")
class StoreById(MethodView):
    @blp.response(200,StoreSchema)
    def get(self,store_id):
        try:
            return stores[store_id]
        except KeyError:
            abort(404,message="Store not found")
    