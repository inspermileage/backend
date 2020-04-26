from typing import List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from src.api.utils.db import get_db
from src.models.track import Track as TrackModel
from src.schemas.track import TrackCreate, TrackInDB, TrackUpdate

router = APIRouter()


@router.post("/", response_model=TrackInDB)
def create_track(*, db: Session = Depends(get_db), track_in: TrackCreate):
    """
    Inserts a track into the Track table, given the request body.
    """
    try:
        obj_in_data = jsonable_encoder(track_in)
        db_obj = TrackModel(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    except Exception as err:
        raise HTTPException(status_code=500, detail=err)


@router.get("/", response_model=List[TrackInDB])
def read_tracks(db: Session = Depends(get_db)):
    """
    Returns a list of all the track entries in the database.
    """

    return db.query(TrackModel).all()


@router.get("/{name}", response_model=TrackInDB)
def read_track(*, db: Session = Depends(get_db), name: str):
    """
    Returns a Track specified by the name
    """

    track_obj = db.query(TrackModel).filter(TrackModel.name == name).first()
    if not track_obj:
        raise HTTPException(status_code=404, detail="Track not found")
    return track_obj


@router.put("/", response_model=TrackInDB)
def update_track(*, db: Session = Depends(get_db), track_info: TrackUpdate):
    """
    Updates the Track specified by the name field in the request body, with the rest of the body fields.
    """

    # Tries to find the track by name
    track_obj = db.query(TrackModel).filter(TrackModel.name == track_info.name).first()
    if not track_obj:
        raise HTTPException(status_code=404, detail="Track not found")

    # Iterates request body and updates the track object
    obj_data = jsonable_encoder(track_obj)
    update_data = track_info.dict(exclude_unset=True)
    for field in obj_data:
        if field in update_data:
            setattr(track_obj, field, update_data[field])
    db.add(track_obj)
    db.commit()
    db.refresh(track_obj)
    return track_obj


@router.delete("/{name}", response_model=TrackInDB)
def delete_track(*, db: Session = Depends(get_db), name: str):
    """
    Deletes a Track specified by the name.
    """

    track_obj = db.query(TrackModel).filter(TrackModel.name == name).first()
    if not track_obj:
        raise HTTPException(status_code=404, detail="Track not found")

    db.delete(track_obj)
    db.commit()
    return track_obj
