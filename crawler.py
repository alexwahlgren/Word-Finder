import requests
import bs4
import urllib
import random

def initCrawl(url, step, steps):
    print('Crawling ...')
    crawler(url, step, steps)

def crawler(url, step, steps):
    if step < steps:
        try:
            print('** Site ', step, ' : ', url, ' **')
            res = requests.get(url)
            soup = bs4.BeautifulSoup(res.text, 'lxml')
            badLinks = []
            for link in soup.find_all('a'):
                badLinks.append(link.get('href'))
            print('CONTROL : badLinks=',len(badLinks))
            links = []
            for i in badLinks:
#               Om du vill se alla hemsidor, ta bort kommentar nedan
#                print(i)
                if i != None and "http" in i:
                    links.append(i)
            if not links:
                print('*** Results: ', step, ' websites were crawled. ***')
                return
            print('CONTROL : links=', len(links))
            nextUrl = links[random.randint(0,(len(links)))]
            step = step + 1
            crawler(nextUrl, step, steps)
        except IndexError as ie:
             print('Error : ', ie)
             print('*** Results: ', step, ' websites were crawled. ***')
        except Exception as e:
             print('Error : ', e)
             print('*** Results: ', step, ' websites were crawled. ***')

    else:
         print('*** Results: ', step, ' websites were crawled. ***')


initCrawl('https://whynohttps.com/', 1, 20)
