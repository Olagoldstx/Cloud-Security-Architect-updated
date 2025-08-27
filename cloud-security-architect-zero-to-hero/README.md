<div align="center">
  <img src="https://img.shields.io/badge/Cloud-Security%20Architect-blue?style=for-the-badge&logo=cloud" alt="Cloud Security Architect"/>
  <img src="https://img.shields.io/badge/Linux-Security-green?style=for-the-badge&logo=linux" alt="Linux Security"/>
  <img src="https://img.shields.io/badge/Python-Security-yellow?style=for-the-badge&logo=python" alt="Python Security"/>
  <img src="https://img.shields.io/badge/AWS-Azure-GCP-orange?style=for-the-badge&logo=amazonaws" alt="Multi-Cloud"/>
</div>

# Cloud Security Architect — Zero to Hero (4-Month Internship-Style Course)

**Author:** Olakunle Paul Omoniyi  
**Instructor:** "Professor of Cloud Security" (Your AI Tutor)  
**Role Target:** Cloud Security Architect (Multi-Cloud: AWS, Azure, GCP)  
**Focus:** Linux • Python • SIEM • Red/Blue Team • Automation • AI Security  
**Format:** 16 weeks → weekly themes with spoon‑fed daily labs & projects

> Drag & drop this entire folder into a new GitHub repository to publish your portfolio.  
> Recruiter‑friendly: Clear structure, daily progress, artifacts, and capstone.

---

## 🔥 Outcome at a Glance
- End‑to‑end **multi‑cloud security** portfolio (AWS, Azure, GCP)
- **Linux + Python** security automation toolkit
- **SIEM detection content** (Splunk/ELK/Azure Sentinel/Chronicle)
- Red‑team vs Blue‑team **attack & defense** evidence
- **Capstone**: Secure-by-design cloud architecture + live detections
- HR‑friendly weekly README trail + final presentation deck

---

## 🗂 Repo Map
```
cloud-security-architect-zero-to-hero/
├─ README.md
├─ LICENSE
├─ CODE_OF_CONDUCT.md
├─ CONTRIBUTING.md
├─ .gitignore
├─ syllabus/
│  ├─ Syllabus.md
│  ├─ WeeklyBreakdown.md
│  └─ DailySchedule.md
├─ labs/
│  ├─ week01_linux_basics/
│  ├─ week02_python_for_security/
│  ├─ week03_aws_cli_iam/
│  ├─ week04_azure_cli_defender/
│  ├─ week05_gcp_security_chronicle/
│  ├─ week06_siem_splunk_sentinel/
│  ├─ week07_network_security/
│  ├─ week08_red_team_basics/
│  ├─ week09_incident_response/
│  ├─ week10_zero_trust/
│  ├─ week11_automation_as_code/
│  ├─ week12_cloud_forensics/
│  ├─ week13_ai_for_security/
│  ├─ week14_capstone_red_vs_blue/
│  ├─ week15_resume_github_branding/
│  └─ week16_final_presentation/
├─ scripts/
│  ├─ python/
│  └─ bash/
├─ projects/
│  ├─ aws_secure_architecture/
│  ├─ azure_defender_labs/
│  ├─ gcp_chronicle_playbooks/
│  └─ final_capstone/
└─ docs/ (diagrams, slides, PDFs)
```

---

## 🧭 How to Use
1. Complete each week in order. Each **week folder** contains a README with learning goals and **7 daily labs**.
2. Commit artifacts daily: scripts, screenshots, detections, queries, architecture diagrams.
3. Tag milestones with releases: `v0.1-foundations`, `v0.2-siem`, `v1.0-capstone`.
4. Share `docs/Final-Presentation.pdf` with recruiters.

---

## 🧪 Environment Prereqs (Local)
- Linux (Ubuntu 22.04) or WSL2
- Python 3.11+ with `venv`
- Docker + docker-compose
- Git + GitHub
- Optional: Kali VM / Parrot for red team labs

## ☁️ Cloud Prereqs
- AWS Free Tier account + IAM admin user
- Azure account + Azure AD Global Admin (test tenant) or PIM eligible
- GCP project + Security tools enabled

---

## 🧰 Quickstart
```bash
# clone your repo after publishing to GitHub
git clone https://github.com/<your-username>/cloud-security-architect-zero-to-hero.git
cd cloud-security-architect-zero-to-hero

# set up Python virtual env for security tooling
python3 -m venv .venv
source .venv/bin/activate
pip install -r labs/week02_python_for_security/requirements.txt
```
