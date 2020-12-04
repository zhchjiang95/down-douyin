#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import os
import datetime
import json
from requests_html import HTMLSession

date = datetime.datetime.now()

dir = os.path.abspath('.')
# 时间作为文件名
work_path = os.path.join(dir, str(date.year) + str(date.month) + str(date.day) + str(date.hour) + str(date.minute) + str(date.second) + '.mp4')

# 定义ua，获取真实地址需要
ua_phone = 'Mozilla/5.0 (Linux; Android 6.0; ' \
         'Nexus 5 Build/MRA58N) AppleWebKit/537.36 (' \
         'KHTML, like Gecko) Chrome/80.0.3987.116 Mobile Safari/537.36'


def down_douyin(dy_url):
  print('请稍候…')
  session = HTMLSession()
  re = session.get(dy_url)

  # 获取视频id
  print('获取id…')
  url_id = re.html.url.split('/')[5]

  # 获取链接信息，json格式
  url_json = session.get('https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=' + url_id)

  # 视频url
  print('获取视频地址…')
  v_url = json.loads(url_json.html.html)['item_list'][0]['video']['play_addr']['url_list'][0]

  # 重定向后的真实地址
  print('解析地址…')
  xg_url = session.get(v_url.replace('playwm', 'play'), headers={ 'User-Agent': ua_phone })

  # 下载
  print('正在下载…')
  urllib.request.urlretrieve(xg_url.url, work_path)
  print('下载完成！（文件位于当前目录下）')

# 用户输入
dy_url = input('请输入抖音分享链接（如：https://v.douyin.com/JCpaNyB/）：')

if dy_url:
  down_douyin(dy_url)
else:
  print('未输入！！')
