#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Justin C.'
SITENAME = u'Heriam'
SITEURL = u'http://www.jiang-hao.com'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

THEME = 'tuxlite_tbs'

FILENAME_METADATA = '(?P<slug>.*)'

ARCHIVES_URL = 'pages/archives.html'
ARCHIVES_SAVE_AS = ARCHIVES_URL
ARTICLE_URL = 'pages/{category}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = PAGE_URL
CATEGORY_URL = 'pages/{slug}/index.html'
CATEGORY_SAVE_AS = CATEGORY_URL
TAG_URL = 'tags/{slug}.html'
TAG_SAVE_AS = TAG_URL
DEFAULT_LANG = u'zh_CN'
DEFAULT_CATEGORY = 'uncategorized'

RELATIVE_URLS = True
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
USE_FOLDER_AS_CATEGORY = True
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = [".git"]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('iMooC', 'http://www.imooc.com/'),
         ('w3schools', 'http://www.w3schools.com/'),
         ('Cisco Lab', 'https://developer.cisco.com/'),
         ('Coursera', 'https://www.coursera.org/'),
         ('RUNOOB', 'http://www.runoob.com/')
         )


# Social widget
SOCIAL = (('Facebook','https://www.facebook.com/hao.zju'),
		  ('Weibo', 'http://weibo.com/207575725'),
          ('Linkedin', 'http://www.linkedin.com/in/haochiang'),
          ('Github','https://github.com/Heriam'),
          ('Qyer', 'http://www.qyer.com/u/5831110/plan')
          )
		  
MENUITEMS = (
  ('出版','/pages/publications'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
        'extra/CNAME': {'path': 'CNAME'},
        'extra/favicon.ico': {'path': 'favicon.ico'},
        }

