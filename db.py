from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Finding(Base):
    __tablename__ = "findings"
    id = Column(Integer, primary_key=True)
    file = Column(String)
    line = Column(Integer)
    issue = Column(Text)
    severity = Column(String)
    verdict = Column(String)
    explanation = Column(Text)

engine = create_engine("sqlite:///triage.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)