import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as ureq
import logging 
import os
from flask import Flask
import pymongo
class Scrap:
  def __init__(self):
   
   logging.basicConfig(filename="Scrapper.log",level=logging.INFO,format='%(asctime)s %(levelname)s: %(message)s' )
   #Directory To Store Downloaded Image
   Save_dir="images/"
   if not os.path.exists(Save_dir):
    os.makedirs(Save_dir)
   else:
    pass
  def Scraper(self,Query):
   Query=Query

  #Fake User Agent to Avoid Blocking
   headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64;x64) AppleWebkit/537.36(KHTML,like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
   url=query="Virat Kohli"
   url=f"https://www.google.com/search?sca_esv=571e9f62cdadf4fd&sxsrf=AE3TifMuF_9Lqfmmx8XoqAVUcUhjPgj6NQ:1753174080696&q={query}&udm=2&fbs=AIIjpHxU7SXXniUZfeShr2fp4giZ1Y6MJ25_tmWITc7uy4KIeqDdErwP5rACeJAty2zADJjYuUnSkczEhozYdaq1wZrEheAY38UjnRKVLYFDREDmzxDQH5cf73Nv5SUwLly1WG2RRTz5Zp2Uvco3Dr76giEv7KoLdER8DerohCvE5WYq8IvfNQRQHkwcsZAmUfFI3CBSx3HjRSebGup2eLjFz8thpHIe2Q&sa=X&ved=2ahUKEwiqyLyyitCOAxXfpa8BHdnAGj8QtKgLKAF6BAgYEAE&biw=1280&bih=585&dpr=1.5"
 #Fetch Result 
   response=requests.get(url,headers=headers) #Sent Request
   try:
    if response.ok:
     Soup=bs(response.content,'html.parser') #Parse Html Code 

     image_tags=Soup.findAll('img')

     del image_tags[0]

     img_data_mongo=[]   # To Store Data In Mongo Db
     Save_dir="images/"
     for i in image_tags:
        img_url=i['src']
        img_data=requests.get(img_url).content
        my_dict={'index':img_url,'image':img_data}
        img_data_mongo.append(my_dict)
        with open(os.path.join(Save_dir,f"{query}_{image_tags.index(i)}.jpg") ,"wb") as f :
            f.write(img_data)
    
       # client = pymongo.MongoClient("")
       # db = client['']
       # review_col = db[]
       # review_col.insert_many(img_data) 
     logging.info(f'Just Scrapped {Query} Images')      
     return 1
     
    else:
     logging.info('Response Not 200')
     logging.shutdown()
     return "Try Again"
   except Exception as e:
     logging.warning(str(e))
     logging.shutdown()
     return 'Something Went Wrong'
     

