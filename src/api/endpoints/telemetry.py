from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.api.utils.db import get_db
from src.crud.crud_telemetry import create, delete, read_all, read_one_by_id
from src.crud.utils import ExistenceException, NonExistenceException
from src.models.telemetry import Telemetry as TelemetryModel
from src.schemas.telemetry import TelemetryCreate, TelemetryInDB, TelemetryOutDB

router = APIRouter()


@router.get("/", response_model=List[TelemetryInDB])
def read_Telemetrys(db: Session = Depends(get_db)):
    """
    Returns a list of all the teleme entries in the database.
    """

    return read_all(db_session=db)


@router.get("/{telemetry_id}", response_model=TelemetryInDB)
def read_Telemetry(*, db: Session = Depends(get_db), Telemetry_id: int):
    """
    Returns a Round specified by the id.
    """

    try:
        existing_round = read_one_by_id(db_session=db, Telemetry_id=Telemetry_id)
    except NonExistenceException as err:
        raise HTTPException(status_code=404, detail=err.message)
    return existing_round


# @router.get("/{telemetry_data_teste}", response_model=TelemetryInDB)
# def read_Telemetry_by_id(*, db: Session = Depends(get_db), Telemetry_ref_date: date):
#     """
#     Returns a Round specified by the date.
#     """

#     try:
#         existing_round = read_one_by_date(db_session=db, Telemetry_ref_date=Telemetry_ref_date)
#     except NonExistenceException as err:
#         raise HTTPException(status_code=404, detail=err.message)
#     return existing_round


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


# @router.put("/", response_model=TelemetryInDB)
# def update_Telemetry(*, db: Session = Depends(get_db), Telemetry_id: int, Telemetry_info: TelemetryUpdate):
#     """
#     Updates the Telemetry specified by id, with the body request fields.
#     """
#     try:
#         updated_Telemetry = update(db_session=db, Telemetry_id=Telemetry_id, obj_in=Telemetry_info)
#     except NonExistenceException as err:
#         raise HTTPException(status_code=303, detail=err.message)
#     return updated_Telemetry


@router.delete("/{telemetry_id}", response_model=TelemetryOutDB)
def delete_Telemetry(*, db: Session = Depends(get_db), telemetry_id: int):
    """
    Deletes a Telemetry specified by the name.
    """

    try:
        deleted_Telemetry = delete(db_session=db, telemetry_id=telemetry_id)
    except NonExistenceException as err:
        raise HTTPException(status_code=303, detail=err.message)
    return deleted_Telemetry
