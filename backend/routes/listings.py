from flask import request, jsonify
from . import bp
from models import get_listings

@bp.route('/listings', methods=['GET'])
def get_filtered_listings():
    filters = request.args.to_dict()
    listings = get_listings(filters)
    return jsonify(listings)
