from langgraph.graph import StateGraph, END

# IMPORTANT FIX: mapping correct function name
from services.ai_engine import process_job_with_ai as detect_ats


# -------------------
# NODE 1: FETCH JOB
# -------------------
def fetch_job(state):
    """
    Simulates job + candidate data fetching
    """

    state["job_url"] = "https://example.com/job/python-dev"
    state["job_desc"] = "Python Developer with FastAPI and SQL experience"
    state["profile"] = "Candidate has 3 years experience in Python, FastAPI, SQL"

    # ATS score (AI engine call)
    state["ats"] = detect_ats(state["profile"])

    return state


# -------------------
# NODE 2: GENERATE RESUME
# -------------------
def generate_resume_node(state):
    ats_score = state.get("ats", {}).get("ats_score", 0)

    state["resume"] = f"""
RESUME
-------
Skills: Python, FastAPI, SQL
Experience: 3 years backend development
Match Score: {ats_score}
"""

    return state


# -------------------
# NODE 3: COVER LETTER
# -------------------
def generate_cover_letter_node(state):
    state["cover_letter"] = f"""
Dear Hiring Manager,

I am excited to apply for the role mentioned in {state.get("job_url")}.

Based on my experience in Python and FastAPI, I believe I am a strong fit.

Regards,
AI Agent
"""

    return state


# -------------------
# BUILD GRAPH
# -------------------
builder = StateGraph(dict)

builder.add_node("fetch_job", fetch_job)
builder.add_node("generate_resume", generate_resume_node)
builder.add_node("cover_letter", generate_cover_letter_node)

builder.set_entry_point("fetch_job")

builder.add_edge("fetch_job", "generate_resume")
builder.add_edge("generate_resume", "cover_letter")
builder.add_edge("cover_letter", END)

graph = builder.compile()