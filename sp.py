import pprint
import time
import requests
import csv


def getMoreInfo(link, query):
    pass_ticket = "XkpRiYXjy5FWOO9QzGzgR6WZyJ8VPkvBnOiCQ5/u2kvHaOjrkYy4LsoOREfr96rL"
    if query == 'ckxxwx':
        appmsg_token = "1147_0EZX1x28x8Fx7hZEbUsDkANS0RET8p7dVlssWU3MYvelrZj4W3kRBr72wik80LS-bbZaA4RM0oDJmW-I",
        phoneCookie = "rewardsn=; wxtokenkey=777; wxuin=2357978339; devicetype=Windows10x64; version=6304051b; lang=zh_CN; pass_ticket=XkpRiYXjy5FWOO9QzGzgR6WZyJ8VPkvBnOiCQ5/u2kvHaOjrkYy4LsoOREfr96rL; appmsg_token=1147_0EZX1x28x8Fx7hZEbUsDkANS0RET8p7dVlssWU3MYvelrZj4W3kRBr72wik80LS-bbZaA4RM0oDJmW-I; wap_sid2=COPJr+QIEooBeV9ISVFoUmxxekotVllZcHJ4Y1BzaV9qWDF1TW5xdUxKS3hLN0pCTGxoWnNLU1VBSjM1ZVZ3bXBJTG9YcXJLUmNHZGU4S2s0WUZ2UzlCWUVMeUxmUmRsZDBPSHhSYWw1WXVsN01xZFRFQTdDcFFCRU1ENXcyQlJlY19hcHhHX2owbzNsa1NBQUF+MOz9644GOA1AAQ=="
    mid = link.split("&")[1].split("=")[1]
    idx = link.split("&")[2].split("=")[1]
    sn = link.split("&")[3].split("=")[1]
    _biz = link.split("&")[0].split("_biz=")[1]

    # 目标url
    url = "http://mp.weixin.qq.com/mp/getappmsgext"
    # 添加Cookie避免登陆操作，这里的"User-Agent"最好为手机浏览器的标识
    headers = {
        "Cookie": phoneCookie,
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.1021.400 QQBrowser/9.0.2524.400"
    }

    # 添加data，`req_id`、`pass_ticket`分别对应文章的信息，从fiddler复制即可。
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

    # 使用post方法进行提交
    content = requests.post(url, headers=headers, data=data, params=params).json()

    # 提取其中的阅读数和点赞数
    if 'appmsgstat' in content:
        readNum = content["appmsgstat"]["read_num"]
        likeNum = content["appmsgstat"]["like_num"]
    else:
        print('请求参数过期！')

    # 歇10s，防止被封
    time.sleep(10)
    return readNum, likeNum
f = open('公众号文章.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['标题', '文章发布时间', '阅读'])
csv_writer.writeheader()

for page in range(0, 40, 5):
    url = f'https://mp.weixin.qq.com/cgi-bin/appmsg?action=list_ex&begin={page}&count=5&fakeid=MzU2MzczODk5Mw==&type=9&query=&token=917232029&lang=zh_CN&f=json&ajax=1'
    headers = {
        'cookie': 'RK=irC949kbEr; ptcz=c1fef67b4821d694549d63523b83eec986e2e404e043e3d7898f96dd533c60c1; tvfe_boss_uuid=36f3eb687a3819e1; pgv_pvid=776247440; fqm_pvqid=77f20b09-dee2-41cb-9220-ea30bf226287; luin=o1821383696; lskey=00010000224ca8d172eb24494c6a117f968be60dacb60e3fb919497601c43010af01ebb56047e9f1f9299be0; ua_id=hrHgN0bnEnpweY4QAAAAANmSYNBFnaHNtwqMsgL7_zQ=; wxuin=41730003600153; bizuin=3864731929; noticeLoginFlag=1; remember_acct=1821383696%40qq.com; rand_info=CAESIAmzqjCHi+GOqowwmMamkWssUa1iO+lCxvNom0OpvY9a; slave_bizuin=3864731929; data_bizuin=3864731929; data_ticket=qTWfszpInHyXKxJ5Ds2wxkEFJggVLE4aaHYOYRysKcBlJTx19/4GwwmAXlaU9ivC; slave_sid=WEVJU3g0THZCb3puSnRHT0xLX0FmdzFqVTJXcWNBak5pdDhHaHJnSTF6c2xXdFI5Y0xmQlFkR0ptQjZrbkl6eGhHN3VHVzNLUTZIMzBvQ1NoZWVjTGNRc2R1d0hiQm5xMnFHT0xwTEZIazBEQ3liS2x0dUgweTEwbzNra25pemVFczNBVnlLT2lwNTVNa29k; slave_user=gh_90e67dbbe971; xid=81eddf5741071c33622c2255ef1c66ad; openid2ticket_oGSFb5r2nDQIulijwis0rQMMoBuc=SQEZ9EIjYtK4N1hMzZj3O+xf5P+SaOQq3vUHQvyhHWg=; mm_lang=zh_CN',
        'referer': 'https://mp.weixin.qq.com/cgi-bin/appmsg?t=media/appmsg_edit_v2&action=edit&isNew=1&type=77&createType=0&token=917232029&lang=zh_CN',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
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

        readNum,likeNum = getMoreInfo(link_url,'ckxxwx')
        dit = {
            '标题': title,
            '文章发布时间': otherStyleTime,
            # '文章地址': link_url,
            '阅读': readNum,
        }
        csv_writer.writerow(dit)
        print(dit)


