class CaptchaDetector:

    def detect(self, page):
        text = page.content().lower()

        captcha_signals = [
            "captcha",
            "verify you are human",
            "robot",
            "recaptcha",
            "hcaptcha"
        ]

        for signal in captcha_signals:
            if signal in text:
                return True

        return False