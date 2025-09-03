#!/usr/bin/env python3
"""
Database Population Script for LRT Analytics Platform
This script connects to PostgreSQL and populates tables with sample data.
"""

import os
import psycopg2
from psycopg2.extras import execute_values
import sys

# Database connection parameters
# Update these with your actual Render database credentials
DB_CONFIG = {
    'host': os.environ.get('DB_HOST', 'your-render-db-host'),
    'port': os.environ.get('DB_PORT', '5432'),
    'database': os.environ.get('DB_NAME', 'lanesearch'),
    'user': os.environ.get('DB_USER', 'lanesearch'),
    'password': os.environ.get('DB_PASSWORD', 'your-db-password')
}

# Sample data
CARRIERS_DATA = [
    ('Carrier 1', 'Atlanta', 'GA', '30301', 'St. Louis', 'MO', '63101', 25),
    ('Carrier 1', 'Houston', 'TX', '77001', 'Chicago', 'IL', '60601', 17),
    ('Carrier 1', 'Atlanta', 'GA', '30301', 'Chicago', 'IL', '60601', 32),
    ('Carrier 1', 'Atlanta', 'GA', '30301', 'Chicago', 'IL', '60601', 32),
    ('Carrier 2', 'St. Louis', 'MO', '63101', 'Houston', 'TX', '77001', 18),
    ('Carrier 2', 'Houston', 'TX', '77001', 'Dallas', 'TX', '75201', 34),
    ('Carrier 2', 'Atlanta', 'GA', '30301', 'Houston', 'TX', '77001', 13),
    ('Carrier 3', 'Chicago', 'IL', '60601', 'Atlanta', 'GA', '30301', 30),
    ('Carrier 3', 'Dallas', 'TX', '75201', 'Houston', 'TX', '77001', 24),
    ('Carrier 3', 'Houston', 'TX', '77001', 'St. Louis', 'MO', '63101', 21),
    ('Carrier 4', 'Chicago', 'IL', '60601', 'Dallas', 'TX', '75201', 28),
    ('Carrier 4', 'St. Louis', 'MO', '63101', 'Atlanta', 'GA', '30301', 15),
    ('Carrier 4', 'Dallas', 'TX', '75201', 'Chicago', 'IL', '60601', 33),
    ('Carrier 5', 'Houston', 'TX', '77001', 'Atlanta', 'GA', '30301', 19),
    ('Carrier 5', 'Atlanta', 'GA', '30301', 'Dallas', 'TX', '75201', 26)
]

SHIPPERS_DATA = [
    ('Shipper A', 'Atlanta', 'GA', '30301', 'Chicago', 'IL', '60601', 150),
    ('Shipper A', 'Houston', 'TX', '77001', 'St. Louis', 'MO', '63101', 200),
    ('Shipper B', 'Chicago', 'IL', '60601', 'Dallas', 'TX', '75201', 175),
    ('Shipper B', 'St. Louis', 'MO', '63101', 'Houston', 'TX', '77001', 125),
    ('Shipper C', 'Dallas', 'TX', '75201', 'Atlanta', 'GA', '30301', 300),
    ('Shipper C', 'Atlanta', 'GA', '30301', 'Houston', 'TX', '77001', 250),
    ('Shipper D', 'Houston', 'TX', '77001', 'Chicago', 'IL', '60601', 180),
    ('Shipper D', 'Chicago', 'IL', '60601', 'St. Louis', 'MO', '63101', 220),
    ('Shipper E', 'St. Louis', 'MO', '63101', 'Dallas', 'TX', '75201', 160),
    ('Shipper E', 'Dallas', 'TX', '75201', 'Houston', 'TX', '77001', 190)
]

