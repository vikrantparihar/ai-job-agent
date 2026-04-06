from services.field_mapper import FieldMapper

class FormFiller:

    def __init__(self):
        self.mapper = FieldMapper()

    def fill_form(self, page, fields, candidate):

        for field in fields:
            try:
                # 🔍 Map value
                value = self.mapper.map_field(field, candidate)

                if not value:
                    continue

                # 🔥 Important: field structure handle करना
                if isinstance(field, dict):
                    selector = field.get("selector")
                else:
                    selector = field

                if not selector:
                    continue

                # ✍️ Fill field
                page.fill(selector, str(value))

                print(f"✅ Filled: {selector} -> {value}")

            except Exception as e:
                print(f"❌ Fill error for {field}: {e}")