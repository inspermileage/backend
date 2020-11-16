from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date, datetime
from src.api.utils.db import get_db
from src.crud.crud_rounds import create, delete, read_all, read_one, read_by_reason,read_by_data,  update
from src.crud.utils import ExistenceException, NonExistenceException
from src.schemas.round import RoundCreate, RoundInDB, RoundOutDB, RoundUpdate

router = APIRouter()


@router.post("/", response_model=RoundInDB)
def create_round(*, db: Session = Depends(get_db), round_in: RoundCreate):
    """
    Inserts a round into the Round table, given the request body.
    """
    try:
        created_round = create(db_session=db, obj_in=round_in)
    except ExistenceException as err:
        raise HTTPException(status_code=303, detail=err.message)
    return created_round


@router.get("/", response_model=List[RoundInDB])
def read_rounds(db: Session = Depends(get_db)):
    """
    Returns a list of all the round entries in the database.
    """

    return read_all(db_session=db)


@router.get("/{round_id}", response_model=RoundInDB)
def read_round(*, db: Session = Depends(get_db), round_id: int):
    """
    Returns a Round specified by the id.
    """

    try:
        existing_round = read_one(db_session=db, round_id=round_id)
    except NonExistenceException as err:
        raise HTTPException(status_code=404, detail=err.message)
    return existing_round



@router.get("/reason/{round_reason}", response_model=List[RoundInDB])
def read_round_by_reason(*, db: Session = Depends(get_db), round_reason: str):
    """
    Returns a Round specified by the Reason.
    """

    try:    
        existing_round_reason = read_by_reason(db_session=db, round_reason=round_reason)
    except NonExistenceException as err:
        raise HTTPException(status_code=404, detail=err.message)
    return existing_round_reason

@router.get("/reason/{round_data}", response_model=List[RoundInDB])
def read_round_by_data(*, db: Session = Depends(get_db), round_data: str):
    """
    Returns a Round specified by the Data.
    """

    try:    
        existing_round_data = read_by_data(db_session=db, round_data=round_data)
    except NonExistenceException as err:
        raise HTTPException(status_code=404, detail=err.message)
    return existing_round_data





@router.put("/{round_id}", response_model=RoundOutDB)
def update_round(*, db: Session = Depends(get_db), round_id: int, round_info: RoundUpdate):
    """
    Updates the Round specified by  id, with the body request fields.
    """

    try:
        updated_round = update(
            db_session=db, round_id=round_id, obj_in=round_info)
    except NonExistenceException as err:
        raise HTTPException(status_code=303, detail=err.message)
    return updated_round


@router.delete("/{round_id}", response_model=RoundOutDB)
def delete_round(*, db: Session = Depends(get_db), round_id: int):
    """
    Deletes a Round specified by the id.
    """

    try:
        deleted_round = delete(db_session=db, round_id=round_id)
    except NonExistenceException as err:
        raise HTTPException(status_code=303, detail=err.message)
    return deleted_round
