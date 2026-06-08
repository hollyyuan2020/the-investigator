Verdict: Likely Business Email Compromise (BEC) / CEO Fraud attempt

Confidence: High (95–99%)

Evidence
Authentication Failures
SPF: softfail
DKIM: fail
DMARC: fail

These indicate the message did not successfully authenticate as a legitimate email from the purported domain.

Reply-To Mismatch
From: marcus.webb@meridiangroup.com
Reply-To: mwebb.ceo2026@gmail.com

This is a strong indicator of fraud. The attacker wants responses sent to a Gmail account under their control rather than the corporate account.

Social Engineering Indicators
Executive impersonation (CEO)
Urgent wire transfer request
Claims executive is unavailable
Secrecy request ("Do not discuss this with anyone else")
High-dollar transaction
Time pressure ("deadline of 5 PM today")



Recommended Action
Do not send the wire.
Do not reply to the email.
Contact the CEO using a known phone number or trusted communication channel.
Notify the security team.
Preserve the message and headers for investigation.
Require out-of-band verification and dual approval before any funds transfer.
