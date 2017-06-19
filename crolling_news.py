"""네이버 뉴스 기사 웹 크롤러 모듈"""
from bs4 import BeautifulSoup
import urllib.request
import lxml

import cleaned_txt
import top_keyword
import cleaned_output2
import list
import sys

# 출력 파일 명
OUTPUT_FILE_NAME = 'output1.txt'
# 긁어 올 URL

#URL = 'http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=105&oid=022&aid=0003184019'
print("URL을 입력하시오 : ")
URL = input()

# 크롤링 함수
def get_text(URL):
    source_code_from_URL = urllib.request.urlopen(URL)
    soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')
    text = ''
    for item in soup.find_all('div', id='articleBodyContents'):   ##daum은 id : news_view
        text = text + str(item.find_all(text=True))
    return text


# 메인 함수
def main():

        open_output_file = open(OUTPUT_FILE_NAME, 'w')
        result_text = get_text(URL)
        open_output_file.write(result_text)
        open_output_file.close()
        cleaned_txt.main()
        top_keyword.main()
        cleaned_output2.main()
        list.main()



if __name__ == "__main__":
    main()
