-- Populate carriers table with sample data
INSERT INTO carriers (carrier, origin_city, origin_state, origin_zip, destination_city, destination_state, destination_zip, capacity) VALUES
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
('Carrier 5', 'Atlanta', 'GA', '30301', 'Dallas', 'TX', '75201', 26);

-- Populate shippers table with sample data
INSERT INTO shippers (shipper, origin_city, origin_state, origin_zip, destination_city, destination_state, destination_zip, volume) VALUES
('Shipper A', 'Atlanta', 'GA', '30301', 'Chicago', 'IL', '60601', 150),
('Shipper A', 'Houston', 'TX', '77001', 'St. Louis', 'MO', '63101', 200),
('Shipper B', 'Chicago', 'IL', '60601', 'Dallas', 'TX', '75201', 175),
('Shipper B', 'St. Louis', 'MO', '63101', 'Houston', 'TX', '77001', 125),
('Shipper C', 'Dallas', 'TX', '75201', 'Atlanta', 'GA', '30301', 300),
('Shipper C', 'Atlanta', 'GA', '30301', 'Houston', 'TX', '77001', 250),
('Shipper D', 'Houston', 'TX', '77001', 'Chicago', 'IL', '60601', 180),
('Shipper D', 'Chicago', 'IL', '60601', 'St. Louis', 'MO', '63101', 220),
('Shipper E', 'St. Louis', 'MO', '63101', 'Dallas', 'TX', '75201', 160),
('Shipper E', 'Dallas', 'TX', '75201', 'Houston', 'TX', '77001', 190);

-- Populate geo_data table with sample postal codes
INSERT INTO geo_data (country, postal_code, lat, lng, city, state_code, state_name, population, density) VALUES
('US', '30301', 33.7490, -84.3880, 'Atlanta', 'GA', 'Georgia', '5000', '2500'),
('US', '60601', 41.8781, -87.6298, 'Chicago', 'IL', 'Illinois', '8000', '3200'),
('US', '77001', 29.7604, -95.3698, 'Houston', 'TX', 'Texas', '6500', '2800'),
('US', '63101', 38.6270, -90.1994, 'St. Louis', 'MO', 'Missouri', '4500', '2100'),
('US', '75201', 32.7767, -96.7970, 'Dallas', 'TX', 'Texas', '7200', '3000'),
('US', '10001', 40.7505, -73.9934, 'New York', 'NY', 'New York', '12000', '5000'),
('US', '90210', 34.0901, -118.4065, 'Beverly Hills', 'CA', 'California', '3500', '1800'),
('US', '33101', 25.7617, -80.1918, 'Miami', 'FL', 'Florida', '4800', '2200'),
('US', '98101', 47.6062, -122.3321, 'Seattle', 'WA', 'Washington', '5500', '2600'),
('US', '02101', 42.3601, -71.0589, 'Boston', 'MA', 'Massachusetts', '6200', '2900');

-- Verify data was inserted
SELECT 'Carriers' as table_name, COUNT(*) as record_count FROM carriers
UNION ALL
SELECT 'Shippers' as table_name, COUNT(*) as record_count FROM shippers
UNION ALL
SELECT 'Geo Data' as table_name, COUNT(*) as record_count FROM geo_data;