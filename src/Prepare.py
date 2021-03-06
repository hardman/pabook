#coding=utf-8

from optparse import OptionParser

import os

import urlparse

from src.utils import Utils, Log

from Config import Config

from src.parser import ParserFactory

class Prepare:
    def __init__(self):
        self.onPrepare();

    def createParser(self):
        #创建parser
        parserName = Config.shared.parserName;
        parser = ParserFactory.shared.get(parserName);

        if not parser: 
            raise Exception("parser cant init");

        if Config.shared.parseType == "all":
            parser.execute();
        else:
            parser.downloadBook(Config.shared.url);

    def onPrepare(self):
        self.createParser()

    def test(self):
        Log.test();


