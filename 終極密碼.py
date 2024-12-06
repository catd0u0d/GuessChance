import random  # 引入隨機數
import re  # 引入正則表達式
from collections import deque  # 引入雙端隊列

game_records = deque(maxlen=10)  # 用於保存遊戲紀錄，最多10筆


#  檢查玩家名稱
def is_valid_name(name):
    if len(name) > 50:      # 若名稱過長，直接拒絕
        return False
    # 定義玩家名稱允許的範圍、長度 1 到 20
    pattern = re. compile("^[A-Za-z0-9\u4e00-\u9fff_.\/]{1,20}$")
    return bool(pattern.match(name)) and len(name.strip()) > 0


#  處理輸入和猜測
def get_valid_guess(guess_attempt, skip_count, max_skips=10):
    while True:
        guess_input = input(f'請猜測第 {guess_attempt} 次的數字：').strip()

        match guess_input:
            # 玩家按下 Enter 而未輸入內容
            case "":
                skip_count += 1
                print(f"您跳過了第 {skip_count} 次猜測！")

                if skip_count > max_skips:
                    print("您已達到跳過次數上限，遊戲結束！🚫")
                    return None, skip_count, True
                continue

            # 輸入有效數字範圍
            case _ if guess_input.isdigit() and 1 <= int(guess_input) <= 50:
                return int(guess_input), skip_count, False

            # 數字太長或不在範圍內
            case _ if guess_input.isdigit():
                print("請輸入 1 到 50 範圍內的數字。")
                continue

            # 無效輸入
            case _:
                print("無效輸入！請輸入一個有效的數字。")


#  遊戲玩法
def play_game():
    print('\n=============================')
    print("您好，歡迎來玩終極密碼！")
    print("\n範圍是 1 到 50，您有 5 次機會！")
    # 隨機生成答案，包含1和50
    answer = random.randint(1, 50)

    # 初始化遊戲
    correct = False
    guess_attempt = 0
    skip_count = 0

    for guessChance in range(5):
        guess_attempt = guessChance + 1

        # 獲取有效的猜測
        guess, skip_count, force_end = get_valid_guess(
            guess_attempt, skip_count)
        if force_end:
            return answer, False, guess_attempt  # 強制結束遊戲，返回結果

        # 給出提示
        match (guess < answer, guess > answer, guess == answer):
            case (False, False, True):
                print("Bingo！您答對了 🎉")
                correct = True
                break
            case (True, False, False):
                print('可惜猜錯了！答案比這個大哦。')
            case (False, True, False):
                print('可惜猜錯了！答案比這個小哦。')

    if not correct:
        print("\nGame Over！💀 遊戲結束了...正確答案是", answer)

    # 返回遊戲結果
    return answer, correct, guess_attempt if correct else None


#  遊戲流程
def main():
    total_games_played = 0
    max_games = 50  # 限制最多玩 50 局

    while total_games_played < max_games:
        # 要求玩家輸入名稱，並檢查是否合法
        while True:
            print("請輸入您的名稱：（長度最多 20字）")
            player_name = input().strip()
            player_name = player_name.replace(" ", "")  # 去除多餘的空格
            if is_valid_name(player_name):
                break  # 名稱合法
            else:
                # 名稱不合法
                print("不能用這個名字喔！請輸入有效的名稱。（只能包含字母、數字、中文、底線、點和斜線）")

        answer, correct, guess_attempt = play_game()

        result = {
            "名稱": player_name,
            "答案": answer,
            "結果": "答對" if correct else "答錯",
            "次數": guess_attempt if correct else "N/A"
        }
        game_records.append(result)

        # 顯示遊戲紀錄
        print('\n===========================\n遊戲紀錄（最近 10 筆）：')
        for idx, record in enumerate(game_records, start=1):
            print(f"{idx}. 玩家: {record['名稱']} | 答案: {record['答案']} | 結果: {
                  record['結果']} | 次數: {record['次數']}")

        # 是否再玩一次
        play_again = input("\n是否想要再玩一次？ (y/n): ").strip().lower()
        if play_again != 'y':
            print("\n謝謝遊玩！下次再見 👋")
            break

        total_games_played += 1

    if total_games_played >= max_games:
        print("📢 無與倫比的成就！您已達到遊戲次數上限，謝謝遊玩！\n下次再見 👋")


if __name__ == '__main__':
    main()
