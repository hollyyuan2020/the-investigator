## Incident Report: Ransomware Incident
### Summary

A ransomware incident occurred on [Current Date] involving the unauthorized access to sensitive data and encryption of files. The attacker gained initial access through a brute-force login attempt, followed by successful logins using stolen credentials. The malware encrypted critical data and demanded ransom in exchange for decryption keys.

## Timeline

| Time | Event |
| --- | --- |
| 01:14:07 | FAILED LOGIN admin from 185.220.101.47 |
| 01:14:19 | FAILED LOGIN admin from 185.220.101.47 |
| 01:14:31 | SUCCESS LOGIN admin from 185.220.101.47 |
| 01:20:55 | SUCCESS LOGIN admin from 185.220.101.47 |
| 01:22:03 | CREATE \\fileserver\share\invoice.docx |
| 01:31:40 | RENAME report.xlsx -> report.xlsx.locked |
| 01:31:41 | RENAME budget.xlsx -> budget.xlsx.locked |
| 01:31:42 | RENAME patients.db -> patients.db.locked |
| 01:31:50 | CREATE READ_ME_TO_DECRYPT.txt |

## Root Cause

The attacker gained initial access through a brute-force login attempt, followed by successful logins using stolen credentials. The malware encrypted critical data and demanded ransom in exchange for decryption keys.

## MITRE ATT&CK Mapping

| Tactic | Technique Name | Technique ID |
| --- | --- | --- |
| Lateral Movement | Brute Force Login Attempt | T1003 |
| Lateral Movement | Credential Stuffing | T1071 |
| Lateral Movement | File Inclusion (via SFX) | T1050 |
| Obfuscation | Data Encryption | T1021 |

## Runbook Status

Completed:

* 1.2: Kept an offline/immutable backup copy and verified restores on a schedule
* 1.5: Centralized logging with enough retention to reconstruct an incident
* 1.6: Hardened the perimeter in advance (default-deny egress, restricted remote admin)
* 2.3: Correlated evidence across sources into one timeline
* 3.1: Isolated affected hosts from the network

Missed:

* None

## Recommended Next Actions

1. Perform a thorough forensic analysis of the affected systems to gather more information on the attacker's tactics, techniques, and procedures (TTPs).
2. Review and update the firewall/egress policy to include additional security measures to prevent similar incidents in the future.
3. Conduct a lessons-learned review within the next 2 weeks to identify areas for improvement and document the incident response process.
4. Communicate with stakeholders and provide updates on the status of the incident response efforts.