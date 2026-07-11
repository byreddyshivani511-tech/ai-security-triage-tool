import json
import os
from groq import Groq
from db import Session, Finding

# Reads the key from the environment variable we just set — never hardcoded
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

with open("findings.json") as f:
    data = json.load(f)

results = data.get("results", [])[:5]  # start with just 5 findings to be safe
session = Session()

print(f"Sending {len(results)} findings to the AI for triage...\n")

for r in results:
    prompt = f"""
You are a security engineer assistant. Respond in this exact format:

Verdict: (True Positive / False Positive / Needs Human Review)
Explanation: (2-3 sentences, plain English)

File: {r['path']}
Line: {r['start']['line']}
Issue: {r['extra']['message']}
Severity: {r['extra']['severity']}
"""
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    ai_output = response.choices[0].message.content

    entry = Finding(
        file=r['path'],
        line=r['start']['line'],
        issue=r['extra']['message'],
        severity=r['extra']['severity'],
        explanation=ai_output,
    )
    session.add(entry)
    print(f"✔ Processed: {r['path']} (line {r['start']['line']})")

session.commit()
print("\nDone. Results saved to triage.db")