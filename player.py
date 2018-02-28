# -*- coding:utf-8 -*-

class Player():
    def __init__(self):
        # D:筒子, T:条子 W:万子
        self.__cards = list()
        # 缺
        self.__waive = None
        # 胡牌
        self.__last = None
        # 出牌
        self.__show = list()
        self.__used = list()
        # 暗雨
        self.__rain_myself = list()
        # 直雨
        self.__rain_them = list()
        # 弯雨
        self.__rain_round = list()

    def use_card(self, card):
        self.__show.append(card)

    def rain_card(self, card, use_type):
        if
