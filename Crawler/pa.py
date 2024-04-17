
# import requests
# from bs4 import BeautifulSoup
# import json

# def scrape_tarot_card_info(url):
#     response = requests.get(url)
#     response.encoding = 'utf-8'  # 根据网页的实际编码调整

#     soup = BeautifulSoup(response.text, 'html.parser')

#     # 提取所有文本信息
#     text = soup.get_text(separator='\n', strip=True)

#     # 组装数据
#     card_info = {
#         'url': url,
#         'text': text
#     }

#     return card_info

# # 爬取的网址
# url = 'https://www.23luke.com/taluobaojianpai/1153.html'

# # 爬取数据
# card_data = scrape_tarot_card_info(url)

# # 保存为JSON文件
# with open('tarot_card_data1.json', 'w', encoding='utf-8') as file:
#     json.dump(card_data, file, ensure_ascii=False, indent=4)

# print('数据已保存到tarot_card_data1.json')

import csv
import requests
from bs4 import BeautifulSoup
import json

def scrape_tarot_card_info(url):
    response = requests.get(url)
    response.encoding = 'utf-8'  # 根据网页的实际编码调整

    soup = BeautifulSoup(response.text, 'html.parser')

    # 提取所有文本信息
    text = soup.get_text(separator='\n', strip=True)

    # 组装数据
    card_info = {
        'url': url,
        'text': text
    }

    return card_info

# 基础URL和卡牌数量
base_url = 'https://www.23luke.com/taluobaojianpai/'
web_data_major = [1033, 1030, 1025, 1017,1014,1008,1003,994,963,607,604,593,588,586,581,577,573,564,559,553,542,532]  # major网站地址列表
web_data_cups = [1166, 1163,1113,1107,1105,1100,1098,1096,1093,1088,519,516,512,508]
web_data_swords = [1156,1153,1151,1148,1144,1142,1137,1133,1126,1120,487,484,479,469]
web_data_wands = [1185,1186,1187,1188,1189,1190,1171,1172,1173,1170,503,500,496,492]
web_data_pentacles =[1228,1227,1207,1208,1209,1210,1211,1212,1206,1205,460,456,445,441]

# card_count = 25  # 从0到21共22张卡牌

# # 循环爬取每张卡牌的信息
# for i in card_count:
#     url = f"{base_url}{i}.html/"
#     card_data = scrape_tarot_card_info(url)
#     all_cards_data.append(card_data)


# 存储所有卡牌信息的列表
all_cards_data = []

# 循环爬取每张卡牌的信息
for i in web_data_pentacles:
    url = f"{base_url}{i}.html"
    card_data = scrape_tarot_card_info(url)
    all_cards_data.append(card_data)

# 保存为CSV文件
csv_file = 'pentacles_cards_data.csv'
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # 写入卡牌数据
    for card in all_cards_data:
        writer.writerow([card['text']])

print('所有卡牌数据已保存')
