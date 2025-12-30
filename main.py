import time
import random
import requests
import json

# 目标 URL
url = "http://ijw.hzcu.edu.cn/xsxk/zzxkyzbjk_xkBcZyZzxkYzb.html?gnmkdm=N253512"

# 1. Cookies
cookies = {
    "JWTUser": "aaa",
    "route": "aaa",
    "JSESSIONID": "aaa"
}

# 2. 完全模拟请求头
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "Host": "ijw.hzcu.edu.cn",
    "Origin": "http://ijw.hzcu.edu.cn",
    "Proxy-Connection": "keep-alive",
    "Referer": "http://ijw.hzcu.edu.cn/xsxk/zzxkyzb_cxZzxkYzbIndex.html?doType=details&gnmkdm=N253512&layout=default",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36 Edg/143.0.0.0",
    "X-Requested-With": "XMLHttpRequest"
}

# 3. 待选课程列表
courses_to_snatch = [
    {
        "name": "创新创业基础",
        "data": {
            "jxb_ids": "42A6749D33584CD3E063BDB73D0A956E",
            "kch_id": "E00031",
            "kcmc": "(E00031)创新创业基础 - 2.0 学分",
            "rwlx": "2",
            "rlkz": "0",
            "cdrlkz": "0",
            "rlzlkz": "1",
            "sxbj": "1",
            "xxkbj": "0",
            "qz": "0",
            "cxbj": "0",
            "xkkz_id": "47175FFFE58189A2E063BDB73D0A1EDF",
            "njdm_id": "2024",
            "zyh_id": "0121",
            "kklxdm": "10",
            "xklc": "2",
            "xkxnm": "2025",
            "xkxqm": "12",
            "jcxx_id": ""
        }
    }
]


def snatch_with_json():
    print(f"🔥开始抢课🔥")

    session = requests.Session()
    # 将字典形式的 cookies 注入到 session 中
    session.cookies.update(cookies)

    attempt = 1
    while True:
        for course in courses_to_snatch:
            try:
                # 发送 POST 请求，Content-Length 会由 requests 自动计算
                response = session.post(url, data=course["data"], headers=headers, timeout=5)

                now = time.strftime("%H:%M:%S", time.localtime())
                print(f"[{now}] 轮次:{attempt} | 课程:{course['name']} | 状态码:{response.status_code}")

                if response.status_code == 200:
                    try:
                        result_json = response.json()
                        print(f"JSON 响应: {json.dumps(result_json, ensure_ascii=False)}")

                        # 如果教务系统返回特定的“抢课成功”标识，可以这里增加 break
                        if result_json.get("flag") == "1":
                            print("🎉 恭喜！抢课成功！")
                            # return

                    except Exception:
                        print(f"原始响应: {response.text[:100].strip()}")
                else:
                    print(f"请求失败，响应体: {response.text[:50]}")

                # 随机间隔 0.5 到 1 秒，防止被服务器识别为机器人
                time.sleep(random.uniform(0.1, 0.5))

            except Exception as e:
                print(f"⚠️ 网络连接异常: {e}")
                time.sleep(1)

        print("-" * 60)
        attempt += 1


if __name__ == "__main__":
    snatch_with_json()