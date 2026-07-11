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
