from sqlalchemy import Column, Integer, String, Float, Date
from app.core.database import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(String)  # keep simple for now
    description = Column(String)
    vendor = Column(String)
    amount = Column(Float)
