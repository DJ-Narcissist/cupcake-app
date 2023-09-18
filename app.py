"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify
from models import Cupcake, db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] ='Cakes_for_less'

db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route ('/api/cupcakes', methods = ['GET'])
def get_all_cupcakes():
    cupcakes = Cupcake.query.all()
    cupcakes_data = [{'id': cupcakes.id, 'flavor':cupcake.flavor, 'size' : cupcake.size, 'rating' : cupcake.rating, 'image' : cupcake.image}]

    return jsonify(cupcakes = cupcakes_data)


@app.route('/api/cupcakes/<int:cupcake-id>',  methods = ['GET'])
def get_cupcake(cupcake.id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    cupcake_data = {'id': cupcake.id, 'flavor' : cupcake.flavor, 'size' : cupcake.size, 'rating' : cupcake.rating, 'image ' : cupcake.image}
    return jsonify(cupcake = cupcake_data)


@app.route('/api/cupcakes' , methods = ['POST'])
def create_cupcakes():
    data = request.get_json()
    new_cupcake = Cupcake(flavor = data['flavor'], size = data['size'], rating = data['rating'], image = data['image'] or None)
    db.session.add(new_cupcake)
    db.session.commit()
    return jsonify(cupcakes = {'id' : new-cupcake.id, 'flavor' : new_cupcake.flavor, 'size' : new_cupcake.size, 'rating' : new_cupcake.image})


@app.route('/api/cupcakes/int:cupcake_id>', methods = ['PATCH'])
def update_cupcake(cupcake_id):
    """Get the cupcake or a 404 message"""
    cupcake = Cupcake.query_or_get_404(cupcake_id)

    """Get updated data from the request"""
    data = request.get.json()

    """Update the cupcake"""
    cupcake.flavor = data.get('flavor', cupcake.flavor)
    cupcake.size = data.get('size', cupcake.size)
    cupcake.rating = data.get('rating', cupcake.rating)
    cupcake.image = data.get('image', cupcake.image)

    db.session.commit()

    cupcake_data = {'id': cupcake.id, 'flavor' : cupcake.flavor, 'size' : cupcake.size, 'rating' : cupcake.rating, 'image ' : cupcake.image}
    return jsonify(cupcake = cupcake_data)

@app.route('/api/cupcakes/<int:cupcake-id>', methods = ['DELETE'])
def delete_cupcake(cupcake_id):
    """Raise 404 error if cupcake not found"""
    cupcake = Cupcake.query_or_get_404(cupcuke_id)

    """Delete the cupcake from database"""
    db.session.delete(cupcake)
    db.session.commit()

    """Message to show the cupcake was deleted"""
    cupcake_data = {'message': f'Cupcake ID {cupcake_id} has been deleted'}

    return jsonify(cupcake_data), 204

if __name__ == '__main__':
    app.run(debug = True)
    app.run()