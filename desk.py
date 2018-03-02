# -*- coding:utf-8 -*-
import random
import Queue
from user import User
from player import Player


class Desk:
    def __init__(self, desk_id, name, user):
        self._queue = Queue.Queue()
        self._desk_id = desk_id
        self._desk_name = name
        self._player_id = list()
        self._player_obj = dict()
        self._guest = list()
        self._player_one = user._user_id
        self._player_two = None
        self._player_three = None
        self._player_four = None
        self._desk_owner = user._user_id
        self._next_one = None
        self._show_player = None
        self._desk_card = list()

        self._player_id.append(user._user_id)
        self._player_obj[user._user_id] = user

    def init_game(self):
        # 1-9 w 11-19 d 21-29 t
        cards = [x for x in range(1, 10)] * 4 + [x for x in range(11, 20)] * 4 + [x for x in range(21, 30)] * 4
        random.shuffle(cards)
        self._player_obj[self._player_one]._cards = random.sample(cards, 13)
        for x in self._player_obj[self._player_one]._cards:
            cards.remove(x)
        self._player_obj[self._player_two]._cards = random.sample(cards, 13)
        for x in self._player_obj[self._player_two]._cards:
            cards.remove(x)
        self._player_obj[self._player_three]._cards = random.sample(cards, 13)
        for x in self._player_obj[self._player_three]._cards:
            cards.remove(x)
        self._player_obj[self._player_four]._cards = random.sample(cards, 13)
        for x in self._player_obj[self._player_four]._cards:
            cards.remove(x)
        random.shuffle(cards)
        self._desk_card = cards
        for x in self._desk_card:
            self._queue.put(x)

    def pot_card(self):
        if not self._queue.empty():
            return self._queue.get()
        else:
            return None

    def hu_card(self, card):
        print "q"


    def join_desk(self, user, desk_num):
        self._player_id.append(user._user_id)
        if desk_num == 1:
            self._player_one = user._user_id
        elif desk_num == 2:
            self._player_two = user._user_id
        elif desk_num == 3:
            self._player_three = user._user_id
        elif desk_num == 4:
            self._player_four = user._user_id
        self._player_id.append(user._user_id)
        self._player_obj[user._user_id] = Player(user)

    def exit_desk(self, player_id, desk_num):
        if desk_num == 1:
            self._player_one = None
        elif desk_num == 2:
            self._player_two = None
        elif desk_num == 3:
            self._player_three = None
        elif desk_num == 4:
            self._player_four = None
        if player_id in self._player_id:
            self._player_id.remove(player_id)
        else:
            return -1
        del self._player_obj[player_id]

        if self._desk_owner == player_id:
            if desk_num == 4:
                for x in range(1, 4):
                    if self._player_one is not None:
                        self._desk_owner = self._player_one
                        break
                    elif self._player_two is not None:
                        self._desk_owner = self._player_two
                        break
                    elif self._player_three is not None:
                        self._desk_owner = self._player_three
                        break
            elif desk_num == 1:
                for x in range(1, 4):
                    if self._player_two is not None:
                        self._desk_owner = self._player_two
                        break
                    elif self._player_three is not None:
                        self._desk_owner = self._player_three
                        break
                    elif self._player_four is not None:
                        self._desk_owner = self._player_four
                        break
            elif desk_num == 2:
                for x in range(1, 4):
                    if self._player_three is not None:
                        self._desk_owner = self._player_three
                        break
                    elif self._player_four is not None:
                        self._desk_owner = self._player_four
                        break
                    elif self._player_one is not None:
                        self._desk_owner = self._player_one
                        break
            elif desk_num == 3:
                for x in range(1, 4):
                    if self._player_four is not None:
                        self._desk_owner = self._player_four
                        break
                    elif self._player_one is not None:
                        self._desk_owner = self._player_one
                        break
                    elif self._player_two is not None:
                        self._desk_owner = self._player_two
                        break

    def get_desk_player(self):
        return len(self._player_id)


if __name__ == "__main__":
    # name, nickname, user_id, username, user_key, money, icon):
    user1 = User("player1", u"昵称1", 1001, "username1", "sssss111", 100, "/picture1.jpg")
    print "user1:", user1._name, user1._nickname, user1._user_id, user1._username, user1._user_key, user1._money, user1._icon
    user2 = User("player2", u"昵称2", 1002, "username2", "sssss222", 100, "/picture2.jpg")
    print "user2:", user2._name, user2._user_id
    user3 = User("player3", u"昵称3", 1003, "username3", "sssss333", 100, "/picture3.jpg")
    print "user3:", user3._name, user3._user_id
    user4 = User("player4", u"昵称4", 1004, "username4", "sssss444", 100, "/picture4.jpg")
    print "user3:", user4._name, user4._user_id
    desk = Desk(101, "101号桌", user1)
    desk.join_desk(user2, 2)
    desk.join_desk(user3, 3)
    desk.join_desk(user4, 4)
    desk.init_game()
    for item in desk._player_obj.keys():
        print sorted(desk._player_obj[item]._cards)

