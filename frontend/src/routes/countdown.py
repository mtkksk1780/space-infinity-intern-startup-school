from fasthtml import FastHTML
from fasthtml.common import *
from components.header import header_html
from components.footer import footer_html

def create_count_down_page():
    return """
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Countdown Page</title>
        <style>
            body {
                text-align: center;
                font-family: Arial, sans-serif;
                background-image: url('/static/images/countdown/Group_22.png');
                background-size: contain;  /* 画像全体を表示 */
                background-position: top;  /* 上部分をしっかり表示 */
                background-repeat: no-repeat;
                background-attachment: fixed;  /* スクロール時に背景が固定される */
                color: white;
                min-height: 100vh;  /* ページ全体の高さを確保 */
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
            }
            #countdown {
                font-size: 3rem;
                font-weight: bold;
                margin-top: 20px;
            }
            .button-container {
                margin-top: 20px;
            }
            button {
                font-size: 1.2rem;
                padding: 10px 20px;
                margin: 5px;
                cursor: pointer;
                background-color: white;
                border: none;
                border-radius: 5px;
            }
        </style>
    </head>
    <body>
        <h1>DEMO DAY COUNTDOWN</h1>
        <div id="countdown">Let's get started!</div>
        <div class="button-container">
            <button onclick="startCountdown()">Start</button>
            <button onclick="resetCountdown()">Reset</button>
        </div>
        <script>
            let targetTime = null;
            let interval = null;
            function updateCountdown() {
                if (!targetTime) return;
                const now = new Date();
                const diff = targetTime - now;
                if (diff <= 0) {
                    document.getElementById('countdown').innerHTML = "DEMO DAY HAS STARTED!";
                    clearInterval(interval);
                    return;
                }
                const days = Math.floor(diff / (1000 * 60 * 60 * 24));
                const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
                const seconds = Math.floor((diff % (1000 * 60)) / 1000);
                document.getElementById('countdown').innerHTML = `${days} DAYS ${hours}:${minutes}:${seconds}`;
            }
            function startCountdown() {
                if (interval) clearInterval(interval);  // 既存のカウントダウンをクリア
                const now = new Date();
                targetTime = new Date(now.getTime() + (3 * 24 * 60 * 60 * 1000)); // 現在時刻 + 3日
                updateCountdown();
                interval = setInterval(updateCountdown, 1000);
            }
            function resetCountdown() {
                clearInterval(interval);
                targetTime = null;
                document.getElementById('countdown').innerHTML = "Countdown was reset";
            }
        </script>
    </body>
    </html>
    """