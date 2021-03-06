import pandas as pd
from bs4 import BeautifulSoup
import urllib.request
import os
from pathlib import Path
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument('--disable-dev-shm-usage')

print("driver open")
driver = webdriver.Chrome(options=options)
print("driver open finish")

names = pd.read_csv('seoul names.csv', index_col=0) # 서울시 행정구역 정보 불러오기
base_url = "https://www.diningcode.com/2018/ajax/list.php"
total_cafe = []

   
# ---------카페 이름, 링크 크롤링 ----------------
# 각 카페의 이름을 가져옵니다.
# for index, data in names.iterrows():
#     page = 1 # 한 페이지에 10개씩 보여줍니다.
#     print(data.item(), 'get cafe data')
#     while(True):
#         url = base_url + '?' + 'query=서울' + data.item() + '카페' + '&' + 'page=' + str(page) # 주소 설정
#         driver.get(url) # 크롬으로 페이지 접속
#         # 로드까지 기다립니다.

#         html = driver.page_source # 페이지 소스 저장
#         soup = BeautifulSoup(html, 'html.parser') # 스프로 파싱
         
#         # 데이터에서 텍스트를 추출합니다
#         cafe_list = [d.text.split(' ', 1)[1] for d in soup.find_all("span", class_="btxt")]
#         cafe_link = [d.get("href") for d in soup.find_all("a", class_='blink')]
#         review_counts = [int(d.text) for d in soup.find_all("span", class_="review button")]
            
#         # 추출한 데이터를 묶어서 반복합니다.
#         for pair in zip(cafe_list, cafe_link, review_counts):
                
#             if pair[2] != 0: # 리뷰가 있는 카페만 크롤링합니다.
#                # 데이터 저장용 딕셔너리를 생성합니다
#                 cafe_dict = {
#                         'name': pair[0],
#                         'link': pair[1]
#                 }
                
                
#                     # 만든 딕셔너리가 배열에 없으면 추가합니다.
#                 if cafe_dict not in total_cafe:
#                     total_cafe.append(cafe_dict)
#         print('wait1')
#         time.sleep(5) # 한번에 너무 많은 요청을 보내면 서버가 죽어요
#         print('wait2')
        
#         if len(cafe_list) != 10: break # 목록이 10개 미만이면 최대 개수에 도달했다는 뜻입니다.   
#         page += 1
        
            
# print('total_cafe lenth : ', len(total_cafe))

# all_cafe = pd.DataFrame(total_cafe)
# all_cafe.to_csv('all_cafe.csv')
# 카페 상세정보 link는 uri가 포함되어있습니다.
base_url = "https://www.diningcode.com/"
src = ""

# 전체 리뷰를 불러옴
try: cafe_info = pd.read_csv('cafe_dictinfo.csv', index_col=0).to_dict('records')
except:
    cafe_info = []

try: user_review = pd.read_csv('user_data.csv', index_col=0).to_dict('records')
except:
    user_review = []
# 딕셔너리 방식으로 변경했기 때문에 주석처리합니다
# name_list = [] 
# main_tag_list = []
# score_list = []
# star_score = []
# like = []
# locate = []
# taste_score = []
# price_score = []
# service_score = []
# feat_text=[]
# purpose_list = []
#---------------------------------
# cafe_name = []
# user = []
# review = []

total_cafe = pd.read_csv('all_cafe.csv', index_col=0).to_dict('records')
# 위에서 생성된 total_cafe 배열을 사용해 접근합니다.
# 예외처리 위한 라이브러리
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException

