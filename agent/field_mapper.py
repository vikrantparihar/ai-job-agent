class FieldMapper:

    def map_field(self, field, candidate):

        text = str(field).lower()

        # NAME
        if "name" in text:
            return candidate.get("name", "John Doe")

        # EMAIL
        if "email" in text:
            return candidate.get("email", "demo@email.com")

        # SKILLS
        if "skill" in text:
            return ", ".join(candidate.get("skills", []))

        # EXPERIENCE
        if "experience" in text:
            return candidate.get("experience", "")

        # DEFAULT (unknown)
        return None