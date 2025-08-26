from sqlalchemy import Column, Integer, String, Double, Boolean, BigInteger
from database import Base

class Carrier(Base):
    __tablename__ = "carriers"
    id = Column(Integer, primary_key=True, index=True)
    carrier = Column(String)
    origin_city = Column(String)
    origin_state = Column(String)
    origin_zip = Column(String)
    destination_city = Column(String)
    destination_state = Column(String)
    destination_zip = Column(String)
    capacity = Column(Integer)

class Shipper(Base):
    __tablename__ = "shippers"
    id = Column(Integer, primary_key=True, index=True)
    shipper = Column(String)
    origin_city = Column(String)
    origin_state = Column(String)
    origin_zip = Column(String)
    destination_city = Column(String)
    destination_state = Column(String)
    destination_zip = Column(String)
    volume = Column(Integer)

class GeoData(Base):
    __tablename__ = "geo_data"
    id = Column(Integer, primary_key=True, index=True)
    country = Column(String)
    postal_code = Column(String)
    lat = Column(Double)
    lng = Column(Double)
    city = Column(String)
    state_code = Column(String)
    state_name = Column(String)
    zcta = Column(String)
    parent_zcta = Column(String)
    population = Column(String)
    density = Column(String)
    county_fips = Column(String)
    county_name = Column(String)
    county_weights = Column(String)
    county_names_all = Column(String)
    county_fips_all = Column(String)
    imprecise = Column(String)
    military = Column(String)
    timezone = Column(String)
    region = Column(String)
    market = Column(String) 