import re, sys, csv, pathlib
from collections import Counter

LOG = sys.argv[1] if len(sys.argv) > 1 else "/var/log/auth.log"
out = pathlib.Path("ssh_bruteforce_report.csv")
pat = re.compile(r"(\w{3}\s+\d+ \d{2}:\d{2}:\d{2}).*Failed password for (?:invalid user )?(\w+) from (\d+\.\d+\.\d+\.\d+)")

rows = []
with open(LOG, "r", errors="ignore") as f:
    for line in f:
        m = pat.search(line)
        if m:
            rows.append({"ts": m.group(1), "user": m.group(2), "ip": m.group(3)})

counter = Counter([r["ip"] for r in rows])
with open(out, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["ts","user","ip"])
    w.writeheader()
    for r in rows:
        w.writerow(r)
print(f"Wrote {out} with {len(rows)} events")
print("Top offenders:", counter.most_common(5))
