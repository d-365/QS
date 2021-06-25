# -*- coding: utf-8 -*-
# @Time    : 2021/6/23 11:44
# @Author  : dujun
# @File    : other1.py
# @describe:

class MusicPlayer(object):
    # 记录第一个被创建对象的引用
    instance = None
    # 记录是否执行过初始化动作
    init_flag = False

    def __new__(cls, *args, **kwargs):

        # 1. 判断类属性是否是空对象
        if cls.instance is None:
            # 2. 调用父类的方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)

        # 3. 返回类属性保存的对象引用
        return cls.instance

    def __init__(self):

        if MusicPlayer.init_flag is False:
            print("初始化音乐播放器")
            MusicPlayer.init_flag = True


if __name__ == '__main__':
    player = MusicPlayer()
    print(player)

    player2 = MusicPlayer()
    print(player2)
