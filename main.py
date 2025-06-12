import time
import random
import requests

# 目标 URL
url = "http://ijw.hzcu.edu.cn/xsxk/zzxkyzbjk_xkBcZyZzxkYzb.html?gnmkdm=N253512"

# 请求头
headers = {
    "Proxy-Connection": "keep-alive",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                  " (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "Origin": "http://ijw.hzcu.edu.cn",
    "Referer": "http://ijw.hzcu.edu.cn/xsxk/zzxkyzb_cxZzxkYzbIndex.html?doType=details&gnmkdm=N253512&layout=default",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
}

# Cookies
cookies = {
    "route": "aaa",
    "JSESSIONID": "aaa"
}

# 要刷选的课程列表，每个字典包含完整的表单字段
courses = [
    {
        "jxb_ids": "319BE2E2E6D4BEC3E063BDB73D0A817E",
        "kch_id": "16BF9C9EFD249E1EE063BDB73D0A0EB9",
        "kcmc": "(D13002)文化与旅游 - 2.0 学分",
        "rwlx": "2",
        "rlkz": "0",
        "cdrlkz": "0",
        "rlzlkz": "1",
        "sxbj": "1",
        "xxkbj": "0",
        "qz": "0",
        "cxbj": "0",
        "xkkz_id": "3737E7E5EF1B9EA6E063BDB73D0AFEFF",
        "njdm_id": "2024",
        "zyh_id": "20E28528D2959F63E063BDB73D0AA904",
        "kklxdm": "10",
        "xklc": "2",
        "xkxnm": "2025",
        "xkxqm": "3",
        "jcxx_id": ""
    }
]

if __name__ == "__main__":
    print("开始模拟课程选课请求，按 Ctrl+C 停止...")
    while True:
        for course in courses:
            try:
                # 随机延迟，模拟人为操作
                delay = random.uniform(0.1, 0.5)
                print(f"等待 {delay:.2f} 秒后发送请求 for kch_id={course['kch_id']}...")
                time.sleep(delay)

                # 发送 POST 请求
                response = requests.post(url, data=course, headers=headers, cookies=cookies, timeout=10)

                # 打印日志
                print(f"课程: {course['kcmc']}, 状态码: {response.status_code}, 响应: {response.text[:200]}...\n")

            except requests.exceptions.RequestException as e:
                print(f"请求课程 {course['kch_id']} 时发生网络错误: {e}")
            except Exception as e:
                print(f"处理课程 {course['kch_id']} 时发生错误: {e}")