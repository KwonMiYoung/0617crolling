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
















