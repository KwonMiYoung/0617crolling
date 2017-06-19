"""

from collections import Counter
import string
import math
nt = 0

INPUT_FILE_NAME = 'cleaned_output2.txt'


list=['IoT','구글','자율주행차','알파고','통신']
IT_news_category=[]

read_file = open(INPUT_FILE_NAME, 'r')
text = read_file.readline()  # txt file change encoding

IT_news=text

for i in range (0,5):
    df = IT_news.find(list[i])
    print(df)
    if(df!=-1):
        IT_news_category=INPUT_FILE_NAME
        print(list[i]) #단어 없으면 df=-1 로 저장됨
    print(IT_news_category)

"""

from collections import Counter
import string
import math
import crolling_news


INPUT_FILE_NAME = 'cleaned_output2.txt'

# 출력 파일 명
OUTPUT_FILE_NAME = 'IT_news.txt'
write_file = open(OUTPUT_FILE_NAME, 'w')

# 메인 함수
def main():
    nt = 0



    list1=['IoT','구글','자율주행차','알파고','통신','삼성','애플','아이폰','AI','로봇','네이버','퀄컴','인공지능','스마트폰','해킹','랜선','스마트','방송','LG','SKT','디지털',
           '아마존','온라인']
    IT_news_category=[]

    read_file = open(INPUT_FILE_NAME, 'r')
    text = read_file.readline()  # txt file change encoding

    IT_news=text

    for i in range (0,22):
        df = IT_news.find(list1[i])

        if(df!=-1):  #IT news 찾았을 때
            write_file.write(str(crolling_news.URL))
            write_file.close()
            print("OUTPUT")
            print(crolling_news.URL)


if __name__ == "__main__":
    main()















