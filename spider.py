import pprint
import time
import requests
import csv

f = open('公众号文章.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['标题', '文章发布时间', '阅读'])
csv_writer.writeheader()

for page in range(0, 365, 5):
    url = f'https://mp.weixin.qq.com/cgi-bin/appmsg?action=list_ex&begin={page}&count=5&fakeid=MzU2MzczODk5Mw==&type=9&query=&token=1772436253&lang=zh_CN&f=json&ajax=1'
    headers = {
        'cookie': 'RK=irC949kbEr; ptcz=c1fef67b4821d694549d63523b83eec986e2e404e043e3d7898f96dd533c60c1; tvfe_boss_uuid=36f3eb687a3819e1; pgv_pvid=776247440; fqm_pvqid=77f20b09-dee2-41cb-9220-ea30bf226287; luin=o1821383696; lskey=00010000224ca8d172eb24494c6a117f968be60dacb60e3fb919497601c43010af01ebb56047e9f1f9299be0; ua_id=hrHgN0bnEnpweY4QAAAAANmSYNBFnaHNtwqMsgL7_zQ=; wxuin=41730003600153; uuid=add1a8cdef89fdb8907148b865d00f04; cert=EzHebBlmeNbqLJ03zkHVyqnAE8YyZ4b1; sig=h01e6d82884d3110ad2d67e601e4b7f42a553923ea68028f3f528507c70d6965f55ec11ae01fc72a24e; data_bizuin=3864731929; data_ticket=31FznXT1025cip0dk13JHaNr+g3ai+lPrJ/VP8aljHoQ8LomnF46I01FDxrszwE/; master_key=PjrJJY1K+lGyDDNVRj/SQgOp/OHcvuEc4OlRRGcoQ5Q=; master_user=gh_90e67dbbe971; master_sid=cjNPZW9jcXQyVTB5M1VyNUlrMHZyVzVEbXZoOGVLZHp5TkJ2NDJBMnljZmdnMzFNSXRWVXR2cVAyUDRnSWc4V2tVMDcxR3ZUbWdBZ1p4ZENHUjdQdnJkVTRDSGtlYTc0dzZGa3AzTG9RUHhfZlpsQTlBOWUwb1k1NW53NVBjTTZqRlpXSHBqb3Nabm9sczlT; master_ticket=ce6e8e5d6dc7273fdf1849074c66990b; bizuin=3864731929; slave_user=gh_90e67dbbe971; slave_sid=U1R1U3hhN293cFpSZjBnZjF4MTNyakdoZFYyUVY4RTV2OF9IRHpubEVtNDAwZ0NvODl4VzJoMF9FMldIbThhTkdvNmNDYjF2cVZ4NmgxblRRMXFvT1FHYWpFRGx2VklSeHRqaTVhRlZlTF9nUF9odjdGV1VKaU1GTmdXZUxwVWdnNmlUY1ZuOVczdDlLQWt4; rewardsn=; wxtokenkey=777',
        'referer': 'https://mp.weixin.qq.com/cgi-bin/appmsg?t=media/appmsg_edit_v2&action=edit&isNew=1&type=10&createType=0&token=1252678642&lang=zh_CN',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6304051b)',
    }
    response = requests.get(url=url, headers=headers)
    html_data = response.json()
    pprint.pprint(response.json())
    lis = html_data['app_msg_list']

    for li in lis:
        title = li['title']
        link_url = li['link']
        update_time = li['update_time']
        timeArray = time.localtime(int(update_time))
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        mid = link_url.split("&")[1].split("=")[1]
        idx = link_url.split("&")[2].split("=")[1]
        sn = link_url.split("&")[3].split("=")[1]
        _biz = link_url.split("&")[0].split("_biz=")[1]
        appmsg_token = "1147_gDEpiMo69YB3k4iabUsDkANS0RET8p7dVlssWapTHZphKdERL5sxx4KpunkmclB - AHQgUzFYPvhoKSJG"
        pass_ticket = "QLREms00EMMDtZUI7a3srRKYNLDpkcRlJNyqdE6qz5fpQlfsT9yhZmtxJ82VhXAW"
        data = {
            "is_only_read": "1",
            "is_temp_url": "0",
            "appmsg_type": "9",
            'reward_uin_count': '0'
        }
        params = {
            "__biz": _biz,
            "mid": mid,
            "sn": sn,
            "idx": idx,
            "key": '777',
            "pass_ticket": pass_ticket,
            "appmsg_token": appmsg_token,
            "uin": '777',
            "wxtoken": "777"
        }
        content = requests.post(url, headers=headers, data=data, params=params).json()
        # 提取其中的阅读数和点赞数
        if 'appmsgstat' in content:
            readNum = content["appmsgstat"]["read_num"]
            print("阅读："+readNum)
            likeNum = content["appmsgstat"]["like_num"]
        else:
            print('请求参数过期！')
        dit = {
            '标题': title,
            '文章发布时间': otherStyleTime,
            # '文章地址': link_url,
            '阅读': readNum,
        }
        csv_writer.writerow(dit)
        print(dit)
