from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects import postgresql as psql
from sqlalchemy.schema import Identity
from .database import Base


class Job(Base):
    __tablename__ = "jobs"
    job_id = Column(Integer, Identity(start=1, cycle=False), primary_key=True, index=True)
    job_type = psql.ENUM('ingestion', 'prediction', name='process')
    job_started = Column(psql.TIMESTAMP)
    job_ended = Column(psql.TIMESTAMP)
    files = Column(psql.ARRAY(String))
    file_records = Column(psql.ARRAY(TEXT))


class Attribute(Base):
    __tablename__ = "attributes"
    attribute_id = Column(Integer, Identity(start=1, cycle=False), primary_key=True, index=True)
    ingestion_id = relationship("Job", index=True)
    entity_id = Column(Intege, index=True)
    key = Column(String, index=True)
    value = Column(psql.JSON)