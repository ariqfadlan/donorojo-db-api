"""
Main entrypoint for API server

Created by : ariqfadlan
Version    : 1.0.0
License    : MIT
"""
import base64
from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi.responses import StreamingResponse, JSONResponse, RedirectResponse
from fastapi import FastAPI, Depends, HTTPException, Query, Header

from app import controllers, schemas, models
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

DESCRIPTION="""
VisitDonorojo Database API helps you to provide
tourism data from Sendang and Kalak village.

## Info
You can **read infos**
"""

app = FastAPI(
    title="VisitDonrojo API",
    description=DESCRIPTION,
    version="1.0.0",
    contact={
        "name": "KKN-PPM UGM Donorojo Team",
        "url": "http://visitdonorojo.id/contact",
    },
    license_info={
        "name": "MIT",
    },
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/', response_class=RedirectResponse, include_in_schema=False)
def root():
    return "/docs"

@app.get('/places', response_model=List[schemas.TouristAttraction],
        response_model_exclude={
            "location": {"tourist_attraction_id"},
            "address": {"tourist_attraction_id"}
        },
        responses={
            200: {"model": List[schemas.TouristAttractionDocs]},
            404: { "model": schemas.GeneralException }
            },
        tags=["infos"]
    )

def get_all_places(
        skip: int = 0,
        limit: int = 100,
        db: Session = Depends(get_db)
    ):
    places = controllers.get_tourist_attractions(skip, limit, db)
    if places is None:
        raise HTTPException(404, "No places found!")
    return places


@app.get("/place/{place_id}", response_model=schemas.TouristAttraction,
        response_model_exclude={
            "location": {"tourist_attraction_id"},
            "address": {"tourist_attraction_id"}
        },
        responses={
            200: { "model": schemas.TouristAttractionDocs },
            404: { "model": schemas.GeneralException }
        },
        tags=["infos"]
        )
def get_a_place(place_id: int, db: Session = Depends(get_db)):
    db_place = controllers.get_tourist_attraction(db, row_id=place_id)
    if db_place is None:
        raise HTTPException(404, "Place not found!")
    return db_place


@app.get("/address/{place_id}", response_model=schemas.Address,
        responses = {404: { "model": schemas.GeneralException }},
        tags=["infos"]
        )
def get_an_address(place_id: int, db: Session = Depends(get_db)):
    db_address = controllers.get_address_by_id(db, place_id)
    if db_address is None:
        raise HTTPException(404, "Address not found!")
    return db_address


@app.get("/location/{place_id}", response_model=schemas.Location,
        responses = {404: { "model": schemas.GeneralException }},
        tags=["infos"]
        )
def get_a_location(place_id: int, db: Session = Depends(get_db)):
    db_location = controllers.get_location_by_id(db, place_id)
    if db_location is None:
        raise HTTPException(404, "Location not found!")
    return db_location


@app.get("/qr/{place_id}",
        responses={
        200: { "content": { "image/png": {} }},
        406: { "model": schemas.GeneralException }
            },
        response_model=schemas.LocationQR,
        tags=["infos"]
        )
def generate_geo_qrcode(
        place_id: int,
        db: Session = Depends(get_db),
        accept: str = Header(None),
        use_google: Optional[bool] = Query(False, alias="use-google")
    ):
    loc = controllers.get_location_by_id(db, place_id)
    if loc is None:
        raise HTTPException(404, "Location not found!")

    if use_google:
        data = controllers.generate_qrcode(
                loc.latitude,
                loc.longitude,
                "https://www.google.com/maps/search/?api=1&query=")
    else:
        data = controllers.generate_qrcode(loc.latitude, loc.longitude)

    if accept == "image/png":
        return StreamingResponse(content=data, media_type="image/png")
    if accept in ("application/json", "*/*"):
        data_encoded = base64.urlsafe_b64encode(data.read())
        return JSONResponse({"data": str(data_encoded, "utf-8")})

    raise HTTPException(406,
                "Filetype not supported! Available: 'image/png' or 'application/json'")
