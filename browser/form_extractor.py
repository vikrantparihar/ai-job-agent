class FormExtractor:

    def extract_fields(self, page):
        fields = []

        try:
            # 🔥 HARD WAIT (dynamic load ke liye)
            page.wait_for_timeout(5000)

            # 🔥 RECURSIVE FRAME SCAN
            def extract_from_frame(frame):
                local_fields = []

                try:
                    print("🔍 Checking frame:", frame.url)

                    # wait inside frame
                    frame.wait_for_timeout(2000)

                    inputs = frame.query_selector_all("input, textarea, select")

                    print(f"🧪 Found {len(inputs)} inputs in frame")

                    for inp in inputs:
                        try:
                            name = inp.get_attribute("name") or ""
                            placeholder = inp.get_attribute("placeholder") or ""
                            label = inp.get_attribute("aria-label") or ""

                            field_name = name or placeholder or label

                            if field_name:
                                local_fields.append(field_name)

                        except Exception as e:
                            print("❌ Field error:", e)

                    # 🔥 CHECK CHILD FRAMES (ULTRA FIX)
                    for child in frame.child_frames:
                        local_fields.extend(extract_from_frame(child))

                except Exception as e:
                    print("❌ Frame error:", e)

                return local_fields

            # 🔥 START FROM MAIN PAGE
            fields = extract_from_frame(page.main_frame)

        except Exception as e:
            print("❌ Extract error:", e)

        return list(set(fields))  # remove duplicates