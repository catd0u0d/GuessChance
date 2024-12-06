終極密碼小遊戲
這是一款簡單有趣的終極密碼小遊戲，
玩家需在有限次數內猜出隨機生成的數字。
遊戲會記錄最近 10 局的遊戲紀錄，並以表格格式友善地顯示。
----------------------------------------------------------------------------------------------------------------------

功能特性
玩家名稱檢查：支援中文、英文、數字、底線（_）、點號（.）和斜線（/）。
隨機數字範圍：遊戲範圍為 1 到 50。
多次猜測：每局最多有 5 次猜測機會。
跳過次數限制：連續跳過猜測次數上限（預設 10 次）將結束遊戲。
友善的遊戲紀錄：顯示最近 10 局的遊戲結果，採用整齊的表格格式。
最大局數限制：最多可進行 50 局遊戲。

如何執行遊戲
確保已安裝 Python，並符合版本需求。
將使用終端機或命令提示字元執行

常見問題 (FAQ)
1. 為什麼名稱無法使用特殊字元？
為了確保遊戲紀錄的整潔與安全，名稱僅允許部分字元（英文字母、數字、中文、底線、點號和斜線）。

2. 是否可以修改隨機數範圍？
可以。在程式碼中修改 play_game() 函數中的 random.randint(1, 50) 範圍即可。

3. 跳過次數限制能否調整？
可以。在 get_valid_guess() 函數中調整 max_skips 參數的值。
