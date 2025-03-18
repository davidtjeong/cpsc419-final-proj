from database import get_db_connection
import datetime

def get_listings(filters):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM Listings WHERE 1=1"
    params = []

    if 'bedrooms' in filters:
        query += " AND apartment_id IN (SELECT apartment_id FROM Apartments WHERE bedrooms = %s)"
        params.append(filters['bedrooms'])

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