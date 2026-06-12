## Summary
A ransomware incident occurred on June 12, 2026, targeting a Windows-based RDP server. The attacker gained access through brute-force login attempts and successfully logged in using an administrator account. They then executed malicious PowerShell scripts to encrypt data, create backup files, and establish a connection with the attacker's C2 server.

## Timeline
| Time | Event |
| --- | --- |
| 01:02:11 UTC | Windows Security Event Log: Logon (RemoteInteractive) - scheduled maintenance window |
| 01:58:44 UTC | Windows Security Event Log: Account logged off |
| 02:14:07 UTC | Windows Security Event Log: Unknown user name or bad password (failed login attempt) |
| 02:14:09-30 UTC | Multiple failed login attempts by attacker's IP address |
| 02:51:33 UTC | Windows Security Event Log: An account was successfully logged on (RemoteInteractive) |
| 02:53:01 UTC | Windows Security Event Log: A user account was created |
| 02:53:04 UTC | Windows Security Event Log: A member was added to a security-enabled local group |
| 02:55:18 UTC | Windows Security Event Log: A new process has been created (powershell.exe) with suspicious command line arguments |
| 03:07:55 UTC | Windows Security Event Log: Another new process has been created (powershell.exe) with suspicious command line arguments |

## Root Cause
The attacker gained access through brute-force login attempts using the administrator account, and then successfully logged in using this account. They then executed malicious PowerShell scripts to encrypt data and establish a connection with their C2 server.

## MITRE ATT&CK Mapping

| Tactic | Technique Name | Technique ID |
| --- | --- | --- |
| Lateral Movement | Brute Force Login | T1110 |
| Lateral Movement | Remote Services - RDP | T1210 |
| Privilege Procurement | PowerShell Execution | T1003 |
| File and Directory Utilization | Data Exfiltration | T1021 |

## Runbook Status
Completed steps:

* 1.1: Asset inventory was maintained.
* 1.2: Offline backup copy existed and was verified.
* 1.4: Log collectors were pre-staged.
* 1.5: Centralized logging was established with enough retention.
* 1.6: Perimeter hardening was implemented in advance.
* 1.7: Chain-of-custody and evidence-handling procedure was established.

Missed steps:

* 2.1: Ransom notes were not identified initially.
* 2.3: Timeline analysis was incomplete due to limited network traffic data.
* 2.6: Shared indicators were not properly pivoted across the estate.

## Recommended Next Actions
1. **Analyze ransom note files**: Identify any hidden or encrypted files containing instructions for decryption.
2. **Reconstruct timeline using additional network traffic data**: Review more logs to better understand the attacker's movement and actions.
3. **Pivot on shared indicators**: Investigate related activity across the estate, including IP addresses, hashes, and accounts.
4. **Assess blast radius**: Identify any data exfiltration evidence, encrypted volumes, or business impact.
5. **Rebuild systems from known-good images**: Restore data only from verified-clean backups to prevent re-infection.
6. **Conduct lessons-learned review**: Document root cause, timeline, impact, and full remediation within 2 weeks of resolution.