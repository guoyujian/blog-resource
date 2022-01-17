import scrapy
import pandas as pd
import os


class YybkDetailDownSpider(scrapy.Spider):
    name = 'yybk_detail_down'
    allowed_domains = ['yunyubaike.com']
    df = pd.read_json("/mnt/sfs_turbo/guoyujian/tools/yybkSpider/urls.json")
    # 273179
    start_urls = df['detail_url'].drop_duplicates().tolist()

    def parse(self, response):
        url = response.url
        content = response.text

        file_name = url.replace("https://www.yunyubaike.com/", "")
        file_name = 'html/' + file_name.replace('/', '_')   # html/huaiyun_wiki_270163.html

        print("保存文件：" + file_name)
        with open(file_name, 'w') as f:
            f.write(content)
        pass

    '''
    该方法分类分文件夹保存html，不利于后续解析
    '''
    # def parse(self, response):
    #     url = response.url
    #     content = response.text
    #     # html/huaiyun_wiki/270163.html
    #     full_file_path = "html/" + url.replace("https://www.yunyubaike.com/", "")
    #     save_dir = full_file_path[0: full_file_path.rfind('/')]
    #     if not os.path.exists(save_dir):
    #         print("创建目录: " + save_dir)
    #         os.makedirs(save_dir)
    #     if os.path.exists(full_file_path):
    #         print(full_file_path + "文件已存在，跳过")
    #     else:
    #         print("保存文件：" + full_file_path)
    #         with open(full_file_path, 'w') as f:
    #             f.write(content)
    #     pass
