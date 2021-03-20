import sqlite3
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument("price",type=float, required=True, help="This Field cant be left blank.")
    parser.add_argument("store_id",type=float, required=True, help="Every Item Needs a Store ID")

    @jwt_required()
    def get(self,name):
        print("!"*100)
        item = ItemModel.find_by_name(name)
        print(item)
        print("!"*100)
        if item:
            return item.json()
        return {"Message":"Item Not Found"},404
        
    def post(self,name):
        
        if ItemModel.find_by_name(name):
            # print("!"*30)
            # print(self.find_by_name(name))
            # print("!"*30)
            return {"Message":"Item with name {} already exists in database.".format(name)},400# in case something is wrong with request.
        
        data = Item.parser.parse_args()
        # update_item = {"name":name, "price":data["price"]}
        update_item = ItemModel(name,data['price'],data['store_id'])
        try:
            update_item.save_to_db()
        except Exception as error:
            print(error)
            return {"Message": "Could Not add {}".format(update_item)},500 #internal server error
        return update_item.json(), 201 #successful request
    
    def put(self,name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        
        if item is None:
            # item = ItemModel(name,data['price'],data['store_id'])
            item = ItemModel(name, **data)
        else:
            item.price = data['price']
        
        item.save_to_db()
        return item.json(), 201
        
    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        
        return {"message":"Item Deleted"}

class ItemList(Resource):
    def get(self):
        # return {"ITEMLIST":[entry.json() for entry in ItemModel.query.all()]}
        # using lambda function
        print("getting ItemList")
        return list(map(lambda x:x.json(), ItemModel.query.all()))