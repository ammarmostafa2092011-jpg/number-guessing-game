import random

def play_game():
    # البرنامج بيختار رقم عشوائي بين 1 و100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("🎯 أهلاً بيك في لعبة تخمين الرقم!")
    print(f"أنا فكرت في رقم بين 1 و100، عندك {max_attempts} محاولات تخمنه.")

    while attempts < max_attempts:
        try:
            guess = int(input("خمن الرقم: "))
        except ValueError:
            print("من فضلك اكتب رقم صحيح!")
            continue

        attempts += 1

        if guess < secret_number:
            print("الرقم أكبر من كده ⬆️")
        elif guess > secret_number:
            print("الرقم أصغر من كده ⬇️")
        else:
            print(f"🎉 برافو! خمنت صح في المحاولة رقم {attempts}")
            return

    print(f"❌ خلصت المحاولات! الرقم كان {secret_number}")

if __name__ == "__main__":
    play_game()
