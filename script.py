import datetime
from fastapi import FastAPI
from pymongo import MongoClient 
import pandas as pd
import numpy as np
from typing import Union

CONNECTION_STRING ="mongodb+srv://user:12345@attendance.kobg93v.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(CONNECTION_STRING)
db =client['attendance']

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}