# Ransomware Incident-Response Runbook

A concise, checklist-driven runbook organized by the four phases of the
[NIST SP 800-61](https://csrc.nist.gov/pubs/sp/800/61/r2/final) incident-response
lifecycle. Work top-to-bottom; check each box as you complete it.

> Scope: ransomware (encryption + extortion). Adapt thresholds and contacts to your environment.

---

## 1. Preparation

- [ ] 1.1 Maintain an up-to-date asset inventory (hosts, owners, criticality, data classification).
- [ ] 1.2 Keep an offline / immutable backup copy and verify restores on a schedule (test, don't assume).
- [ ] 1.3 Document the IR contact tree: incident lead, IT/ops, legal, comms/PR, executive sponsor, insurer.
- [ ] 1.4 Pre-stage tooling: log collectors, EDR, forensic imaging, and detection scripts (`audit.py`, `hunt.py`, `timeline.py`).
- [ ] 1.5 Centralize logging (auth, file, network/egress) with enough retention to reconstruct an incident.
- [ ] 1.6 Harden the perimeter in advance: default-deny egress, restricted remote admin (see `firewall_hardened.conf`).
- [ ] 1.7 Establish a chain-of-custody and evidence-handling procedure before you need it.
- [ ] 1.8 Run tabletop exercises so roles and decisions are rehearsed, not improvised.

---

## 2. Detection & Analysis

- [ ] 2.1 Confirm the incident is real (not a false positive): identify ransom notes (e.g. `READ_ME_TO_DECRYPT.txt`) and mass file renames to extensions like `.locked`.
- [ ] 2.2 Identify patient zero and scope: which hosts, accounts, and shares are affected.
- [ ] 2.3 Correlate evidence across sources — auth, file, and network logs — into one timeline (`timeline.py`).
- [ ] 2.4 Look for the initial access vector: failed-then-successful logins / brute force (`audit.py`).
- [ ] 2.5 Hunt for command-and-control: regular, fixed-size outbound beacons to suspicious IPs/ports (`hunt.py`).
- [ ] 2.6 Pivot on shared indicators (IPs, hashes, accounts) to find related activity across the estate.
- [ ] 2.7 Determine the ransomware family/strain (note, extension, TTPs) to inform decryption/recovery options.
- [ ] 2.8 Assess blast radius: data exfiltration evidence, encrypted volumes, and business impact.
- [ ] 2.9 Assign severity and declare the incident; start the formal incident log (timestamps, actions, decisions).

---

## 3. Containment, Eradication & Recovery

### Containment (short-term)
- [ ] 3.1 Isolate affected hosts from the network (disable switchport / NIC / Wi-Fi) — do **not** power off (preserves memory evidence).
- [ ] 3.2 Block known-bad egress at the firewall (e.g. C2 destinations and non-standard ports) before they re-establish.
- [ ] 3.3 Disable or reset compromised accounts and rotate exposed credentials; revoke active sessions/tokens.
- [ ] 3.4 Protect and isolate backups so encryption/deletion can't spread to them.

### Eradication
- [ ] 3.5 Capture forensic images/snapshots of affected systems before rebuilding.
- [ ] 3.6 Remove the threat: malware, persistence mechanisms, attacker accounts, and unauthorized tooling.
- [ ] 3.7 Patch the exploited vulnerability and close the initial access vector (e.g. tighten remote admin/egress).
- [ ] 3.8 Validate that all indicators of compromise are cleared across the environment, not just on patient zero.

### Recovery
- [ ] 3.9 Rebuild systems from known-good images; restore data only from verified-clean backups.
- [ ] 3.10 Reset all potentially exposed credentials and enforce MFA on remote access.
- [ ] 3.11 Restore in a phased manner with enhanced monitoring; watch for re-infection or beacon resumption.
- [ ] 3.12 Confirm business operations are functioning and data integrity is intact before declaring closure.

---

## 4. Post-Incident Activity

- [ ] 4.1 Hold a blameless lessons-learned review within ~2 weeks of resolution.
- [ ] 4.2 Document root cause, timeline, impact, and full remediation (an incident report).
- [ ] 4.3 Update detections, runbooks, and the firewall/egress policy based on what was missed.
- [ ] 4.4 Track and close remediation action items with owners and due dates.
- [ ] 4.5 Complete legal/regulatory and breach-notification obligations as required.
- [ ] 4.6 Retain evidence per policy; brief stakeholders and feed improvements back into Preparation.

---

### Key decision reminders
- Do **not** pay or negotiate without legal, executive, and insurer/law-enforcement involvement.
- Preserve evidence before remediating — once you wipe, it's gone.
- Communicate on out-of-band channels if email/identity systems may be compromised.
