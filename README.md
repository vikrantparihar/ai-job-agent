AI Job Application Agent 
1️⃣ Project Overview

Ye AI agent jobs ke liye end-to-end application automate karta hai.

Job queue se jobs pick karta hai
Resume tailor karta hai
Cover letter generate karta hai
ATS detect karta hai (Workday, Greenhouse, Lever, LinkedIn)
Form fill karta hai intelligent logic se
Auto submit karta hai

LinkedIn ya ATS login manual hai.

2️⃣ Features
Job queue handling multiple jobs
Resume tailoring per job
Cover letter generation
Form filling using:
Candidate DB
Custom answers
LLM inference
HITL (Human-in-the-Loop) for ambiguous fields
Backlog & failure logging
Demo-ready with seeded jobs and user
3️⃣ Setup Instructions
Clone repo:
git clone https://github.com/<your-username>/ai-job-application-agent.git
cd ai-job-application-agent
Install dependencies:
pip install -r requirements.txt
Copy .env.example → .env and add credentials
Initialize DB + demo data:
python db/seed_demo_data.py
4️⃣ How to Run
python run_demo.py
Manual login will be prompted
Agent picks jobs → fills forms → submits automatically
HITL triggers for ambiguous fields (30s timeout)
5️⃣ Candidate DB
Users: name, email, phone, resume_path
Custom answers: notice period, relocation, salary expectation, etc.
Jobs: URL, company, title, ATS platform, status, failure reason, unresolved fields
6️⃣ ATS Detection
Auto-detects platform from URL + DOM
Supported: Workday, Greenhouse, Lever, LinkedIn
7️⃣ HITL
Triggered only for ambiguous fields
Timeout 30 sec → no input → field logged in DB
User input → auto-fill + saved for future
8️⃣ Demo Recording
File: demo_recording.mp4
Shows:
Manual login
Job pick + ATS detection
Resume + cover letter generation
Form filling + HITL
Auto submission
Job status update
9️⃣ Scaling Notes
Multiple users → separate queues
Concurrent agents → task queue system
Backlog & retry handling built-in
10️⃣ Notes
Credentials only in .env
Hardcoding URLs for demo is allowed
Designed for Easy Apply + 3 ATS demo
