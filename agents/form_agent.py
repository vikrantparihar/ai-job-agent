def fill_form(page):
    try:
        # Example fields
        if page.locator("input[name='email']").count() > 0:
            page.fill("input[name='email']", "your@email.com")

        if page.locator("input[name='name']").count() > 0:
            page.fill("input[name='name']", "Vikrant")

        print("✅ Form filled")

    except Exception as e:
        print("❌ Form error:", e)