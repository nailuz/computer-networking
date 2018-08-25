# -*- coding: utf-8 -*-

#The main class to this exercise. It show us how a basic layer works
class Layer(object):
    def __init__(self, name, top_layer=None, bot_layer=None):
        self.name = name
        self.top_layer = top_layer
        self.bot_layer = bot_layer
    
    def to_bot(self, data):
        if self.bot_layer:
            self.bot_layer.to_bot(data)
        else:
            print('BLOCKED. The layer', self.name, 'has not implement the bot layer')

    def to_top(self, data):
        if self.top_layer:
            print(str(self.name), 'I will to top layer...', data)
            self.top_layer.to_top(data)
        else:
            print('BLOCKED. The layer', self.name, 'has not implement the top layer')

class StringLayer(Layer):
    def to_bot(self, data):
        print(self.name, self.__class__.__name__, data)
        self.bot_layer.to_bot(data)

class ReverseLayer(Layer):
    def to_bot(self, data):
        print(self.name, self.__class__.__name__, data[::-1])
        self.bot_layer.to_bot(data[::-1])

    def to_top(self, data):
        print(self.name, self.__class__.__name__, data[::-1])
        self.top_layer.to_top(data[::-1])

class CharLayer(Layer):
    def __init__(self, *args, **kwargs):
        super(CharLayer, self).__init__(*args, **kwargs)
        self.buffer = []

    def to_bot(self,data):
        for i in data:
            print(self.name, self.__class__.__name__, i)
            self.bot_layer.to_top(i)
        self.bot_layer.to_top(None)

    def to_top(self, data):
        if data != None:
            self.buffer.append(data)
            print(self.name, self.__class__.__name__, ''.join(self.buffer))
        else:
            self.top_layer.to_top(''.join(self.buffer))



#Declaring the layers
layer_a1 =  StringLayer('Top A')
layer_a2 =  ReverseLayer('Mid A')
layer_a3 =  CharLayer('Bot A')

layer_b1 =  StringLayer('Top B')
layer_b2 =  ReverseLayer('Mid B')
layer_b3 =  CharLayer('Bot B')

#Conecting layers
layer_a1.bot_layer = layer_a2
layer_a2.top_layer = layer_a1
layer_a2.bot_layer = layer_a3
layer_a3.top_layer = layer_a2

layer_b1.bot_layer = layer_b2
layer_b2.top_layer = layer_b1
layer_b2.bot_layer = layer_b3
layer_b3.top_layer = layer_b2

layer_a3.bot_layer = layer_b3
layer_b3.bot_layer = layer_a3
 
#To trying something
layer_a1.to_bot('networks')
layer_b1.to_bot('infrastructure')