import random
import time

import requests

# 目标 URL
url = "http://ijw.hzcu.edu.cn/xsxk/zzxkyzbjk_xkBcZyZzxkYzb.html?gnmkdm=N253512"

# 1. 独立的 Cookies 字典
cookies = {
    "JWTUser": "",
    "route": "",
    "JSESSIONID": ""
}

# 2. 完全模拟的请求头
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

# 3. 完整的表单数据 (19个字段)
course_data = {
    "jxb_ids": "44DC4E8E055B53CFE063BDB73D0AB680",
    "kch_id": "0CFD1C4DBD881470E063BDB73D0A03EE",
    "kcmc": "(D70023)羽毛球Ⅰ - 1.0 学分",
    "rwlx": "2",
    "rlkz": "0",
    "cdrlkz": "0",
    "rlzlkz": "1",
    "sxbj": "1",
    "xxkbj": "0",
    "qz": "0",
    "cxbj": "0",
    "xkkz_id": "47175FFFE77389A2E063BDB73D0A1EDF",
    "njdm_id": "2024",
    "zyh_id": "0121",
    "kklxdm": "05",
    "xklc": "2",
    "xkxnm": "2025",
    "xkxqm": "12",
    "jcxx_id": ""
}


def run_task():
    # 使用 Session 管理会话
    session = requests.Session()
    session.cookies.update(cookies)

    attempt = 1
    while True:
        try:
            # 随机延迟，避免被系统识别为异常流量
            wait_time = random.uniform(0.2, 0.5)
            time.sleep(wait_time)

            # 发送 POST 请求
            response = session.post(
                url,
                data=course_data,
                headers=headers,
                timeout=10
            )

            now = time.strftime("%H:%M:%S", time.localtime())

            # 打印关键日志
            print(f"[{now}] 第 {attempt} 次尝试 | 状态码: {response.status_code}")
            print(f"响应内容: {response.text[:100]}...")

            # 业务逻辑判断
            if "成功" in response.text:
                print("🎉 抢课成功！正在退出...")
                break
            elif "重复" in response.text:
                print("🔔 提示：已选过该课或正在处理中。")
            elif "非法" in response.text or "登录" in response.text:
                print("❌ 警告：Cookie 可能已过期，请重新获取。")
                break

            attempt += 1

        except requests.exceptions.RequestException as e:
            print(f"❌ 网络异常: {e}")
            time.sleep(1)
        except Exception as e:
            print(f"❌ 运行错误: {e}")
            break


if __name__ == "__main__":
    run_task()
