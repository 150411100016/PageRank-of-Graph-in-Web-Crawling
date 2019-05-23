import my_function as func
import requests
from bs4 import BeautifulSoup

def getLinks():
    
    url = "https://www.suara.com/news/2019/05/22/190121/kapolres-jakpus-minta-polisi-bertahan-pendemo-22-mei-terus-lempar-batu"
    listUrl.append(url)
    listUrl.append("depth")
    node.append(url)
    
    count_depth = 3
    depth = 1
    nav = 0
    
    cek = True
    while cek == True :
        if listUrl[nav] == "depth" :
            listUrl.append("depth")
            depth+=1
            nav+=1
        
        if depth > count_depth:
            cek = False
        
        else :
            url = listUrl[nav]
            req = requests.get(url)
            soup = BeautifulSoup(req.text, 'html.parser')
            news_links = soup.find_all('a',{'class':'ellipsis3'}, href=True)
            node_A = node.index(url)
            for link in news_links:
                listUrl.append(link['href'])
                if link['href'] not in node :
                    node.append(link['href'])
                node_B = node.index(link['href'])
                value = (str(node_A),str(node_B))
                edge.append(value)
            nav+=1
            
if __name__== "__main__":
    listUrl = []
    node = []
    edge = []
    
    links = getLinks()
    
    func.save_list("node",node)
    func.save_list("edge",edge)
    func.save_list("listUrl",listUrl)