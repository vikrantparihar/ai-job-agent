# AI Job Automation Agent

## Features
- FastAPI Job Intake API
- SQLite Database
- Queue-based Job Processing
- AI Job Scoring
- Selenium Automation (LinkedIn Easy Apply)
- Logging System
- Retry Handling (basic)

## How to Run

### Install dependencies
pip install -r requirements.txt

### Run API
uvicorn main:app --reload

### Run Worker
python worker.py

## API Usage

POST /add-job

{
  "title": "Software Engineer",
  "description": "Python backend developer with AI experience"
}

## AI Logic
Uses keyword-based scoring to decide whether to apply or skip jobs.

## Architecture
API → DB → Queue → Worker → Automation