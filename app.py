from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
import os

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app=Flask(__name__)
app.secret_key='aman'
uri = os.getenv("DATABASE_URL")
if uri.startswith("postgres://"):    
     uri = uri.replace("postgres://", "postgresql://", 1)
if uri:
    app.config['SQLALCHEMY_DATABASE_URI']= uri
else:
    app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///data.db'
app.config['SQLAlCHEMY_TRACK_MODIFICATIONS']=False
api= Api(app)


jwt=JWT(app, authenticate, identity)

api.add_resource(Store, '/store/<string:name>')   
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')

api.add_resource(UserRegister, '/register')


if __name__=='__main__':
    app.run(port=5000, debug=True)

