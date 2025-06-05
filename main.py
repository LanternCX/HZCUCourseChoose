import time
import random
import requests

url = "http://ijw.hzcu.edu.cn/xsxk/zzxkyzb_cxXkTitleMsg.html?gnmkdm=N253512"
cookies = {
    "route": "6eff09e6c2dd246d9567fcfd5e531b9a",
    "JSESSIONID": "7B92B99953DE8F407EE42ADB719C0C5A"
}
name = {
    "09AF9D6DB3ED03CEE063BDB73D0A68A3": "中国古代陶瓷",
}
courses = [
    {
        "jxb_ids": "6b5e16e9180a17b1dac98ef33f03958e379ccdb73c46f655700c5ddcf765c9f6b4e9d1c13cf2468a8754d18b0303d9363c9212a337d67aee33bb10bcb9d0e5a2aa062ee85a4d729f717a5b06841bb26ccfafcd63afa4cafa02e47f798f065f26590d4a31894c190c53d59aaed81400c14805d0dccec03a8750e4667786c7ff4a",
        "kch_id": "09AF9D6DB3ED03CEE063BDB73D0A68A3"
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
                print(f"请求 kch_id={course['kch_id']} 时发生错误: {e}")
