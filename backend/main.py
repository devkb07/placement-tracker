from fastapi import FastAPI, Depends
from schemas import ApplicationCreate, ApplicationResponse
from database import db_connect
import datetime

app = FastAPI(title="Student Placement Tracker")

#TO FINISH TMRW
@app.post()
def create_application():

    
    return new_application

@app.get()
def get_applications():
    
    return applications