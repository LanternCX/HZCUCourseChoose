import time
import random
import requests

url = "https://ijw.hzcu.edu.cn/xsxk/zzxkyzbjk_xkBcZyZzxkYzb.html?gnmkdm=N253512"
cookies = {
    "hb_MA-B8B4-DCBCC6752B4F_source": "",
    "route": "",
    "JSESSIONID": ""
}
name = {
    "kch_id": "name",
}
courses = [
    {
        "jxb_ids": "",
        "kch_id": "",
        "qz": 0
    }
]

if __name__ == "__main__":
    while True:
        for course in courses:
            try:
                delay = random.uniform(0, 2 / len(courses))
                print(f"等待 {delay:.2f} 秒后发送请求...")
                time.sleep(delay)
                response = requests.post(url, data=course, cookies=cookies)
                print(f"kch_id={name[course['kch_id']]}, 状态码: {response.status_code}, 响应内容: {response.text[:100]}")
            except Exception as e:
                print(f"请求 kch_id={course[kch_id]} 时发生错误: {e}")
