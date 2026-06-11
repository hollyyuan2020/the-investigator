import os
import ollama

# Configuration
EVIDENCE_DIR = "evidence"
RUNBOOK_PATH = "ir_runbook.md"
# Output path defaults to reports/incident_report.md; override with TRIAGE_REPORT.
REPORT_PATH = os.environ.get("TRIAGE_REPORT", os.path.join("reports", "incident_report.md"))
# Lab default is llama3.2:1b; override on your own machine with TRIAGE_MODEL
# (e.g. set TRIAGE_MODEL=llama3.1:8b) without editing this file.
MODEL = os.environ.get("TRIAGE_MODEL", "llama3.2:1b")

# Step 1: Read every file in the evidence/ folder and bundle the logs together.
evidence_blobs = []
for name in sorted(os.listdir(EVIDENCE_DIR)):
    path = os.path.join(EVIDENCE_DIR, name)
    if os.path.isfile(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        # Label each log so the model knows which file it came from
        evidence_blobs.append(f"### FILE: {name}\n{content}")
evidence_text = "\n\n".join(evidence_blobs)

# Step 2: Read the incident-response runbook so the model can check our steps.
with open(RUNBOOK_PATH, "r", encoding="utf-8") as f:
    runbook_text = f.read()

# Step 3: Define the analyst persona and the exact report structure we want.
system_prompt = (
    "You are a senior SOC (Security Operations Center) analyst. "
    "You analyze raw security evidence carefully, never invent facts, "
    "and clearly separate what the evidence shows from what you infer. "
    "You write precise, well-structured Markdown incident reports."
)

user_prompt = f"""Analyze the security evidence below against our incident-response runbook
and produce a Markdown incident report.

The report MUST contain these sections, in order:
1. ## Summary - a short executive overview of what happened.
2. ## Timeline - chronological list of key events (with timestamps).
3. ## Root Cause - how the attacker got in and why it succeeded.
4. ## MITRE ATT&CK Mapping - a table with one row per finding, columns:
   Tactic | Technique Name | Technique ID (e.g. T1110).
5. ## Runbook Status - which runbook steps were completed vs. missed,
   referencing the step numbers.
6. ## Recommended Next Actions - prioritized, concrete remediation steps.

=== EVIDENCE (logs from the evidence/ folder) ===
{evidence_text}

=== INCIDENT-RESPONSE RUNBOOK (ir_runbook.md) ===
{runbook_text}
"""

# Step 4: Send everything to the local Llama 3.2 model running in Ollama.
print(f"Sending evidence + runbook to {MODEL} via Ollama...")
response = ollama.chat(
    model=MODEL,
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ],
)
report = response["message"]["content"]

# Step 5: Write the model's Markdown report to reports/incident_report.md.
os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)
with open(REPORT_PATH, "w", encoding="utf-8") as f:
    f.write(report)

print(f"Incident report written to {REPORT_PATH}")
