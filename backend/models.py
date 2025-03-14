from database import get_db_connection

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