from db.database import SessionLocal
from models.candidate import Candidate
from models.custom_answer import CustomAnswer
from services.ai_engine import process_job_with_ai
from browser.human_fallback import HumanFallback


class FieldMapper:

    def __init__(self):
        self.db = SessionLocal()
        self.fallback = HumanFallback()

    def map_field(self, field_name: str, candidate: Candidate):

        field_name_lower = field_name.lower()

        # 1️⃣ Candidate DB mapping
        if "name" in field_name_lower:
            return candidate.name

        if "email" in field_name_lower:
            return candidate.email

        if "phone" in field_name_lower:
            return candidate.phone

        if "skill" in field_name_lower:
            return candidate.skills

        if "experience" in field_name_lower:
            return candidate.experience

        # 2️⃣ Custom answers DB
        custom_answers = self.db.query(CustomAnswer).all()
        for ans in custom_answers:
            if ans.question.lower() in field_name_lower:
                return ans.answer

        # 3️⃣ AI fallback
        ai_result = process_job_with_ai(
            job_desc=field_name,
            candidate_profile=candidate.skills
        )

        if "analysis" in ai_result:
            return ai_result["analysis"]

        # 4️⃣ HUMAN-IN-THE-LOOP
        user_answer = self.fallback.ask_user(field_name)

        if user_answer:
            new_ans = CustomAnswer(
                question=field_name,
                answer=user_answer
            )
            self.db.add(new_ans)
            self.db.commit()

            return user_answer

        # 5️⃣ skip if no answer
        return None