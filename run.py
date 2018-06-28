
#coding=utf-8

'''
1. 安装最新版本pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
2. pip install PyMySQL
3. brew install mysql
'''

'''
#安装美丽汤
sudo pip install beautifulsoup4
sudo pip install html5lib
sudo pip install lxml
'''

'''
#运行
python run.py -r "http://www.ybdu.com" -o ./out -p YbduParser -s FileStorge -a "helloworld"
'''

from src.utils import Utils

from src.db.BookinfoDb import BookinfoDb
from src.db.ChapterDb import ChapterDb

from src.utils.Aes import Aes

from src.Prepare import Prepare

from src.parser import BookId

def test():
	Utils.log("--test--");
	# dbins = BookinfoDb();
	# dbins.test();

	chapterDb = ChapterDb(101);
	chapterDb.test();

	# Aes.test();

	# BookId.test();

if __name__ == '__main__':
	test();
	# Prepare();
else:
	print("error");