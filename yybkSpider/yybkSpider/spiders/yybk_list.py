import scrapy


# from yybkSpider.yybkSpider.items import YybkspiderListItem
# from yybkSpider.items import YybkspiderListItem


class YybkListSpider(scrapy.Spider):
    name = 'yybk_list'
    allowed_domains = ['yunyubaike.com']
    start_urls = ['https://www.yunyubaike.com/yunqi/',
                  'https://www.yunyubaike.com/huaiyun_wiki/',
                  'https://www.yunyubaike.com/zaoyunfanying/',
                  'https://www.yunyubaike.com/yunqi_taijiao/',
                  'https://www.yunyubaike.com/yunqi_fayu/',
                  'https://www.yunyubaike.com/yunqi_jiancha/',
                  'https://www.yunyubaike.com/yunqi_yingyang/',
                  'https://www.yunyubaike.com/snsn/',
                  'https://www.yunyubaike.com/fenmian/',
                  'https://www.yunyubaike.com/fenmian_wiki/',
                  'https://www.yunyubaike.com/fenmian_daichan/',
                  'https://www.yunyubaike.com/fenmian_chancheng/',
                  'https://www.yunyubaike.com/fenmian_ketang/',
                  'https://www.yunyubaike.com/chanhou_buru/',
                  'https://www.yunyubaike.com/chanhou_wy_fs/',
                  'https://www.yunyubaike.com/yuezi_wiki/',
                  'https://www.yunyubaike.com/chanhou_huifu/',
                  'https://www.yunyubaike.com/01_jiezhong/',
                  'https://www.yunyubaike.com/01_jiaoliu/',
                  'https://www.yunyubaike.com/01_zaojiao/',
                  'https://www.yunyubaike.com/01_jibing/',
                  'https://www.yunyubaike.com/01_huli/',
                  'https://www.yunyubaike.com/01_wanju/',
                  'https://www.yunyubaike.com/01_yingyang/',
                  'https://www.yunyubaike.com/01_liaojie/',
                  'https://www.yunyubaike.com/01_wiki/',
                  'https://www.yunyubaike.com/yuer01/',
                  'https://www.yunyubaike.com/yuer13/',
                  'https://www.yunyubaike.com/13_wiki/',
                  'https://www.yunyubaike.com/13_liaojie/',
                  'https://www.yunyubaike.com/13_yingyang/',
                  'https://www.yunyubaike.com/13_wanju/',
                  'https://www.yunyubaike.com/13_richang/',
                  'https://www.yunyubaike.com/13_jibing/',
                  'https://www.yunyubaike.com/13_jiaoyu/',
                  'https://www.yunyubaike.com/13_nengli/',
                  'https://www.yunyubaike.com/13_tuoyou/',
                  'https://www.yunyubaike.com/yuer36/',
                  'https://www.yunyubaike.com/36_wiki/',
                  'https://www.yunyubaike.com/36_liaojie/',
                  'https://www.yunyubaike.com/36_yingyang/',
                  'https://www.yunyubaike.com/36_wanju/',
                  'https://www.yunyubaike.com/36_caiyi/',
                  'https://www.yunyubaike.com/36_jibing/',
                  'https://www.yunyubaike.com/36_jiating/',
                  'https://www.yunyubaike.com/36_ruxue/',
                  'https://www.yunyubaike.com/jiankang/',
                  'https://www.yunyubaike.com/my_wiki/',
                  'https://www.yunyubaike.com/my_yingerjibing/',
                  'https://www.yunyubaike.com/myjb_huxi/',
                  'https://www.yunyubaike.com/myjb_xiaohua/',
                  'https://www.yunyubaike.com/myjb_pifu/',
                  'https://www.yunyubaike.com/myjb_guke/',
                  'https://www.yunyubaike.com/myjb_yanke/',
                  'https://www.yunyubaike.com/myjb_kouqiang/',
                  'https://www.yunyubaike.com/muyingyongpin/',
                  'https://www.yunyubaike.com/qinzijiaoyu/',
                  'https://www.yunyubaike.com/qinzi_zhili/',
                  'https://www.yunyubaike.com/qinzi_jiajiao/',
                  'https://www.yunyubaike.com/qinzi_xingge/',
                  'https://www.yunyubaike.com/qinzi_xingwei/',
                  'https://www.yunyubaike.com/qinzi_youxi/',
                  'https://www.yunyubaike.com/qinzi_caiyi/',
                  'https://www.yunyubaike.com/qinzi_duxie/',
                  'https://www.yunyubaike.com/qinzi_youeryuan/',
                  'https://www.yunyubaike.com/buyunbuyu/',
                  'https://www.yunyubaike.com/beiyun_wiki/',
                  'https://www.yunyubaike.com/yunqianjiancha/',
                  'https://www.yunyubaike.com/yichuanyousheng/',
                  'https://www.yunyubaike.com/biyun_liuchan/',
                  'https://www.yunyubaike.com/biyun_yingyang/',
                  'https://www.yunyubaike.com/beiyun/']

    def parse(self, response):
        domain_url = "https://www.yunyubaike.com"
        # items = []
        this_url = response.url
        page_nums = response.xpath("//div[@class='pagebar']/b/text()")
        page_num = ''
        if page_nums:
            page_num = page_nums[0].get()
        # page_num = response.xpath("//div[@class='pagebar']/b/text()")[0].get()
        counts = response.xpath("//div[@class='pagebar']/a[@title]/b/text()")
        count=''
        if counts:
            count = counts[0].get()
        # count = response.xpath("//div[@class='pagebar']/a[@title]/b/text()")[0].get()
        for li in response.xpath("//div[@class='list']/ul/li"):
            titles = li.xpath('.//h2/a/text()')
            title = ''
            if titles:
                title = titles[0].get()
            detail_urls = li.xpath('.//h2/a/@href')
            detail_url = ''
            if detail_urls:
                detail_url = detail_urls[0].get()
            # detail_url = li.xpath('.//h2/a/@href')[0].get()
            yield {
                'this_url': this_url,
                'page_num': page_num,
                'count': count,
                'title': title,
                'detail_url': domain_url + detail_url
            }

            # item = YybkspiderListItem()
            # item['this_url'] = this_url
            # item['page_num'] = page_num
            # item['count'] = count
            # item['detail_url'] = detail_url
            # item['title'] = title

            # items.append(item)
        next_pages = response.xpath("//a[text()='下一页']/@href")
        if next_pages:
            next_page = next_pages[0].get()
            # next_page = response.xpath("//a[text()='下一页']/@href")[0].get()
            if next_page is not None:
                yield response.follow(domain_url + next_page, self.parse)

        # return items
