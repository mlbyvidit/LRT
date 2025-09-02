
from fastapi import FastAPI, UploadFile, File, Depends, Body
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import pandas as pd
from database import SessionLocal, engine, Base
from models import Carrier, Shipper, GeoData
import os
import requests
import json
import csv
from pathlib import Path

Base.metadata.create_all(bind=engine)

# Load sample data on startup
def load_sample_data():
    db = SessionLocal()
    try:
        # Check if data already exists
        if db.query(Carrier).count() > 0:
            print("Data already loaded, skipping...")
            return
        
        print("Loading sample data...")
        
        # Load carriers
        carriers_file = Path("carrier_samples.csv")
        if carriers_file.exists():
            with open(carriers_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    carrier = Carrier(
                        carrier=row['carrier'],
                        origin_city=row['origin_city'],
                        origin_state=row['origin_state'],
                        origin_zip=row['origin_zip'],
                        destination_city=row['destination_city'],
                        destination_state=row['destination_state'],
                        destination_zip=row['destination_zip'],
                        capacity=int(row['capacity'])
                    )
                    db.add(carrier)
        
        # Load shippers
        shippers_file = Path("shippers_sample.csv")
        if shippers_file.exists():
            with open(shippers_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    shipper = Shipper(
                        shipper=row['shipper'],
                        origin_city=row['origin_city'],
                        origin_state=row['origin_state'],
                        origin_zip=row['origin_zip'],
                        destination_city=row['destination_city'],
                        destination_state=row['destination_state'],
                        destination_zip=row['destination_zip'],
                        volume=int(row['volume'])
                    )
                    db.add(shipper)
        
        # Load postal codes (first 100 rows to avoid overwhelming)
        postal_file = Path("postal_codes.csv")
        if postal_file.exists():
            with open(postal_file, 'r') as file:
                reader = csv.DictReader(file)
                count = 0
                for row in reader:
                    if count >= 100:  # Limit to first 100 rows
                        break
                    geo_data = GeoData(
                        country=row.get('country', ''),
                        postal_code=row.get('postal_code', ''),
                        lat=float(row['lat']) if row.get('lat') else None,
                        lng=float(row['lng']) if row.get('lng') else None,
                        city=row.get('city', ''),
                        state_code=row.get('state_code', ''),
                        state_name=row.get('state_name', ''),
                        zcta=row.get('zcta', ''),
                        parent_zcta=row.get('parent_zcta', ''),
                        population=row.get('population', ''),
                        density=row.get('density', ''),
                        county_fips=row.get('county_fips', ''),
                        county_name=row.get('county_name', ''),
                        county_weights=row.get('county_weights', ''),
                        county_names_all=row.get('county_names_all', ''),
                        county_fips_all=row.get('county_fips_all', ''),
                        imprecise=row.get('imprecise', ''),
                        military=row.get('military', ''),
                        timezone=row.get('timezone', ''),
                        region=row.get('region', ''),
                        market=row.get('market', '')
                    )
                    db.add(geo_data)
                    count += 1
        
        db.commit()
        print("Sample data loaded successfully!")
        
    except Exception as e:
        print(f"Error loading sample data: {e}")
        db.rollback()
    finally:
        db.close()

app = FastAPI()

# Load data on startup
@app.on_event("startup")
async def startup_event():
    load_sample_data()

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://lrt-direct.onrender.com", "http://localhost:3003"],  # Production and local URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class GuestTokenRequest(BaseModel):
    dashboard_id: str

# Superset credentials from environment variables
SUPERSET_USERNAME = os.environ.get("SUPERSET_USERNAME", "admin")
SUPERSET_PASSWORD = os.environ.get("SUPERSET_PASSWORD", "admin")
SUPERSET_HOST = os.environ.get("SUPERSET_HOST", "https://superset-web.onrender.com") # Use Render URL in production

async def get_superset_access_token():
    login_data = {
        "username": SUPERSET_USERNAME,
        "password": SUPERSET_PASSWORD,
        "provider": "db"
    }
    login_url = f"{SUPERSET_HOST}/api/v1/security/login"
    response = requests.post(login_url, json=login_data)
    response.raise_for_status()
    return response.json()["access_token"]

@app.post("/superset/guest_token")
async def get_superset_guest_token(request: GuestTokenRequest):
    dashboard_id = request.dashboard_id
    try:
        access_token = await get_superset_access_token()
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        guest_token_url = f"{SUPERSET_HOST}/api/v1/security/guest_token/"
        
        # Define the resources and user for the guest token
        guest_token_payload = {
            "resources": [
                {"type": "dashboard", "id": dashboard_id}
            ],
            "user": {
                "username": "guest_user",
                "first_name": "Guest",
                "last_name": "User"
            }
        }
        
        response = requests.post(guest_token_url, headers=headers, json=guest_token_payload)
        response.raise_for_status()
        return {"guest_token": response.json()["token"]}
    except requests.exceptions.RequestException as e:
        print(f"Error generating Superset guest token: {e}")
        return {"error": str(e)}, 500

@app.get("/")
def read_root():
    return {"message": "Lane Search API is running"}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/upload/carriers")
async def upload_carriers(file: UploadFile = File(...), db: Session = Depends(get_db)):
    df = pd.read_csv(file.file)
    for _, row in df.iterrows():
        carrier = Carrier(**{k: row[k] for k in Carrier.__table__.columns.keys() if k != 'id'})
        db.add(carrier)
    db.commit()
    return {"status": "success"}

@app.post("/upload/shippers")
async def upload_shippers(file: UploadFile = File(...), db: Session = Depends(get_db)):
    df = pd.read_csv(file.file)
    for _, row in df.iterrows():
        shipper = Shipper(**{k: row[k] for k in Shipper.__table__.columns.keys() if k != 'id'})
        db.add(shipper)
    db.commit()
    return {"status": "success"}

@app.post("/upload/geo")
async def upload_geo(file: UploadFile = File(...), db: Session = Depends(get_db)):
    df = pd.read_csv(file.file)

    # Define a mapping from CSV columns to GeoData model columns
    # This handles cases where CSV column names might differ or columns are missing
    column_mapping = {
        "country": "country",
        "postal_code": "postal_code",
        "lat": "lat",
        "lng": "lng",
        "city": "city",
        "state_code": "state_code",
        "state_name": "state_name",
        "zcta": "zcta",
        "parent_zcta": "parent_zcta",
        "population": "population",
        "density": "density",
        "county_fips": "county_fips",
        "county_name": "county_name",
        "county_weights": "county_weights",
        "county_names_all": "county_names_all",
        "county_fips_all": "county_fips_all",
        "imprecise": "imprecise",
        "military": "military",
        "timezone": "timezone",
        "market": "market",
        # 'region' is in the model but not in the CSV, will be handled below
    }

    # Prepare a list to hold GeoData objects
    geo_data_to_add = []

    for _, row in df.iterrows():
        data = {}
        for model_col, csv_col in column_mapping.items():
            if csv_col in row and pd.notna(row[csv_col]):
                # Explicitly convert numeric types, handling potential errors
                if model_col in ["lat", "lng", "population", "density"]:
                    try:
                        data[model_col] = float(row[csv_col])
                    except ValueError:
                        data[model_col] = None  # Set to None if conversion fails
                else:
                    data[model_col] = str(row[csv_col])
            else:
                data[model_col] = None  # Set to None if column is missing or NaN

        # Handle 'region' column which is in the model but not in the CSV
        if "region" not in data:
            data["region"] = None

        geo = GeoData(**data)
        db.add(geo)

    db.commit()
    return {"status": "success"}

@app.get("/data/carriers")
def get_carriers(db: Session = Depends(get_db)):
    return [c.__dict__ for c in db.query(Carrier).all()]

@app.get("/data/shippers")
def get_shippers(db: Session = Depends(get_db)):
    return [s.__dict__ for s in db.query(Shipper).all()] 

@app.get("/data/geo")
def get_geo(db: Session = Depends(get_db)):
    return [g.__dict__ for g in db.query(GeoData).all()]
