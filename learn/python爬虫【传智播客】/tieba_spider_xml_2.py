import requests
from lxml import etree

# 来源网络

class Myspider():
    def __init__(self):
        self.post_bar = input('请输入贴吧名：')
        self.num = 1

    def postBar(self):
        '''
        获取贴吧帖子的url
        :return:
        '''
        base_url = 'https://tieba.baidu.com/'
        url = base_url + 'f?' + 'kw=' + self.post_bar
        response = requests.get(url)
        response.encoding = 'utf8'
        # 解析html 为 HTML 文档，
        #print(response.text)
        html = etree.HTML(response.text)
        # 抓取当前页面的所有帖子的url的后半部分，也就是帖子编号
        tieName = html.xpath('//div[@class ="threadlist_lz clearfix"]/div/a/@href')
        for tieUrl in tieName:
            url = base_url + tieUrl
            self.imgUrl(url)
    def imgUrl(self,url):
        response = requests.get(url)
        response.encoding = 'utf8'
        html = etree.HTML(response.text)
        tieName = html.xpath('//img[@class="BDE_Image"]/@src')

        for tieUrl in tieName:
            self.loadImg(tieUrl)

    def loadImg(self,url):
        print(url)
        print('正在下载第%s张' % self.num)
        with open('out/' + str(self.num) + '.png', 'wb') as file:

            # 2. 获取图片里的内容
            images = requests.get(url)

            # 3. 调用文件对象write() 方法，将page_html的内容写入到文件里
            file.write(images.content)

        self.num +=1

if __name__ =='__main__':
    imgSpdier = Myspider()
    imgSpdier.postBar()