# Day 1: Linux CLI Fundamentals

## Why it matters
Linux is the control plane for most security tooling.

## Prereqs
- None

## Steps
1. `uname -a`, `ls`, `cat`, `tail -f`
2. Users & groups: `useradd`, `passwd`, `usermod`, `groups`
3. Permissions: `chmod`, `chown`, `umask`
4. Services: `systemctl status ssh`
5. Hardening: disable root SSH, set up key-based auth

## Deliverables
- [ ] Hardened SSH config + screenshot of successful key login

## Reflection
- What failed?
- How would you detect/prevent this in prod?
