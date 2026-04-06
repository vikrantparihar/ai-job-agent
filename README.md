
# AI Job Application Agent

## 🚀 Project Overview
This project is an **AI Job Application Agent** that automates the end-to-end job application process.  
It picks jobs from a queue, tailors the resume, generates a cover letter, detects ATS platforms, fills the application forms intelligently, and submits them automatically.  

> Manual login is required for LinkedIn or other ATS platforms.  

---

## 🎯 Features
- **Job Queue:** Handles multiple jobs automatically.
- **Resume Tailoring:** Customizes resume per job using candidate profile.
- **Cover Letter Generation:** Automatically generates a professional cover letter.
- **ATS Detection:** Supports Workday (required), Greenhouse, Lever, LinkedIn.
- **Form Filling:** Intelligent filling via:
  1. Candidate Database
  2. Custom Answers (key-value pairs)
  3. LLM inference for missing fields
- **Human-in-the-Loop (HITL):** Pauses ambiguous fields, 30-second user input timeout.
- **Demo Ready:** Pre-seeded user + 5–6 demo job URLs.

---

## 📂 Repository Structure

---

## ⚙️ Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/<your-username>/ai-job-application-agent.git
cd ai-job-application-agent
Install dependencies
pip install -r requirements.txt
Add credentials
Copy .env.example → .env
Add your LinkedIn username and password
(Optional) ATS API keys if required
Initialize DB & seed demo data
python db/seed_demo_data.py
🏃 How to Run Demo
python run_demo.py
Manual login will be prompted.
Agent will pick jobs, fill forms using:
Candidate DB
Custom answers
LLM inference (if needed)
HITL triggers for ambiguous fields with 30-second timeout.
Once submitted, the agent moves to the next job automatically.