GEO_DATA = [
    ('US', '30301', 33.7490, -84.3880, 'Atlanta', 'GA', 'Georgia', '5000', '2500'),
    ('US', '60601', 41.8781, -87.6298, 'Chicago', 'IL', 'Illinois', '8000', '3200'),
    ('US', '77001', 29.7604, -95.3698, 'Houston', 'TX', 'Texas', '6500', '2800'),
    ('US', '63101', 38.6270, -90.1994, 'St. Louis', 'MO', 'Missouri', '4500', '2100'),
    ('US', '75201', 32.7767, -96.7970, 'Dallas', 'TX', 'Texas', '7200', '3000'),
    ('US', '10001', 40.7505, -73.9934, 'New York', 'NY', 'New York', '12000', '5000'),
    ('US', '90210', 34.0901, -118.4065, 'Beverly Hills', 'CA', 'California', '3500', '1800'),
    ('US', '33101', 25.7617, -80.1918, 'Miami', 'FL', 'Florida', '4800', '2200'),
    ('US', '98101', 47.6062, -122.3321, 'Seattle', 'WA', 'Washington', '5500', '2600'),
    ('US', '02101', 42.3601, -71.0589, 'Boston', 'MA', 'Massachusetts', '6200', '2900')
]

def connect_to_database():
    """Connect to PostgreSQL database"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def populate_carriers(cursor):
    """Populate carriers table"""
    print("Populating carriers table...")
    
    # Clear existing data
    cursor.execute("DELETE FROM carriers")
    
    # Insert new data
    insert_query = """
        INSERT INTO carriers (carrier, origin_city, origin_state, origin_zip, 
                            destination_city, destination_state, destination_zip, capacity)
        VALUES %s
    """
    
    execute_values(cursor, insert_query, CARRIERS_DATA)
    print(f"Inserted {len(CARRIERS_DATA)} carrier records")

def populate_shippers(cursor):
    """Populate shippers table"""
    print("Populating shippers table...")
    
    # Clear existing data
    cursor.execute("DELETE FROM shippers")
    
    # Insert new data
    insert_query = """
        INSERT INTO shippers (shipper, origin_city, origin_state, origin_zip,
                            destination_city, destination_state, destination_zip, volume)
        VALUES %s
    """
    
    execute_values(cursor, insert_query, SHIPPERS_DATA)
    print(f"Inserted {len(SHIPPERS_DATA)} shipper records")

def populate_geo_data(cursor):
    """Populate geo_data table"""
    print("Populating geo_data table...")
    
    # Clear existing data
    cursor.execute("DELETE FROM geo_data")
    
    # Insert new data
    insert_query = """
        INSERT INTO geo_data (country, postal_code, lat, lng, city, state_code, 
                            state_name, population, density)
        VALUES %s
    """
    
    execute_values(cursor, insert_query, GEO_DATA)
    print(f"Inserted {len(GEO_DATA)} geo data records")

def verify_data(cursor):
    """Verify data was inserted correctly"""
    print("\nVerifying data insertion...")
    
    tables = ['carriers', 'shippers', 'geo_data']
    
    for table in tables:
        cursor.execute(f"SELECT COUNT(*) FROM {table}")
        count = cursor.fetchone()[0]
        print(f"{table}: {count} records")

def main():
    """Main function to populate database"""
    print("LRT Database Population Script")
    print("==============================")
    
    # Check if database credentials are provided
    if DB_CONFIG['host'] == 'your-render-db-host':
        print("\nERROR: Please update the database credentials in the script!")
        print("You need to set:")
        print("- DB_HOST: Your Render database host")
        print("- DB_PASSWORD: Your database password")
        print("\nOr set environment variables:")
        print("export DB_HOST=your-render-db-host")
        print("export DB_PASSWORD=your-db-password")
        sys.exit(1)
    
    # Connect to database
    conn = connect_to_database()
    if not conn:
        print("Failed to connect to database. Exiting.")
        sys.exit(1)
    
    try:
        cursor = conn.cursor()
        
        # Populate tables
        populate_carriers(cursor)
        populate_shippers(cursor)
        populate_geo_data(cursor)
        
        # Commit changes
        conn.commit()
        
        # Verify data
        verify_data(cursor)
        
        print("\n✅ Database population completed successfully!")
        print("\nNext steps:")
        print("1. Go to Superset")
        print("2. Refresh your database connection")
        print("3. Create datasets from the populated tables")
        print("4. Build your dashboard!")
        
    except psycopg2.Error as e:
        print(f"Error during database operation: {e}")
        conn.rollback()
    
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    main()