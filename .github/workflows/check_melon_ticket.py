import time
import requests

# 設定你的演出、場次、座位 ID
PRODUCT_ID = "210858"   # 你的演出 ID
SCHEDULE_ID = "100001"  # 你的場次 ID
SEAT_ID = "157, 158, 160, 174, 175, 176, 177, 396, 398, 400, 402, 403, 404, 598, 599, 600, 601, 602, 604, 605, 607, 608, 609, 610, 614, 616, 617, 618, 621, 623, 653, 654, 656, 694, 709, 710, 711, 713, 737, 739, 740, 741, 742"  # 你的座位 ID

# LINE Notify 設定
LINE_ACCESS_TOKEN = "93FXd8FB5ziW5Vo8WXnjfjakytxzEQL7gZU4jCZDwmo"
LINE_NOTIFY_URL = "https://notify-api.line.me/api/notify"


def send_line_message(message):
    """ 發送 LINE 通知 """
    headers = {"Authorization": f"Bearer {LINE_ACCESS_TOKEN}"}
    data = {"message": message}
    response = requests.post(LINE_NOTIFY_URL, headers=headers, data=data)

    # 檢查回應狀態和內容
    print(f"Response status: {response.status_code}")
    print(f"Response content: {response.text}")

def check_ticket():
    """ 檢查票務狀態 """
    try:
        CHECK_URL = f"https://ticket.melon.com/api/product/{PRODUCT_ID}/schedule/{SCHEDULE_ID}/seat/{SEAT_ID}"
        response = requests.get(CHECK_URL)

        # 打印回應內容，看看它是不是 JSON 格式
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Content: {response.text}")

        # 檢查是否成功收到 JSON 格式的回應
        if "application/json" in response.headers.get("Content-Type", ""):
            data = response.json()
        else:
            print("收到的不是 JSON 格式的回應，可能是錯誤或 HTML 頁面。")
            return

        # 確保 API 返回的資料格式正確
        available = data.get("available", False)  # 假設 API 返回 {"available": True}

        if available:
            send_line_message("🎟️ 有票了！快去搶票！👉 https://tkglobal.melon.com/performance/index.htm?langCd=EN&prodId=210858")
        else:
            print("❌ 目前沒有票")
    except Exception as e:
        print(f"錯誤：{e}")

if __name__ == "__main__":
    while True:
        check_ticket()
        time.sleep(1)  # 每 1 秒檢查一次
