# -*- coding: utf-8 -*-
from time import sleep
import re
import os
import json
from selenium import webdriver
# Python이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록합니다.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
# 이제 장고를 가져와 장고 프로젝트를 사용할 수 있도록 환경을 만듭니다.
import django
django.setup()

from portfolio.models import SnsData


def parse_insta():

        driver = webdriver.Chrome('C:/Users/ajy/chromedriver')

        url='https://www.instagram.com/explore/tags/%EB%89%B4%EB%8B%89/'
        driver.get(url)
        sleep(5)
        x=driver.find_element_by_css_selector('#react-root > section > main > article > div:nth-child(3) > div > div:nth-child(1) > div:nth-child(1) > a > div.eLAPa > div._9AhH0')
        x.click()

        pattern = '#([0-9a-zA-Z가-힣]*)'
        hash_w = re.compile(pattern)
        data={}


        page=0
        while page <10:
            sleep(3)
            text_hash=driver.find_element_by_css_selector('div.C4VMK > span').text.replace('\n','')
            author=driver.find_element_by_css_selector('div.C4VMK > h2').text

            hashtag=[]
            hash_tag = hash_w.findall(text_hash)
            for tag in hash_tag: 
                hashtag.append('#'+tag)

            text=re.sub(r"(?:@\S*|#\S*|http(?=.*://)\S*)",'', text_hash)
            
            page_data={}
            page_data['author']=author
            page_data['text']=text.strip()
            page_data['hashtag']=hashtag
            data['%d' % page] = page_data
            
            next_page=driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]')
            next_page.click()
            
            page+=1
        driver.close()
        return data



# 이 명령어는 이 파일이 import가 아닌 python에서 직접 실행할 경우에만 아래 코드가 동작하도록 합니다.
if __name__=='__main__':        
    insta_data_dict = parse_insta()
    for i,c in insta_data_dict.items():
        SnsData(author=c['author'], text=c['text'], hashtag=c['hashtag']).save()    







