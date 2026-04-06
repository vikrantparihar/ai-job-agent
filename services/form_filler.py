from services.field_resolver import resolve_field


def fill_form(page, ats, resume_path, cover_letter, user_id):

    print(f"🧠 Starting form fill for ATS: {ats}")

    if ats == "lever":
        return fill_lever_form(page, resume_path, cover_letter, user_id)

    elif ats == "greenhouse":
        return fill_greenhouse_form(page, resume_path, cover_letter, user_id)

    else:
        print("⚠️ ATS not supported yet")
        return []


# 🟢 LEVER FORM
def fill_lever_form(page, resume_path, cover_letter, user_id):
    print("🟢 Filling Lever form...")

    unanswered = []

    try:
        # Full Name
        name = resolve_field("name", "text", user_id)
        if name:
            if page.query_selector("input[name='name']"):
                page.fill("input[name='name']", name)
            else:
                unanswered.append("name")

        # Email
        email = resolve_field("email", "text", user_id)
        if email:
            if page.query_selector("input[name='email']"):
                page.fill("input[name='email']", email)
            else:
                unanswered.append("email")

        # Phone (optional)
        phone = resolve_field("phone", "text", user_id)
        if phone:
            if page.query_selector("input[name='phone']"):
                page.fill("input[name='phone']", phone)

        # Resume Upload
        if page.query_selector("input[type='file']"):
            page.set_input_files("input[type='file']", resume_path)
        else:
            unanswered.append("resume")

        # Cover Letter
        if page.query_selector("textarea"):
            page.fill("textarea", cover_letter)

    except Exception as e:
        print("❌ Lever form error:", e)

    return unanswered


# 🟡 GREENHOUSE FORM (basic)
def fill_greenhouse_form(page, resume_path, cover_letter, user_id):
    print("🟡 Filling Greenhouse form...")

    unanswered = []

    try:
        # Name
        name = resolve_field("name", "text", user_id)
        if name:
            if page.query_selector("input[name='first_name']"):
                page.fill("input[name='first_name']", name)

        # Email
        email = resolve_field("email", "text", user_id)
        if email:
            if page.query_selector("input[name='email']"):
                page.fill("input[name='email']", email)

        # Resume
        if page.query_selector("input[type='file']"):
            page.set_input_files("input[type='file']", resume_path)

    except Exception as e:
        print("❌ Greenhouse error:", e)

    return unanswered