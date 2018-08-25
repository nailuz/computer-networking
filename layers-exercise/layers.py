# -*- coding: utf-8 -*-

#The main class to this exercise. It show us how a basic layer works
class Layer(object):
    def __init__(self, name, top_layer=None, bot_layer=None):
        self.name = name
        self.top_layer = top_layer
        self.bot_layer = bot_layer
    
    def send(self, data):
        if self.bot_layer:
            print(str(self.name), 'i am sending to bottom...', data)
            self.bot_layer.send(data)
        else:
            print('BLOCKED. The layer', self.name, 'has not implement the bot layer')

    def receive(self, data):
        if self.top_layer:
            print(str(self.name), 'i am receiving to top...', data)
            self.top_layer.receive(data)
        else:
            print('BLOCKED. The layer', self.name, 'has not implement the top layer')





#Declaring the layers
layer_a1 =  Layer('top layer from A')
layer_a2 =  Layer('mid layer from A')
layer_a3 =  Layer('bot layer from A')

layer_b1 =  Layer('top layer from B')
layer_b2 =  Layer('mid layer from B')
layer_b3 =  Layer('bot layer from B')

#Conecting layers
layer_a1.bot_layer = layer_a2

layer_a2.top_layer = layer_a1
layer_a2.bot_layer = layer_a3

layer_a3.top_layer = layer_a2

layer_b1.bot_layer = layer_b2

layer_b2.top_layer = layer_b1
layer_b2.bot_layer = layer_b3

layer_b3.top_layer = layer_b2

#To post something
layer_a3.receive('test')
layer_a1.send('test')