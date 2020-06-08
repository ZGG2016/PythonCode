from urllib import request,parse
from lxml import etree

def writeImage(link,headers):
    """
    将html内容写入到本地
    :param link:
    :param headers:
    :return:
    """
    req = request.Request(link, headers=headers)
    response = request.urlopen(req)
    image = response.read().decode()
    filename = link[-10:]
    # 写入到本地磁盘文件内
    path = "out//%s " % filename
    with open(path, "wb") as f:
        f.write(image)
    print("已经成功下载 " + path)

def loadLink(link,headers):
    """
    取出每个帖子里的每个图片连接
    :param link:
    :param headers:
    :return:
    """
    req = request.Request(link, headers=headers)
    response = request.urlopen(req)
    html = response.read().decode()

    content = etree.HTML(html)
    link_list = content.xpath('//img[@class="BDE_Image"]/@src')
    for link in link_list:
        writeImage(link,headers)

def loadPage(fullUrl):
    """
    根据url发送请求，获取服务器响应文件
    :param fullUrl:
    :return:
    """

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36 Edg/83.0.478.44",
    }
    req = request.Request(fullUrl, headers=headers)
    response = request.urlopen(req)
    html = response.read().decode()
    #print(html)
    content = etree.HTML(html)
    # link_list = content.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href')
    link_list = content.xpath('//div[@class="t_con cleafix"]/div//a/@href')

    #print(link_list)
    for link in link_list:
        fulllink = "http://tieba.baidu.com" + link
        #print(fulllink)
        loadLink(fulllink,headers)

def tiebaSpider(url, startPage, endPage):
    """
        作用：贴吧爬虫调度器，负责组合处理每个页面的url
        url : 贴吧url的前部分
        startPage : 起始页
        endPage : 结束页
    """
    for page in range(startPage, endPage + 1):
        # http://tieba.baidu.com/f?xxx&pn=0
        fullUrl = url + "&" + "pn=%s" % str((page - 1) * 50)
        loadPage(fullUrl)
        # print html

        print("谢谢使用")


if __name__ == "__main__":

    tiebaName = input("请输入贴吧名称：")
    startPage = int(input("请输入开始页码："))
    endPage = int(input("请输入结束页码："))
    name = {"kw": tiebaName}
    url = "http://tieba.baidu.com/f?" + parse.urlencode(name)

    tiebaSpider(url, startPage, endPage)

