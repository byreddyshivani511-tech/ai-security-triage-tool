from fastapi import FastAPI
from db import Session, Finding

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Security Triage API is running"}

@app.get("/findings")
def get_findings():
    session = Session()
    findings = session.query(Finding).all()
    session.close()
    return [
        {
            "id": f.id,
            "file": f.file,
            "line": f.line,
            "issue": f.issue,
            "severity": f.severity,
            "explanation": f.explanation
        }
        for f in findings
    ]

@app.get("/findings/{finding_id}")
def get_finding(finding_id: int):
    session = Session()
    finding = session.query(Finding).filter(Finding.id == finding_id).first()
    session.close()
    if finding is None:
        return {"error": "Finding not found"}
    return {
        "id": finding.id,
        "file": finding.file,
        "line": finding.line,
        "issue": finding.issue,
        "severity": finding.severity,
        "explanation": finding.explanation
    }