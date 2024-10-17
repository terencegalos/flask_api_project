from flask import Blueprint, request, jsonify, abort
from flask.views import MethodView
from myapp import db, app
from myapp.product.models import Product



catalog = Blueprint('catalog',__name__)

@catalog.route('/')
@catalog.route('/home')
def home():
    return 'Welcome to the catalog home'


class ProductView(MethodView):
    
    def get(self,id=None,page=1):
        if not id:
            products = Product.query.paginate(page=page,per_page=10).items
            res = {}
            for product in products:
                res[product.id] = {
                    'name':product.name,
                    'price':str(product.price),
                }
        else:
            product = Product.query.filter_by(id=id).first()
            if not product:
                abort(404)
            res = {
                'name':product.name,
                'price':str(product.price),
            }
        return jsonify(res)
    
    
        
    def post(self):
        name = request.form['name']
        price = request.form['price']
        product = Product(name,price)
        db.session.add(product)
        db.session.commit()
        return jsonify({product.id:{
            'name':product.name,
            'price':str(product.price),
        }
        })
        
    def put(self,id):
        product = Product.query.filtery_by(id=id).first()
        if not product:
            abort(404)
        name = request.form['name']
        price request.form['price']
        product.name = name
        product.price = price
        db.session.commit()
        return jsonify({
        'id':product.id,
        'name':product.name,
        'price':str(product.price),
        })

    def delete(self,id):
        product = Product.query.filter_by(id=id).first()
        if not product:
            abort(404)
        db.session.delete(product)
        db.session.commit()
    return jsonify({
        'message':'Product deleted successfully'
    })
            
            
            
product_view = ProductView.as_view('product_view')
app.add_url_rule(
    '/product/',view_func=product_view,methods=['GET','POST']
)
app.add_url_rule(
    '/product/<int:id>',view_func=product_view,methods=['GET','PUT','DELETE']
)