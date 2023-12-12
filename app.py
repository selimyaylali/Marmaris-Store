from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from models import Product

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)


@app.route('/search')
def search():
    query = request.args.get('query', '')
    products = Product.query.filter(
        db.or_(
            Product.description.ilike(f'%{query}%'),
            Product.product_no.ilike(f'%{query}%'),
            Product.category.ilike(f'%{query}%')
        )
    ).all()

    return render_template('search_result.html', products=products, query=query)


@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product_detail.html', product=product)



if __name__ == '__main__':
    app.run(debug=True)

with app.app_context():
    db.create_all()

    if Product.query.count() == 0:
        products_list = [
            {'product_no': 'P001', 'description': 'Balenciaga T-shirt', 'price': 19.99,
             'image_file': 'balenciaga_tshirt.png',
             'category': 'Apparel'},
            {'product_no': 'P002', 'description': 'Axel Arigato Sneaker', 'price': 89.99,
             'image_file': 'axel_arigato.png',
             'category': 'Footwear'},
            {'product_no': 'P003', 'description': 'Bacarat Perfume', 'price': 49.99,
             'image_file': 'bacarat_perfume.png',
             'category': 'Accessories'},
            {'product_no': 'P004', 'description': 'Playstation 5 Slim', 'price': 199.99,
             'image_file': 'playstation5_slim.png',
             'category': 'Electronics'},
            {'product_no': 'P005', 'description': 'Iphone 15', 'price': 59.99, 'image_file': 'iphone15.png',
             'category': 'Electronics'},
            {'product_no': 'P006', 'description': 'Beymen Towel', 'price': 29.99,
             'image_file': 'beymen_towel.png',
             'category': 'Accessories'},
            {'product_no': 'P007', 'description': 'Prada T-Shirt', 'price': 24.99,
             'image_file': 'prada_tshirt.png',
             'category': 'Apparel'},
            {'product_no': 'P008', 'description': 'Dolce Gabbana Tshirt', 'price': 39.99,
             'image_file': 'dolcegabbana_tshirt.png',
             'category': 'Apparel'},
            {'product_no': 'P009', 'description': 'Quantum Watch', 'price': 34.99,
             'image_file': 'quantum_watch.png',
             'category': 'Accessories'},
            {'product_no': 'P010', 'description': 'Ralph Lauren Sweater', 'price': 14.99,
             'image_file': 'rl_sweater.png',
             'category': 'Apparel'}
        ]

        for product in products_list:
            new_product = Product(
                product_no=product['product_no'],
                description=product['description'],
                price=product['price'],
                image_file=product['image_file'],
                category=product['category']
            )
            db.session.add(new_product)

        db.session.commit()
