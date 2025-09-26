```py
import requests
import json

# 你的 Slack webhook URL，注意要放自己的，别泄漏！
url = 'https://hooks.slack.com/services/T0SEVS2SG/xxxx/xxx'

# 你的消息内容，可以是 text 或 blocks
payload = {
    "text": "Hello from Python! 🚀"
    # 或复杂一点：blocks: [...]
}

# 如果你想发 block 格式就：
# payload = {...跟你 Apps Script 里的 block 对应的内容...}

headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=json.dumps(payload), headers=headers)

if response.status_code == 200:
    print('Message sent!')
else:
    print(f"Failed: {response.status_code} - {response.text}")
```
