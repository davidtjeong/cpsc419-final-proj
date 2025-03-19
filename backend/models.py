from database import get_db_connection
import datetime


def basic_listings_query():
    """
    Return the basic SELECT query for listings,
    joining Apartments and Locations.
    """
    return """
    SELECT l.*, a.*, loc.*
    FROM Listings l
    LEFT JOIN Apartments a ON l.apartment_id = a.apartment_id
    LEFT JOIN Locations loc ON a.location_id = loc.location_id
    WHERE 1=1
    """

def apply_apartments_filters(query, params, filters):
    """
    Apply filters from the Apartments table:
    - bedrooms, bathrooms, square_footage
    """
    if filters.get('bedrooms'):
        query += " AND a.bedrooms = %s"
        params.append(filters['bedrooms'])
    if filters.get('bathrooms'):
        query += " AND a.bathrooms = %s"
        params.append(filters['bathrooms'])
    if filters.get('square_footage'):
        query += " AND a.square_footage = %s"
        params.append(filters['square_footage'])
    return query, params

def apply_listings_filters(query, params, filters):
    """
    Apply filters from the Listings table:
    - price, start_date, end_date, status, etc.
    """
    if filters.get('price'):
        query += " AND l.price = %s"
        params.append(filters['price'])
    if filters.get('start_date'):
        query += " AND l.start_date = %s"
        params.append(filters['start_date'])
    if filters.get('end_date'):
        query += " AND l.end_date = %s"
        params.append(filters['end_date'])
    if filters.get('status'):
        query += " AND l.status = %s"
        params.append(filters['status'])
    return query, params

def apply_location_filters(query, params, filters):
    """
    Apply filters from the Locations table:
    - street_address, city, state, etc.
    """
    if filters.get('street_address'):
        query += " AND loc.street_address LIKE %s"
        params.append(f"%{filters['street_address']}%")
    return query, params


def get_listings(filters):
    """
    Get listings from the database based on the provided filters.

    Filters include:
      - Apartments: bedrooms, bathrooms, square_footage
      - Listings: price, start_date, end_date, status
      - Locations: street_address, city, state, zip_code, country

    Args:
        filters (dict): Dictionary containing filters for the query.
    """
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Start with a base query that joins all relevant tables
    query = basic_listings_query()
    params = []

    # Apply filters, if present
    query, params = apply_apartments_filters(query, params, filters)
    query, params = apply_listings_filters(query, params, filters)
    query, params = apply_location_filters(query, params, filters)

    # Optionally group/order/limit. Adjust as necessary.
    query += " GROUP BY l.listing_id ORDER BY l.created_at DESC LIMIT 100"

    cursor.execute(query, params)
    listings = cursor.fetchall()

    cursor.close()
    conn.close()

    return listings















def create_listing(listing_data):
    """create a new listing in the database
        Args:
            listing_data (dict):dictionary containing listing information
            
        Returns:
            dict: Information about the created listing including the new ID
        """

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        title = listing_data.get('title')
        location = listing_data.get('location')
        price = listing_data.get('price')
        description = listing_data.get('description')
        start_date = listing_data.get('startDate')
        end_date = listing_data.get('endDate')
        apartment_id = listing_data.get('apartmentId')

        if isinstance(start_date, str):
            start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
        if isinstance(end_date, str):
            end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()

        query = """
        INSERT INTO Listings
        (title, location, price, description, start_date, end_date, apartment_id, created_at)
        VALUES (%s, %s, %s, %s, %s, %S, %S, %S, NOW())"""

        cursor.execute(query, (
            title, 
            location,
            price,
            description,
            start_date,
            end_date,
            apartment_id
        ))

        listing_id = cursor.lastrowid

        conn.commit()
        cursor.close()
        conn.close()

        return {
            'id': listing_id,
            'message': 'Listing created successfully'
        }
    except Exception as e:
        if 'conn' in locals() and conn.is_connected():
            conn.rollback()
            cursor.close()
            conn.close()
        
        raise Exception(f"Error creating listing: {str(e)}")
    