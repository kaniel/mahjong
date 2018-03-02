# -*- coding:utf-8 -*-

class Player:
    def __init__(self, user):
        self._user_id = user._user_id
        self._user = user
        # D:筒子, T:条子 W:万子
        self._cards = list()
        # 缺
        self._waive = None
        # 胡牌
        self._last = None
        self._last_type = list()
        # 出牌
        self._show = list()
        self._used = list()
        # 暗雨
        self._rain_myself = list()
        # 直雨
        self._rain_them = list()
        # 弯雨
        self._rain_round = list()
        self._hit_card = list()
        # 游客
        self._guest = list()

    def use_card(self, card):
        self._show.append(card)

    def rain_card(self, card, use_type):
        # 1: 暗雨 2:直雨 3:弯雨
        if use_type == 1:
            self._cards.remove(card)
            self._cards.remove(card)
            self._cards.remove(card)
            self._cards.remove(card)
            self._rain_myself.append(card)
        elif use_type == 2:
            self._cards.remove(card)
            self._cards.remove(card)
            self._cards.remove(card)
            self._rain_them.append(card)
        elif use_type == 3:
            print "111111111"
            self._cards.remove(card)
            self._rain_round.append(card)
        else:
            print "invalid use_type"

    def last_card(self, card):
        self._cards.append(card)
        self._last = card

    # 出牌
    def show_card(self, card):
        self._cards.remove(card)
        self._show.append(card)

    # 摸牌
    def fetch_card(self, card):
        self._cards.append(card)

    def hit_card(self, card):
        self._cards.remove(card)
        self._cards.remove(card)
        self._hit_card.append(card)

    def check_card(self):
        self._cards

    def add_guest(self, player_id):
        self._guest.append(player_id)

    def remove_guest(self, player_id):
        self._guest.remove(player_id)
