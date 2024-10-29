#!/usr/bin/env python3

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import json
import os

app = FastAPI()

@app.get("/")  # zone apex
def zone_apex():
    return {"Hello": "Hello Zoe"}

@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"sum": a + b}

@app.get("/square/{a}")
def square(a: int):
    return {"square": a ** 2}

@app.get("/divide/{a}/{b}")
def divide(a: int, b: int):
    return {"quotient": a / b}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
