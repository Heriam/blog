#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# 网站信息
AUTHOR = u'Justin C.'
SITENAME = u'Heriam'
SITEURL = u'https://jiang-hao.com'
TIMEZONE = 'Asia/Shanghai'
DEFAULT_DATE_FORMAT = '%Y-%m-%d %a'

# 生成配置
PATH = 'content'
OUTPUT_PATH = 'output'
PAGE_PATHS = ['pages']
PAGE_EXCLUDES = []
ARTICLE_PATHS = ['articles']
ARTICLE_EXCLUDES = []
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = [".git"]
USE_FOLDER_AS_CATEGORY = True
OUTPUT_SOURCES = False
READERS = {'html': None}
TYPOGRIFY = True
STATIC_PATHS = ['extra']
EXTRA_PATH_METADATA = {
        'extra/CNAME': {'path': 'CNAME'},
        'extra/favicon.ico': {'path': 'favicon.ico'},
        }
SLUGIFY_SOURCE = 'title'
DEFAULT_DATE = 'fs'
DIRECT_TEMPLATES = ['tags', 'categories', 'authors', 'archives']

# Markdown扩展
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.tables': {  # 表格
        },
        'markdown.extensions.toc': {     # 目录，设置看https://python-markdown.github.io/extensions/toc/
            'title': 'Table of Contents',      # 目录题头
        },
    },
    'output_format': 'html5',
}


# 页面显示
SUMMARY_MAX_LENGTH = 50
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DEFAULT_ORPHANS = 0
DEFAULT_PAGINATION = 10
NEWEST_FIRST_ARCHIVES = True

# 主题/插件
THEME = 'tuxlite_tbs'
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['extract_toc']

# URL设置
RELATIVE_URLS = True
FILENAME_METADATA = '(?P<slug>.*)'
DRAFT_URL = 'drafts/articles/{slug}.html'
DRAFT_SAVE_AS = DRAFT_URL
ARTICLE_URL = 'articles/{date:%Y}/{category}-{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
DRAFT_PAGE_URL = 'drafts/pages/{slug}.html'
DRAFT_PAGE_SAVE_AS = DRAFT_PAGE_URL
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = PAGE_URL
CATEGORY_URL = 'categories/{slug}.html'
CATEGORY_SAVE_AS = CATEGORY_URL
CATEGORIES_SAVE_AS = 'categories/index.html'
TAG_URL = 'tags/{slug}.html'
TAG_SAVE_AS = TAG_URL
TAGS_SAVE_AS = 'tags/index.html'
AUTHOR_URL = 'authors/{slug}.html'
AUTHOR_SAVE_AS = AUTHOR_URL
AUTHORS_SAVE_AS = 'authors/index.html'
YEAR_ARCHIVE_URL = 'articles/{date:%Y}/index.html'
YEAR_ARCHIVE_SAVE_AS = YEAR_ARCHIVE_URL
ARCHIVES_URL = 'articles/index.html'
ARCHIVES_SAVE_AS = ARCHIVES_URL
DEFAULT_LANG = u'zh_CN'
DEFAULT_CATEGORY = 'uncategorized'

# Feed generation is usually not desired when developing
FEED_DOMAIN = None
FEED_ATOM = None
FEED_ALL_ATOM = None
FEED_ATOM_URL = None
FEED_RSS = None
FEED_RSS_URL = None
FEED_ALL_ATOM_URL = None
FEED_ALL_RSS = None
FEED_ALL_RSS_URL = None
CATEGORY_FEED_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None

# Blogroll
LINKS_WIDGET_NAME = 'LINKS'
LINKS = (('iMooC', 'http://www.imooc.com/'),
         ('w3schools', 'http://www.w3schools.com/'),
         ('Cisco Lab', 'https://developer.cisco.com/'),
         ('Coursera', 'https://www.coursera.org/'),
         ('RUNOOB', 'http://www.runoob.com/')
         )

# Social widget
SOCIAL_WIDGET_NAME = 'SOCIAL'
SOCIAL = (('Facebook','https://www.facebook.com/hao.zju'),
		  ('Weibo', 'http://weibo.com/207575725'),
          ('Linkedin', 'http://www.linkedin.com/in/haochiang'),
          ('Github','https://github.com/Heriam'),
          ('Qyer', 'http://www.qyer.com/u/5831110/plan')
          )
		  
MENUITEMS = (
  ('Archives','/articles'),
  ('Tags','/tags'),
  ('Publications','/pages/publications'),
)



