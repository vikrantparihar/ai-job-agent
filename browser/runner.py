from browser.session_manager import SessionManager
from browser.ats_detector import ATSDetector
from browser.form_extractor import FormExtractor
from browser.form_filler import FormFiller
from browser.form_submitter import FormSubmitter
from browser.navigation import Navigator
from browser.file_uploader import FileUploader
from browser.captcha_detector import CaptchaDetector
from browser.human_fallback import HumanFallback


class JobRunner:

    def __init__(self, headless=False):
        self.session = SessionManager()

        self.detector = ATSDetector()
        self.extractor = FormExtractor()
        self.filler = FormFiller()
        self.submitter = FormSubmitter()
        self.navigator = Navigator()
        self.uploader = FileUploader()

        # CAPTCHA SYSTEM
        self.captcha = CaptchaDetector()
        self.fallback = HumanFallback()

        self.headless = headless

    def run(self, job_url, candidate):

        # 🔥 URL SAFETY CHECK
        if not job_url:
            raise Exception("❌ Job URL is missing")

        page = self.session.start(headless=self.headless)

        try:
            # 1. OPEN PAGE
            page.goto(job_url)
            page.wait_for_load_state("networkidle")

            # 2. CAPTCHA CHECK
            if self.captcha.detect(page):
                self.fallback.pause_for_human(page)

            # 3. ATS DETECTION
            ats = self.detector.detect(job_url, page.content())
            print(f"🔍 ATS: {ats}")

            # 4. FORM EXTRACTION
            fields = self.extractor.extract_fields(page)
            print(f"📄 Fields found: {len(fields)}")

            # 5. FORM FILLING
            self.filler.fill_form(page, fields, candidate)

            # 6. RESUME UPLOAD
            self.uploader.upload_resume(page, "resume.pdf")

            # 7. MULTI STEP NAVIGATION
            for _ in range(3):
                moved = self.navigator.click_next(page)
                if not moved:
                    break

            # 8. SUBMIT
            submitted = self.submitter.find_and_click_submit(page)

            return {
                "status": "success",
                "ats": ats,
                "submitted": submitted
            }

        except Exception as e:
            return {
                "status": "failed",
                "error": str(e)
            }

        finally:
            # ✅ SAFE CLEANUP (FIXED INDENTATION)
            try:
                self.session.close()
            except Exception as e:
                print("⚠️ Session close error:", e)