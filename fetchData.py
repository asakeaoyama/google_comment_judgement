import requests 
import json

# 超連結
url = 'https://www.google.com/maps/rpc/listugcposts?authuser=0&hl=zh-TW&gl=tw&pb=!1m7!1s0x346e0f45b2c9a5f7%3A0x83aa3c36d06307!3s!6m4!4m1!1e1!4m1!1e3!2m2!1i10!2sCAESBkVnSUlDZw%3D%3D!3e1!5m2!1sygM1ZYnDAezg2roPxsi_sA0!7e81!8m5!1b1!2b1!3b1!5b1!7b1!11m10!1e3!2e1!3szh-TW!4stw!5m3!1s2024-01-20!3i3!4e3!6m1!1i2'
# 發送get請求
text = requests.get(url).text
# 取代掉特殊字元，這個字元是為了資訊安全而設定的喔。
pretext = ')]}\''
text = text.replace(pretext,'')
# 把字串讀取成json
soup = json.loads(text)

# 取出包含留言的List 。
# conlist[[rate, comment]]
conlist = []
for i in range(10):
    conlist.append([soup[2][i][0][2][0][0], soup[2][i][0][2][1][0]])

# 逐筆抓出
for i in conlist:
    print("rate:"+str(i[0]))
    print("comment:"+str(i[1]))