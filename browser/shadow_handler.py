class ShadowHandler:

    def get_shadow_element(self, page, selector):
        try:
            element = page.evaluate_handle(f"""
                () => {{
                    return document.querySelector("{selector}")?.shadowRoot || null;
                }}
            """)
            return element
        except:
            return None

    def safe_fill(self, page, selector, value):
        try:
            page.fill(selector, value)
            return True
        except:
            return False