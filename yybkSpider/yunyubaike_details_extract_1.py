import os
from bs4 import BeautifulSoup

'''
yunyubaike_details_extract.py改进版：
  <br/>替换换行；
  制表符代替英文逗号进行分隔；
  原文中有制表符需要用两个空格代替；
  原文中不在替换英文引号和逗号。
'''

input_dir = '/mnt/sfs_turbo/guoyujian/tools/yybkSpider/html'
# input_dir = 'C:/Users/11599/Desktop/yybk_html_test'
output_file_base_name = '/mnt/sfs_turbo/guoyujian/tools/yybkSpider/ouput_20220113/yybk_{}.csv'
# output_file_base_name = 'C:/Users/11599/Desktop/yybk_test.csv'
MAX_ROWS = 50000    # 单个csv文件写入的最大行数


def parse(file_name):
    soup = BeautifulSoup(open(file_name, encoding='utf-8'))
    # title解析
    title = ''
    h1 = soup.find_all("h1")
    if h1:
        title = h1[0].get_text()
    # content解析
    p_list = soup.select("div.article_content > p")
    content = ''
    for p in p_list:
        p_text = p.get_text()
        if p_text != '':
            # 为了避免csv解析失败
            # p_text = p_text.replace(",", "，").replace('"', '')
            p_text.replace("\t", '  ')
            content += p_text + "\n"
    content = content.rstrip().lstrip()
    content = content.replace("\n", "<br/>")
    return title, content
    pass


def main():
    htmls = os.listdir(input_dir)
    # 最终生成的文件个数
    file_num = (len(htmls) + MAX_ROWS - 1) // MAX_ROWS
    for i in range(file_num):
        # i从0开始
        # 第i个文件保存 i*MAX_ROWS[下标] 到 (i+1)*MAX_ROWS - 1
        start_index = i*MAX_ROWS
        end_index = (i+1)*MAX_ROWS - 1
        if end_index > len(htmls):
            end_index = len(htmls)
        with open(output_file_base_name.format(i), "w", encoding='utf-8') as f:
            print("parsing :start_index:{}, end_index:{}; saving as {}"
                  .format(start_index, end_index, output_file_base_name.format(i)))
            f.write("article_id\tcontent\ttitle\n")
            for html_name in htmls[start_index: end_index]:
                title, content = parse(os.path.join(input_dir, html_name))
                f.write(html_name + '\t' + content + '\t' + title + '\n')
    pass


if __name__ == '__main__':
    main()
