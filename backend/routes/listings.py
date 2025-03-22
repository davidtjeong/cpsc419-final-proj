from flask import request, jsonify
from . import bp
from models import get_listings, create_listing

@bp.route('/listings', methods=['GET'])
def get_filtered_listings():
    try:
        filters = request.args.to_dict()
        limit = request.args.get('limit', type=int)
        listings = get_listings(filters, limit=limit)
        #print("Listings returned:", listings)  # For debugging
        return jsonify(listings)
    except Exception as e:
        print("Error in get_filtered_listings:", str(e))
        return jsonify({"error": str(e)}), 500

@bp.route('/listings', methods=['POST'])
def add_listing():
    try:
        # Use request.json instead of request.args
        listing_data = request.get_json()
        print("Received data:", listing_data)
        
        result = create_listing(listing_data)
        return jsonify(result), 201
    
    except Exception as e:
        import traceback
        error_traceback = traceback.format_exc()
        print("Error creating listing:", str(e))
        print(error_traceback)
        return jsonify({'error': str(e), 'traceback': error_traceback}), 500
    