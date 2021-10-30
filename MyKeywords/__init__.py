
"""
继承自定义库中的类，rfw会解析类中的函数作为关键词
"""
from .MyKeywords import *

class MyLib(MyKeywords):
    ROBOT_LIBRARY_SCOPE = "GLOBAL"