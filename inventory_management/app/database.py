from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://dbassignment8_2_9evc_user:IXWx4W0VoIeziOTH4ttUGzM3pkFLziME@dpg-crpd2o2j1k6c73c41kp0-a.oregon-postgres.render.com/dbassignment8_2_9evc"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
