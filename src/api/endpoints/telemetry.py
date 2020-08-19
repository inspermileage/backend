from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.api.utils.db import get_db
from src.crud.crud_telemetry import create, delete, read_all, read_one_by_id
from src.crud.utils import ExistenceException, NonExistenceException
from src.schemas.telemetry import (TelemetryCreate, TelemetryInDB,
                                   TelemetryOutDB)

router = APIRouter()


@router.get("/", response_model=List[TelemetryInDB])
def read_Telemetrys(db: Session = Depends(get_db)):
    """
    Returns a list of all the teleme entries in the database.
    """

    return read_all(db_session=db)


@router.get("/{Telemetry_id}", response_model=TelemetryInDB)
def read_Telemetry(*, db: Session = Depends(get_db), Telemetry_id: int):
    """
    Returns a Round specified by the id.
    """

    try:
        existing_round = read_one_by_id(
            db_session=db, Telemetry_id=Telemetry_id)
    except NonExistenceException as err:
        raise HTTPException(status_code=404, detail=err.message)
    return existing_round


@router.post("/", response_model=TelemetryInDB)
def create_Telemetry(*, db: Session = Depends(get_db), Telemetry_in: TelemetryCreate):
    """
    Inserts a round into the Telemetry table, given the request body.
    """
    try:
        created_Telemetry = create(db_session=db, obj_in=Telemetry_in)
    except ExistenceException as err:
        raise HTTPException(status_code=303, detail=err.message)
    return created_Telemetry


@router.delete("/{telemetry_id}", response_model=TelemetryOutDB)
def delete_Telemetry(*, db: Session = Depends(get_db), telemetry_id: int):
    """
    Deletes a Telemetry specified by the id.
    """

    try:
        deleted_Telemetry = delete(db_session=db, telemetry_id=telemetry_id)
    except NonExistenceException as err:
        raise HTTPException(status_code=303, detail=err.message)
    return deleted_Telemetry
