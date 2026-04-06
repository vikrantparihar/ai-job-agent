import time

def ask_user(question):
    print(f"⚠️ {question}")

    start = time.time()

    while time.time() - start < 30:
        ans = input("Answer: ")
        if ans:
            return ans

    return None