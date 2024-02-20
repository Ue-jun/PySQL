#!/usr/local/bin/python3.7
from wsgiref.handlers import CGIHandler
from PySQL import app
CGIHandler().run(app)
# 回避用コメント