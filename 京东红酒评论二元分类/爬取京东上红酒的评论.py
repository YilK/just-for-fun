# 爬取京东上红酒的差评与好评
# 选取了评论数最多的红酒
import requests
import re
import json
import time


def get_json_comments(page, callbackId, productId, score):  # 获取原始数据
    """
    :param page: 页码
    :param callbackId: fetchJSON_comment98vv(xxxx)
    :param productId: 商品的ID
    :param score : score=1 差评，score=3 好评
    :return: json对象
    """

    url = 'https://sclub.jd.com/comment/productPageComments.action?' \
          'callback=fetchJSON_comment98vv{}&productId={}' \
          '&score={}&sortType=5&page={}&pageSize=10&isShadowSku=0&fold=1' \
        .format(callbackId, productId, score, page)  # url中的productId就是商品的id

    hd = {'User-Agent': 'Mozilla/5.0'}  # 伪装浏览器进行访问

    try:
        r = requests.get(url, headers=hd)
        r.raise_for_status()  # 如果状态不是200，抛出HTTPError异常
    except:
        print('出现异常·1')
    else:  # 如果没有异常发生
        r.encoding = r.apparent_encoding  # 设置编码

        # 将数据改为json格式的数据
        # 利用正则表达式将不需要的数据剔除
        print(r.text)
        result = re.sub(r'fetchJSON_comment98vv.*?\(', '', r.text)
        result = re.sub(r'\);', '', result)

        result = json.loads(result)  # 将字符串转换为JSON对象，由于最外层式大括号，所以最终类型是字典
        # print(result)
        # print(type(result))  # 类型
        return result


def pick_up_comments(json, content_list):  # 挑出所需的数据
    """

    :param json:
    :param content_list: 保存提取的评论
    :return:
    """
    items = json['comments']  # 找到评论所在的列表
    for item in items:
        content_list.append(item['content'])
    print(content_list)


def save_comments(content_list, index, id, count):  # 保存数据
    """
    保存文件
    :param content_list: 包含评论的列表
    :param index: 为文件标识(目的是区别文件的命名)
    :param id: id=1代表保存好评,id=0代表保存差评
    :param count: 为文件标识
    :return:
    """
    if id == 1:
        name = 'postive\\pos{}'
    elif id == 0:
        name = 'negative\\neg{}'

    # 打开文件，将数据写入，一个页面的评论保存为一个文件
    with open(name.format(index + ((count - 1) * 50)), 'w', encoding='utf-8') as f:
        for item in content_list:
            f.write(item + '\n')


def main(page, callbackid, productID, score, id, count):
    """

    :param page: 要爬取的页数
    :param callbackid: url中callback最后的数字
    :param productID: 商品的ID
    :param score : score=1 差评，score=3 好评
    :param id:  在保存文件时起标记作用
    :param count: 为不同的商品做标记，同时也为保存文件时实现文件名的不同
                  如count=1 代表爬取第一种商品的好评和差评
                    count=2 第二种商品
    :return: 无返回值
    """
    for i in range(page):
        content_list = []  # 保存评论的列表
        result = get_json_comments(i, callbackid, productID, score)  # 获得json对象
        pick_up_comments(result, content_list)  # 从json对象中提取出评论
        save_comments(content_list, i, id, count)
        time.sleep(2)


if __name__ == '__main__':
    """
    page : 爬取商品评论的页数
    callbackid :callback=fetchJSON_comment98vv123456 是最后面这一串数字
    productID :商品的id
    score :score=1 差评 ,score=3好评
    id :标记文件保存时的文件名
        id =1 保存好评  id=0 保存差评
    count : 为不同的商品做标记，同时也为保存文件时实现文件名的不同
            如下count=1 代表爬取第一种商品的好评和差评
                count=2 第二种商品
    """

    # 第一种商品
    main(page=50, callbackid=7324, productID=4905796, score=3, id=1, count=1)
    main(50, 7233, 4905796, 1, 0, 1)
    # 第二种商品
    main(page=50, callbackid=85603, productID=302813, score=3, id=1, count=2)
    main(page=50, callbackid=85603, productID=302813, score=1, id=0, count=2)
