import blockchain
import datetime
import random
import person


class Log:

    def __init__(self, id1, id2, id3, id4):
        self.temp = []                      # store objects to be sorted
        self.chain = []                     # final blockchain
        self.p1 = person.Person(id1)        # 4 counselors
        self.p2 = person.Person(id2)        # ID is parameter for constructor
        self.p3 = person.Person(id3)
        self.p4 = person.Person(id4)
        self.b = blockchain.Blockchain()
        self.rtimes = []                    # holds chosen random times

    def create_log(self, l1, l2, l3, l4):

        self.get_entries_exits(self.p1, l1)   # calculates all times of person's entries and exits in path
        self.get_entries_exits(self.p2, l2)   # stores in temp[]
        self.get_entries_exits(self.p3, l3)
        self.get_entries_exits(self.p4, l4)

        self.temp.sort(key=lambda x: x.current_time)        # sorts list of entries and exits  chronologically

        for i in range(0, len(self.temp)):      # creates blockchain
            p = self.temp[i]
            self.b.add_transaction(p.get_ID(), p.get_node(), p.get_time())
            self.b.add_block()

        self.chain = self.b.get_chain()      # gets final blockchain

    # add time of person moving to new location
    def add_time(self, p, l, ele):
        td = datetime.timedelta(minutes=l[ele][1])
        t = p.get_time() + td
        p.set_time(t)
        p.set_node(l[ele][0])

    # randomly chooses time person spends in building then adds
    def in_building(self, p, l, ele):
        times = [58, 72, 84, 96, 122]         # random times a person can be in building

        while True:
            choice = random.choice(times)       # picks random time from list without replacement
            if len(self.rtimes) == 5:           # when all times have been chosen , start over again
                self.rtimes = []

            if choice not in self.rtimes:
                self.rtimes.append(choice)
                break

        td = datetime.timedelta(minutes= choice)    # adds random time to time person enters building to get exit time
        t = p.get_time() + td
        p.set_time(t)

    # gets all exit and entries person makes along path
    def get_entries_exits(self, p, l):

        new_p3 = person.Person("temp")          # create new object to store in temp[] to prevent overwriting
        self.p_equal(new_p3, p)                 # create before each append to list

        for i in range(0, len(l)):              # each loop is a new node on path
            new_p = person.Person("temp")
            self.p_equal(new_p, new_p3)

            self.add_time(new_p, l, i)
            self.temp.append(new_p)             # entry

            new_p2 = person.Person("temp")
            self.p_equal(new_p2, new_p)

            self.in_building(new_p2, l, i)
            self.temp.append(new_p2)             # exit

            self.p_equal(new_p3, new_p2)

    # makes to person objects attributes equal
    def p_equal(self, p1, p2):
        p1.set_ID(p2.get_ID())
        p1.set_time(p2.get_time())
        p1.set_node(p2.get_node())

    # returns blockchain log
    def get_log(self):
        return self.chain

    # get functions
    def get_time(self, index):
        return str(self.chain[index]['tx'][2].strftime('%H')) + ":" + str(self.chain[index]['tx'][2].strftime('%M'))

    def get_ID(self, index):
        return str(self.chain[index]['tx'][0])

    def get_location(self, index):
        return str(self.chain[index]['tx'][1])

    def get_hash(self, index):
        return str(self.chain[index]['hash'])

    def get_p_hash(self, index):
        return str(self.chain[index]['p_hash'])

    def get_nonce(self, index):
        return str(self.chain[index]['nonce'])