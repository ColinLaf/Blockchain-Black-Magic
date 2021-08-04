import datetime


class Person:

    def __init__(self, ID):
        self.t_num = ID
        self.current_time = datetime.datetime(2021, 1, 1, 8, 0, 1, 1)
        self.current_node = 0

    def get_ID(self):
        return self.t_num

    def get_time(self):
        return self.current_time

    def get_node(self):
        return self.current_node

    def set_ID(self, ID):
        self.t_num = ID

    def set_time(self, t):
        self.current_time = t

    def set_node(self, loc):
        self.current_node = loc