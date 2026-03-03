---
name: recon_suite
description: Proactive network scanning and Oracle DB integration.
---
# Instructions
1. Scan the target range using `nmap -sV -T4 --script=vulners`.
2. Save the XML output to a temporary file.
3. Use the `scripts/upload_to_oracle.py` to push findings to the `client_vault`.
4. Generate a Gap Analysis comparing the new scan to the previous DB entry.
