class FileUploader:

    def upload_resume(self, page, file_path):

        selectors = [
            "input[type='file']",
            "input[name*='resume']",
            "input[id*='resume']",
        ]

        for sel in selectors:
            try:
                el = page.query_selector(sel)
                if el:
                    el.set_input_files(file_path)
                    print("📎 Resume uploaded")
                    return True
            except:
                continue

        print("⚠️ Resume upload not found")
        return False