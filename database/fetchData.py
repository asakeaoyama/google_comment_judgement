import requests 
import json
import csv


urlSet = []
# 開啟 CSV 檔案
with open('urlSet.csv', newline='') as csvfile:

    # 讀取 CSV 檔案內容
    rows = csv.reader(csvfile)

    # 以迴圈輸出每一列
    for row in rows:
        if len(row) > 0: urlSet.append(row[0])

c = 0
for url in urlSet:
    c += 1
    print("Line", c)
    # 發送get請求
    text = requests.get(url).text
    # 取代掉特殊字元
    pretext = ')]}\''
    text = text.replace(pretext,'')
    # 把字串讀取成json
    soup = json.loads(text)

    # 取出包含留言的List 。
    # conlist[[rate, comment]]
    conlist = []
    for i in range(10):
        conlist.append([soup[2][i][0][2][0][0], soup[2][i][0][2][1][0].replace('\n', ' ')])


    # 開啟輸出的 CSV 檔案
    with open('commentData.csv', 'a', newline='') as csvfile:
        # 建立 CSV 檔寫入器
        writer = csv.writer(csvfile)
        # 逐筆抓出
        for i in conlist:
            print("rate:", i[0])
            print("comment:" + str(i[1]))

            # Good Comment
            if int(i[0]) == 5:
                # 寫入一列資料
                writer.writerow(["1", i[1]])
            # Bad Comment
            elif int(i[0]) < 4:
                writer.writerow(["0", i[1]])




