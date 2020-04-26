from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.api.utils.db import get_db
from src.crud.crud_rounds import create, delete, read_all, read_one, update
from src.crud.utils import ExistenceException, NonExistenceException
from src.schemas.round import RoundCreate, RoundInDB, RoundUpdate

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


@router.put("/{round_id}", response_model=RoundInDB)
def update_round(*, db: Session = Depends(get_db), round_id: int, round_info: RoundUpdate):
    """
    Updates the Round specified by  id, with the body request fields.
    """

    try:
        updated_round = update(db_session=db, round_id=round_id, obj_in=round_info)
    except NonExistenceException as err:
        raise HTTPException(status_code=303, detail=err.message)
    return updated_round


@router.delete("/{round_id}", response_model=RoundInDB)
def delete_round(*, db: Session = Depends(get_db), round_id: int):
    """
    Deletes a Round specified by the name.
    """

    try:
        deleted_round = delete(db_session=db, round_id=round_id)
    except NonExistenceException as err:
        raise HTTPException(status_code=303, detail=err.message)
    return deleted_round
