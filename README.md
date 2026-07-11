# AI-Powered Security Static Analysis Triage Tool

A backend tool that automates the triage of static analysis security findings using an LLM.
Built to explore how AI can assist security engineers in reducing false-positive fatigue
and speeding up vulnerability review.

## What it does

1. Runs **Semgrep** (static analysis) against a Python codebase to detect security
   vulnerabilities (e.g. code injection, insecure hashing, XSS, CSRF).
2. Sends each finding to an **LLM (via Groq API)**, which classifies it as a
   True Positive, False Positive, or Needs Human Review, and explains it in plain language.
3. Stores the results in a **SQLite database** using SQLAlchemy.
4. Exposes the triaged findings through a **REST API** built with FastAPI, so results
   can be queried programmatically or viewed in a browser.

## Tech stack

- **Semgrep** — static analysis / vulnerability scanning
- **Groq API (Llama 3)** — LLM-based classification and explanation
- **SQLAlchemy + SQLite** — persistence layer
- **FastAPI + Uvicorn** — REST API backend

## Architecture
Source Code → Semgrep Scan → findings.json → LLM Triage (Groq) → SQLite DB → FastAPI /findings

## Example output

Each finding is enriched with an AI-generated verdict, e.g.:
File: src/flask/cli.py (line 1023)
Issue: Detected use of eval() — possible code injection
Verdict: Needs Human Review
Explanation: eval() is used here in a CLI context. While risky in general,
this usage should be checked for whether external input can reach it.

## Why this project

Static analysis tools generate large volumes of findings, many of which are false
positives or low-priority. This project explores using an LLM to add a layer of
automated reasoning on top of raw scanner output — helping prioritize what a human
reviewer should look at first.

## Running it locally

```bash
pip install semgrep groq fastapi uvicorn sqlalchemy
export GROQ_API_KEY="your_key_here"
semgrep scan --config auto <path_to_code> --json > findings.json
python3 triage.py
uvicorn main:app --reload
```

Then visit `http://127.0.0.1:8000/findings`

- CI/CD integration (GitHub Actions) to run scans automatically on every push
- Human feedback loop to track AI triage accuracy over time
- Support for additional static analysis tools (e.g. Bandit, CodeQL)
