from flask import request, jsonify
from . import bp
from models import get_listings, create_listing

@bp.route('/listings', methods=['GET'])
def get_filtered_listings():
    filters = request.args.to_dict()
    listings = get_listings(filters)
    return jsonify(listings)

@bp.route('/listings', methods=['POST'])
def add_listing():
    try:
        print("Recieved data:", request.json)
        listing_data = request.json
        result = create_listing(listing_data)
        return jsonify(result), 201
    except Exception as e:
        import traceback
        error_traceback = traceback.format_exc()
        print("Error creating listing:", str(e))
        print(error_traceback)
        return jsonify({'error': str(e), 'traceback': error_traceback}), 500
