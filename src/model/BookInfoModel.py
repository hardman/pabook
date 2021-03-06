#coding=utf-8

from src.utils import Utils

from Common import *

class BookInfoModel:
    def __init__(self):
        self.clickCount = -1;#点击数
        self.monthClickCount = -1;#月点击数
        self.weekClickCount = -1;#周点击数
        self.collectionCount = -1;#收藏数
        self.recommendCount = -1;#推荐数
        self.monthRecommendCount = -1;#月推荐数
        self.weekRecommendCount = -1;#周推荐数
        self.status = BookInfoStatus.Completed;#状态

        self.wordsCount = -1;#字数
        self.category = "";#分类名称
        self.title = "";#书名
        self.author = "";#作者
        self.des = "";#简介
        self.updateTime = -1;#更新时间
        self.chapterCount = -1;#最新章节
        self.bookImg = "";#图片

        self.downBookUrl = "";
        self.downMuluUrl = "";
        self.uniqueKey = "";
        self.downloadStatus = BookDownloadStatus.Ongoing;

        self.bookId = -1;

    def setUniqueKey(self):
        self.uniqueKey = Utils.md5str(self.category + self.title + self.author);

    def applyDict(self, d):
        attrnames = dir(self);
        for key, value in d.items():
            if key in attrnames:
                setattr(self, key, value);

    def _check(self, attrname, l):
        value = getattr(self, attrname);
        if value != None and len(value) > l:
            setattr(self, attrname, value[:l]);

    def check(self):
        self._check("title", 32);
        self._check("author", 8);
        self._check("des", 512);
        self._check("bookImg", 256);
        self._check("downBookUrl", 256);
        self._check("downMuluUrl", 256);

    def toDict(self, ignoreEmptyStr):
        attrnames = dir(self);
        d = {};
        for n in attrnames:
            if not n.startswith("_") and n != "toDict" and n != "setUniqueKey" and n != "applyDict" and n != "check":
                v = getattr(self, n);
                if isinstance(v, str):
                    if not ignoreEmptyStr or len(v) > 0:
                        d[n] = v;
                else:
                    d[n] = v;
        return d;

    def __str__(self):
        return str(self.toDict(False));