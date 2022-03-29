from flask import jsonify, Blueprint

from destinations.places.models import Place

place_blueprint = Blueprint('places', __name__)


@place_blueprint.route('/places')
def get_places():
    places = Place.query.all()
    return jsonify({
        "data": [result.serialized for result in places]
    })
