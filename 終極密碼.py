import random
import re
from collections import deque

# 遊戲常量
MAX_RECORDS = 10
MAX_GAMES = 50
MAX_NAME_LENGTH = 20
NUMBER_RANGE = (1, 50)
MAX_SKIPS = 10
MAX_ATTEMPTS = 5

# 遊戲紀錄
game_records = deque(maxlen=MAX_RECORDS)

def normalize_title(title):
    """標準化名稱：移除多餘空白"""
    return title.strip().replace(" ", "")

def is_valid_name(name):
    """檢查名稱是否合法"""
    if len(name) > MAX_NAME_LENGTH:
        return False
    pattern = re.compile(r"^[A-Za-z0-9一-鿿_.\\/]+$")
    return bool(pattern.match(name))

def get_valid_guess(attempt, skips, max_skips):
    """獲取有效的玩家猜測"""
    while True:
        guess = input(f"請猜測第 {attempt} 次的數字：").strip()
        match guess:
            case "":
                skips += 1
                print(f"您跳過了第 {skips} 次猜測！")
                if skips > max_skips:
                    print("🚫 已達跳過次數上限，遊戲結束！ You skipped too many times ...")
                    return None, skips, True
                continue
            case _ if guess.isdigit() and NUMBER_RANGE[0] <= int(guess) <= NUMBER_RANGE[1]:
                return int(guess), skips, False
            case _:
                print(f"請輸入 {NUMBER_RANGE[0]} 到 {NUMBER_RANGE[1]} 範圍內的有效數字。")

def play_game():
    """進行遊戲"""
    print("\n=============================")
    print("歡迎來玩終極密碼！Welcome to GuessChance！")
    print(f"範圍是 {NUMBER_RANGE[0]} 到 {NUMBER_RANGE[1]}，您有 {MAX_ATTEMPTS} 次機會！")
    print(f"To get the Password！ The range is {NUMBER_RANGE[0]} to {NUMBER_RANGE[1]} and You have {MAX_ATTEMPTS} chances to WIN！")

    random.seed()
    answer = random.randint(*NUMBER_RANGE)
    correct = False
    skips = 0

    for attempt in range(1, MAX_ATTEMPTS + 1):
        guess, skips, force_end = get_valid_guess(attempt, skips, MAX_SKIPS)
        if force_end:
            return answer, False, attempt

        match (guess < answer, guess > answer, guess == answer):
            case (False, False, True):
                print("🎉 您答對了！Bingo！Congrats on getting the password! 🎉")
                correct = True
                break
            case (True, False, False):
                print("答案比這個大哦！Bigger")
            case (False, True, False):
                print("答案比這個小哦！Smaller")

    if not correct:
        print(f"💀 遊戲結束！正確答案是 {answer} Game Over！YOU LOSS！")

    return answer, correct, attempt if correct else None

def display_game_records(records):
    """顯示遊戲紀錄"""
    print("\n===========================")
    print("遊戲紀錄（最近 10 筆）：")
    print(f"{'序號':<4}{'玩家':^14}{'答案':^8}{'結果':<8}{'次數':<8}")
    print("=" * 42)
    for idx, record in enumerate(records, start=1):
        print(f"{idx:<4}{record['名稱']:^14}{record['答案']:^8}{record['結果']:<8}{record['次數']:<8}")

def main():
    """主程式入口"""
    total_games_played = 0

    while total_games_played < MAX_GAMES:
        while True:
            player_name = normalize_title(input("請輸入您的名稱 Please enter your name："))
            if is_valid_name(player_name):
                break
            print("⚠️ 無效名稱！請輸入有效名稱（限字母、數字、中文、底線等 Allows Letters, Numbers, Chinese, Underline）。")

        answer, correct, attempts = play_game()

        record = {
            "名稱": player_name,
            "答案": answer,
            "結果": "答對" if correct else "答錯",
            "次數": attempts if correct else "N/A"
        }
        game_records.append(record)

        display_game_records(game_records)

        if input("\n是否再玩一次？Play Again？(y/n): ").strip().lower() != 'y' or 'yes':
            print("\n謝謝遊玩！下次再見 Seeya 👋")
            break

        total_games_played += 1

    if total_games_played >= MAX_GAMES:
        print("🎉 您已達到遊戲上限，感謝您的遊玩，下次再見！ Unparalleled Achievement, You have reached the game limit, thanks for playing !🎉")

if __name__ == '__main__':
    main()
