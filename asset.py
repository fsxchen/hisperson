from py2neo import Node

class People:
    def __init__(self, G, name, **kwargs):
        self.name = name
        self.parrent = None
        self.node = None
        n = G.nodes.match("People").where(name=self.name).first()
        if n == None:
            self.node = Node("People", name=self.name, **kwargs)
            G.create(self.node)
        self.node = n


    def __str__(self):
        return self.name

    def add_parrent(self, person):
        if self.parrent != None:
            raise "Error"
        self.parrent = person

    # def get_node(self, G):
    #     node = G.nodes.match("People").where(name=self.name).first()
    #     if node == None:
    #         node = Node("People", name=self.name, **kwargs)
    #     self.node = node
    #     return node

class Event:
    def __init__(self, name):
        self.name = name
        self.desc = ""
        self.parrent = None
        self.pre = None
        self.next = None
        self.participants = []
        self.node = None
    def add_participant(self, people):
        self.participants.append(people)
    def get_node(self, G):
        node = G.nodes.match("Event").where(name=self.name).first()
        if node == None:
            node = Node("Event", name=self.name)
        self.node = node
        return node
