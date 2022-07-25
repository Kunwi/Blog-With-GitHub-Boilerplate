# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/Myblog/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = "Galileo"
enable_jsdelivr = {
    "enabled": False,
    "repo": "Kunwi/Myblog@gh-pages"
}

# 站点设置
site_name = "Kunwi's Blog"
site_logo = "${static_prefix}logo.png"
site_build_date = "2021-11-16T00:52+08:00"
author = "Kunwi Teh"
email = "seesgyy@gmail.com"
author_homepage = "/"
description = "Nothing in life is to be feared, it is only to be understood."
key_words = ['Maverick', 'Kunwi', '游记', '评测','随感']
language = 'zh-CN'
external_links = [
    {
        "name": "TapTap",
        "url": "https://www.taptap.com/user/5704888",
        "brief": "游戏评测"
    },
    {
        "name": "Steam",
        "url": "https://steamcommunity.com/profiles/76561198345862576/recommended/",
        "brief": "游戏评测"
    },
    {
        "name": "goodreads",
        "url": " https://www.goodreads.com/kunwi",
        "brief": "读书记录"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "GitHub",
        "url": "https://github.com/Kunwi",
        "icon": "gi gi-github"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
