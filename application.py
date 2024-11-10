from flask import Flask, render_template
import os
from flask_bootstrap import Bootstrap
from flask_restful import Api
from api import CategoryAPI, ProductAPI

# Initialize the Flask app
app = Flask(__name__, static_url_path='/static')

# Configure the app
current_dir = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = 'static/assets/'
app.config['SECRET_KEY'] = os.urandom(24)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# Initialize Flask extensions
Bootstrap(app)
api = Api(app)

# Add your API resources
api.add_resource(CategoryAPI, '/api/category', '/api/category/<int:category_id>')
api.add_resource(ProductAPI, '/api/product', '/api/product/<int:product_id>')

@app.route('/carbon-calculator')
def carbon_calculator():
    return render_template('Carboncalc.html')



# Import other routes (authentication, user, admin, etc.)
from authentication import *
from admin_routes import *
from user_routes import *

# Start the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
