from marshmallow import Schema  ,fields 

class PlainItemSchema(Schema):
    id=fields.Str(dump_only=True)
    name=fields.Str(required=True)
    price=fields.Float(required=True)
    quantity=fields.Int(required=True)

class PlainStoreSchema(Schema):
    id=fields.Str(dump_only=True)
    name=fields.Str(required=True)


class ItemSchema(PlainItemSchema):
    store_id = fields.Str(required=True)
    store=fields.Nested(PlainStoreSchema(), dump_only=True)

class StoreSchema(PlainStoreSchema):
    items=fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
    















class ItemUpdateSchema(Schema):
    name=fields.Str()
    price=fields.Float()
    quantity=fields.Int()

class ItemDeleteSchema(Schema):
    item_id=fields.Str(required=True)


    