for cafe in total_cafe[len(cafe_info):]:
    time.sleep(5)
    print(cafe,':crawling~~~')
    # url 생성 후 접근
    url = base_url + cafe['link']
    driver.get(url)

    # 첫 번째 사진 클릭 (사진 모드로 들어갑니다)
    # 사진이 뜰때까지 기다립니다.
    # wait = WebDriverWait(driver, 10)
    # element = wait.until(EC.element_to_be_clickable((By.ID, 'div_profile')))
    
    # try:
    #     driver.find_element_by_xpath("//*[@id='div_profile']/div[1]/ul/li[1]").click()
    # except:
    #     continue
        
    # driver.implicitly_wait(3) # 버튼이 등장할때까지 기다립니다.
    # # 음식/실내외 버튼 클릭
    # driver.find_element_by_xpath("//*[@id='full-area']/div[6]/span[2]").click()

    # # 3장을 가져와야 하므로 3번 반복합니다
    # for i in range(3):
    #     img = driver.find_element_by_id('display-img')

    #     if src == img.get_attribute('src') : break # 이미지가 3장 미만인경우, 버튼 클릭이 안 돼서 사진이 넘어가지 않습니다. 앞과 같은 사진이면 반복을 중지합니다.

    #     # 앞과 다른 사진이면 src 변수를 업데이트합니다.
    #     src = img.get_attribute('src')
    #     # 카페이름/image[번호].jpg 로 저장합니다.

    #     dirName = Path("images/" + cafe['name'])

    #     if not os.path.isdir(dirName):
    #         os.makedirs(dirName)
    #     urllib.request.urlretrieve(src, os.path.join(dirName, str(i+1) + ".jpg"))

    #     # 다음 버튼을 클릭합니다.
    #     try:
    #         driver.find_element_by_class_name('btn-gallery-next').click()
    #         driver.implicitly_wait(1)
    #     except:
    #         continue

    # # url 생성 후 접근
    # driver.get(url)
    driver.implicitly_wait(5)
    #방문목적 더보기 클릭   

    one_info = {}
    try:
        btn_more = driver.find_element_by_xpath('//*[@id="div_profile"]/div[8]/div[1]/ul[1]/li[1]/span')
        btn_more.click()
        # time.sleep(1)
    except:
        continue

    try:
        # 카페명
        one_info["name_list"] = (driver.find_element_by_xpath("//*[@id='div_profile']/div[1]/div[2]/p").text)
    except NoSuchElementException:
        one_info["name_list"] = ('-')
    try:
        #메인태그
        one_info["main_tag_list"] = (driver.find_element_by_xpath("//*[@id='div_profile']/div[2]/ul/li[3]/span").text)    
    except NoSuchElementException:
        one_info["main_tag_list"] = ('-')
    try:
        # 스코어
        one_info["score_list"] = (driver.find_element_by_xpath("//*[@id='div_profile']/div[1]/div[4]/p/strong").text)
    except NoSuchElementException:
        one_info["score_list"] = ('-')
    try:
        # 별점 5점 만점
        one_info["star_score"] = (driver.find_element_by_xpath("//*[@id='lbl_review_point']").text)
    except NoSuchElementException:
        one_info["star_score"] = ('-')
        
    try:
        # 좋아요수
        one_info["like"] = (driver.find_element_by_xpath("//*[@id='div_profile']/div[1]/div[5]/a[1]/span/i").text)
    except NoSuchElementException:
        one_info["like"] = ('-')
    try:
        # 주소
        one_info["locate"] = (driver.find_element_by_xpath("//*[@id='div_profile']/div[2]/ul/li[1]").text)
    except NoSuchElementException:
        one_info["locate"] = 
    try:
        # 맛 스코어
        one_info["taste_score"] = (driver.find_element_by_xpath("//*[@id='div_profile']/div[8]/div[1]/p[2]/span[1]/i").text)
    except NoSuchElementException:
        one_info["taste_score"] = ('-')
    try:
        # 가격 스코어
        one_info["price_score"] = (driver.find_element_by_xpath("//*[@id='div_profile']/div[8]/div[1]/p[2]/span[2]/i").text)
    except NoSuchElementException:
        one_info["price_score"] = ('-')
    try:
        # 서비스 스코어
        one_info["service_score"] = (driver.find_element_by_xpath("//*[@id='div_profile']/div[8]/div[1]/p[2]/span[3]/i").text)
    except NoSuchElementException:
        one_info["service_score"] = ('-')
    try:
        # 특징
        one_info["feat_text"] = (driver.find_element_by_xpath("//*[@id='div_profile']/div[2]/ul/li[4]").text)
    except NoSuchElementException:
        one_info["feat_text"] = ('-')
    try:
        # 방문목적
        one_info["purpose_list"] = (driver.find_element_by_xpath("//*[@id='div_profile']/div[8]/div[1]/ul[1]/li[1]").text)
    except NoSuchElementException:
        one_info["purpose_list"] = ('-')    

    cafe_info.append(ont_info)
    
    #유저 리뷰 크롤링
    #리뷰 더보기 버튼 누르기
    while True:   
        try:
            btn_more = driver.find_element_by_xpath('//*[@id="div_more_review"]')
            btn_more.click()
            # time.sleep(1)
        except:
            break
            
    #리뷰 개수만큼 크롤링하기 위해서 리뷰 개수에 대한 정보가 필요하다
    rev = driver.find_element_by_xpath('//*[@id="div_profile"]/div[8]/p').text
    for i in range(int(rev.split('건')[0])):
        one_review = {}
        #카페명
        one_review["cafe_name"] = (cafe['name'])
        #유저ID 및 영향력
        try:
            one_review["user"] = (driver.find_elements_by_xpath("//p[@class='person-grade']")[i].text)
        except:
            one_review['user'] = '-'
            
        #리뷰
        try:
            one_review["review"] = (driver.find_elements_by_css_selector('p.review_contents.btxt')[i].text)
        except:
            one_review["review"] = ('-')

        user_review.append(one_review)

    
    pd.DataFrame(cafe_info).to_csv('cafe_dictinfo.csv', index=False)
    pd.DataFrame(user_review).to_csv('user_data.csv', index = False)        
    
    time.sleep(1)
    print('done')

    


# crawling_cafe = pd.DataFrame([name_list,main_tag_list,score_list,star_score,like,locate,taste_score,price_score,service_score,feat_text,purpose_list]).T
# crawling_cafe.columns = ['name','main_tag','score','star_score','like','locate','taste_score','price_score','service_score','feat_text','purpose_list']
# crawling_cafe.to_csv('cafe_dictinfo')

# user_data = pd.DataFrame([cafe_name,user,review]).T
# user_data.columns=['cafe_name','user','review']
# user_data.to_csv('user_data')

print("crwaling done")