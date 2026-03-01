@echo off
cd /d "c:\Users\integ\OneDrive\デスクトップ\ling-ling-etymon"

echo --- [1/3] 単語を生成中... ---
python scripts\generate_etymology.py 10

echo --- [2/3] GitHubへアップロード準備中... ---
git add data.js essays.js

echo --- [3/3] 公開サイトを更新中... ---
git commit -m "Auto-update: New words/essays added via task scheduler"
git push origin main

echo --- 完了しました！ ---
