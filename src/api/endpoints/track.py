from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.api.utils.db import get_db
from src.crud.crud_track import (create, delete, read_all, read_one_by_name,
                                 update)
from src.crud.utils import ExistenceException, NonExistenceException
from src.schemas.track import TrackCreate, TrackInDB, TrackUpdate, TrackOutDB

router = APIRouter()


@router.get("/", response_model=List[TrackInDB])
def read_tracks(db: Session = Depends(get_db)):
    """
    Returns a list of all the track entries in the database.
    """

    return read_all(db_session=db)


@router.get("/{track_name}", response_model=TrackInDB)
def read_track(*, db: Session = Depends(get_db), track_name: str):

    """
    Returns a Track specified by the name
    """
    try:
        existing_round = read_one_by_name(db_session=db, Track_name=track_name)
    except NonExistenceException as err:
        raise HTTPException(status_code=404, detail=err.message)
    return existing_round


@router.post("/", response_model=TrackInDB)
def create_track(*, db: Session = Depends(get_db), track_in: TrackCreate):
    """
    Inserts a track into the Track table, given the request body.
    """
    try:
        created_Track = create(db_session=db, obj_in=track_in)
    except ExistenceException as err:
        raise HTTPException(status_code=303, detail=err.message)
    return created_Track


@router.put("/{track_name}", response_model=TrackOutDB)
def update_track(*, db: Session = Depends(get_db), track_name: str, track_info: TrackUpdate):
    """
    Updates the Track specified by the name field in the request body, with the rest of the body fields.
    """

    try:
        updated_track = update(db_session=db, track_name=track_name, obj_in=track_info)
    except NonExistenceException as err:
        raise HTTPException(status_code=303, detail=err.message)
    return updated_track


@router.delete("/{track_name}", response_model=TrackOutDB)
def delete_track(*, db: Session = Depends(get_db), track_name: str):
    """
    Deletes a Track specified by the name.
    """
    try:
        deleted_Track = delete(db_session=db, track_name=track_name)
    except NonExistenceException as err:
        raise HTTPException(status_code=303, detail=err.message)
    return deleted_Track
