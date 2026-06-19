import requests
from bs4 import BeautifulSoup
import pandas as pd
import re



# def crawling_saramin(search_text:str,
#                      except_text:str = "",
#                      region:list = None,
#                      category:list = None,
#                      career:str = "",
#                      education:str = "",
#                      max_pages:int = 1):
#     columns = ['이름', '위치', '조건1', '조건2', '회사이름', '링크']
#     rows = []

#     url = "https://www.saramin.co.kr/zf_user/search"

#     headers = {
#         "User-Agent": (
#             "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
#             "AppleWebKit/537.36 (KHTML, like Gecko) "
#             "Chrome/126.0.0.0 Safari/537.36"
#         ),
#         "Accept-Language": "ko-KR,ko;q=0.9,en;q=0.8",
#     }

#     parameters = {'searchword':search_text,
#                 'except_read':except_text,
#                 'comp_page':max_pages}
#     if category:
#         parameters['cat_mcd'] = category

#     if region:
#         parameters['loc_mcd'] = region

#     if career:
#         parameters['career_cd'] = career
#     if education:
#         parameters['edu_cd'] = education

#     response = requests.get(url=url,
#                     headers=headers,
#                     params=parameters,
#                     timeout=15)

#     soup = BeautifulSoup(response.text, 'html.parser')

#     items = soup.select('div.item_recruit')
#     for item in items:
#         job_area = item.select_one('div.area_job') 
#         corp_area = item.select_one('div.area_corp')

#         if not job_area:
#             continue


#         job_title = job_area.select_one('.job_tit').get_text(strip=True)
#         condition_area = job_area.select_one('.job_condition')
#         spans = condition_area.select('span')

#         location = spans[0].get_text(strip=True)
#         condition1 = spans[1].get_text(strip=True)

#         job_sector = item.select_one('div.job_sector')
#         condition2 = job_sector.get_text(strip=True)

#         cor_name = corp_area.select_one('strong').get_text(strip=True)
#         link = job_area.select_one('.job_tit').select_one('.data_layer[href]')
#         real_link = 'https://www.saramin.co.kr/' + link.get('href')

        
#         rows.append({'이름':job_title,
#                     '위치':location,
#                     '조건1':condition1,
#                     '조건2':condition2,
#                     '회사이름':cor_name,
#                     '링크':link,})

#     df = pd.DataFrame(rows)
#     print(df)
    
    
#     return "사람인 결과"



def crawling_work24(search_text:str,
                     except_text:str = "",
                     region:list = None,
                     category:list = None,
                     career:str = "",
                     education:str = "",
                     max_pages:int = 1):
    url = 'https://www.work24.go.kr/wk/a/b/1200/retriveDtlEmpSrchList.do'     
    headers = {"User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64"
         " AppleWebKit/537.36 (KHTML, like Gecko)" 
         "Chrome/126.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "ko-KR,ko;q=0.9,en;q=0.8",
    }
   
    parameters = {'srcKeyword':search_text,
                  'notSrcKeyword':except_text,
                  'pageIndex':max_pages,
                  'resultCnt':10,
                  'CodeDepth1Info':region,
                  'occupation':"024",
                  'careerTypes':"",
                  'academiGbnoEdu':""}
    response = requests.get(url,
                            headers=headers,
                            params=parameters,
                            timeout=15)
    soup = BeautifulSoup(response.text, 'html.parser') 

    items = soup.select('div.box_table_group.gap_box08.column')
    itemss = soup.select('td.link pd24')
    import re
    for a, b in zip(items,itemss):
        
        cells = a.select('div.cell') 
        corp_name = cells[0].get_text(strip=True)
        name = cells[1].get_text(strip=True) 
        corp_area = b.select_one('li.site').get_text(strip=True)
        
        money = b.select_one('span.item.b1_sb').get_text(strip=True)
        money = re.sub(r'\s+', '', money)
        work_time = b.select_one('li.time')


        t = ''

        if work_time:
            if len(work_time) > 1:
                for i in range(len(work_time)):
                    t += work_time.select('span').text
            elif len(work_time) == 1:
                t = work_time.select('span').text

            else:
                t = ''
        else:
            t = ''

        
#         location = b.select_one('li.site').get_text(strip=True)        
#         condition1 = b.select_one('li.member').select('span.item.sm')[0].get_text(strip=True)
#         condition2 = b.select_one('li.member').select('span')[1].get_text(strip=True)
        

# if __name__ == '__main__':
    
#     crawling_work24('')
        
