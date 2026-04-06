import time

class HumanFallback:

    def ask_user(self, question: str, timeout=30):
        print(f"\n⚠️ NEED HUMAN INPUT: {question}")
        print(f"⏳ You have {timeout} seconds...")

        start_time = time.time()

        while time.time() - start_time < timeout:
            try:
                user_input = input("👉 Enter answer: ")
                if user_input:
                    return user_input
            except:
                pass

        print("⏰ Timeout reached!")
        return None

    # ✅ FIX: ADD THIS (IMPORTANT)
    def pause_for_human(self, page=None, seconds=5):
        print(f"🧍 Human fallback pause started...")
        time.sleep(seconds)
        print("🧍 Resume automation...")