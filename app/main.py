#!/usr/bin/env python3

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import json
import os

app = FastAPI()

@app.get("/")  # zone apex
def zone_apex():
<<<<<<< HEAD
    return {"Hello": "Hello Zoe"}
=======
    return {"Hello": "Hello API"}
>>>>>>> 661468dda0051934e6ad7be7bd4eeb40d3c08169

@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"sum": a + b}
<<<<<<< HEAD

@app.get("/square/{a}")
def square(a: int):
    return {"square": a ** 2}
=======
>>>>>>> 661468dda0051934e6ad7be7bd4eeb40d3c08169
