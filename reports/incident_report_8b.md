## Summary
A ransomware attack was detected on May 2nd, with evidence of encryption and extortion attempts. The attacker gained initial access through a brute-force login attempt.

## Timeline

| Time | Event |
| --- | --- |
| 01:14:07 | Failed login attempt from IP 185.220.101.47 (admin account) |
| 01:14:19 | Second failed login attempt from same IP (admin account) |
| 01:14:31 | Successful login from same IP (admin account) |
| 01:20:55 | Subsequent successful login from same IP (admin account) |
| 01:22:03 | File creation on file server (invoice.docx) |
| 01:31:40 | RENAME operation on report.xlsx, renaming it to report.xlsx.locked |
| 01:31:41 | RENAME operation on budget.xlsx, renaming it to budget.xlsx.locked |
| 01:31:42 | RENAME operation on patients.db, renaming it to patients.db.locked |
| 01:31:50 | File creation on file server (READ_ME_TO_DECRYPT.txt) |

## Root Cause
The attacker gained initial access through a brute-force login attempt from IP 185.220.101.47. The account was successfully accessed after two failed attempts, indicating the use of password cracking software.

## MITRE ATT&CK Mapping

| Tactic | Technique Name | Technique ID |
| --- | --- | --- |
| Initial Access | Brute Force | T1140 |
| Lateral Movement | RENAME Operation (to evade detection) | T1021.001 |
| Command and Control | Use of suspicious ports (8443) for C2 communications | T1046 |

## Runbook Status

- **Preparation**: All steps completed
- **Detection & Analysis**:
	+ 2.1: Confirmed the incident is real (identified ransom notes and mass file renames)
	+ 2.2: Identified patient zero and scope of affected hosts, accounts, and shares
	+ 2.3: Correlated evidence across sources into one timeline
	+ 2.4: Found initial access vector (failed-then-successful logins/brute force)
	+ 2.5: Hunted for command-and-control communications (regular, fixed-size beacons to suspicious IPs/ports)
	+ 2.6: Pivoted on shared indicators (IPs, hashes, accounts) to find related activity across the estate
	+ 2.7: Determined ransomware family/strain
	+ 2.8: Assessed blast radius (data exfiltration evidence, encrypted volumes, business impact)
- **Containment, Eradication & Recovery**: All steps pending

## Recommended Next Actions

1.  Isolate affected hosts from the network to prevent further encryption and C2 communications.
2.  Block known-bad egress at the firewall before the attacker re-establishes.
3.  Disable or reset compromised accounts and rotate exposed credentials; revoke active sessions/tokens.
4.  Protect and isolate backups so encryption/deletion can't spread to them.
5.  Capture forensic images/snapshots of affected systems before rebuilding.
6.  Remove the threat: malware, persistence mechanisms, attacker accounts, and unauthorized tooling.

Prioritize these steps according to their urgency and criticality to prevent further damage and ensure successful containment, eradication, and recovery.