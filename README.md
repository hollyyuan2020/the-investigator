# The Investigator
 
An AI-powered security & network analyst I'm building across 8 weeks.

## Live app

**▶ Try it: https://aisocinvestigator.streamlit.app/**

What it does:
- **Correlate & Triage** — upload multiple log sources (firewall, Sysmon, Windows, Suricata) and get one correlated incident report.
- **MITRE ATT&CK mapping** — each finding tagged with tactic, technique name, and technique ID.
- **Severity + plans** — a Low/Medium/High/Critical score with justification, plus investigation and response plans.
- **Download report** — save any analysis as a timestamped Markdown file.
- **Ask the Investigator** — a chat box for follow-up SOC questions.
- **Case Files** — browse past reports saved in `reports/`.

## Skills so far
- Week 1: Thinks like a security analyst (prompt library)
- Week 2: Can triage suspicious emails — check headers (SPF/DKIM/DMARC, Reply-To), flag urgency/secrecy/authority, recommend out-of-band verification
- Week 3: Can audit server logs for failed-login and brute-force patterns (see audit.py)
- Week 4: Can hunt network beaconing and reconstruct an incident timeline from multiple logs to guide response (timeline.py)
- Week 5: Runs an automated triage pipeline (GitHub Actions + a local Llama 3.2 model via Ollama) that reads the IR runbook, maps findings to MITRE ATT&CK, and writes a verified incident report.
- Week 6: A Streamlit SOC Copilot that correlates four telemetry sources (firewall, Sysmon, Windows, Suricata) via Groq and returns a triaged report with MITRE mapping, severity, and response plan (app.py).

