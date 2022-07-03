#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
 * @author junzuowang
 * @description: 配置文件
 * @date 2022-07-03 17:20
'''


class DevelopmentConfig():
    pass

class ProductionConfig():
    pass



config  = {
    'developent':  DevelopmentConfig,
    'production': ProductionConfig
}