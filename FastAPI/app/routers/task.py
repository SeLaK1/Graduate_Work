from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated

from app.models import *
from app.schemas import CreateTask, UpdateTask
from sqlalchemy import select, update, delete, insert

router = APIRouter(prefix='/task', tags=['task'])

@router.get('/')
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task)).all()
    return tasks

@router.get('/task_id')
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is no task found'
        )
    return task

@router.post('/create')
async def create_task(db: Annotated[Session, Depends(get_db)], create_task: CreateTask, user_id: int):
    if db.scalar(select(Task).where(Task.id == user_id)) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is no user found'
        )

    db.execute(insert(Task).values(title=create_task.title,
                                   content=create_task.content,
                                   priorit=create_task.priorit,
                                   user_id=user_id))
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Успешно'
    }

@router.put('/update')
async def update_task(db: Annotated[Session, Depends(get_db)], task_id: int, update_task: UpdateTask):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is no user found'
        )
    db.execute(update(Task).where(Task.id == task_id).values(title=update_task.title,
                                                             content=update_task.content,
                                                             priorit=update_task.priorit))
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Успешно'
    }

@router.delete('/delete')
async def delete_task(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalar(select(Task).where(Task.id == int))
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is no user found'
        )

    db.execute(delete(Task).where(Task.id == task_id))

    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Успешно'
    }










