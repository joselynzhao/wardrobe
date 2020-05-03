#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:main.py
@TIME:2020/4/26 19:49
@DES: 衣橱管理
'''
import os
import os.path as osp
import codecs
item_id = 0
# global item_id

class ITEM():
    def __init__(self,attr_list,attr_value):
        # global item_id
        # self.item_id = item_id
        # item_id+=1 #(在这里变化id)
        self.attr_list = attr_list
        self.attr_value = attr_value

    def get_attr_value(self):
        return self.attr_value

class GROUP():
    def __init__(self,group_name,group_attr):
        self.group_name = group_name
        self.attributes = group_attr
        self.item_list = []
        self.__load_data__() #回复item_list的数据
    def __update_len_item(self):
        self.num_item = len(self.item_list)
        return self.num_item

    def __storage_items__(self):
        file = codecs.open(osp.join('dataset', self.group_name,'group_data.txt'), 'w')
        for item in self.item_list:
            file.write('^'.join(item.attr_value))
            file.write('\n')
        print("the update of items is finished")

    def __load_data__(self):
        try:
            group_data_file = codecs.open(osp.join('database',self.group_name,'group_data.txt'),'r','utf-8')
            group_data =group_data_file.readlines()
            for line in group_data:
                attr_values = line.strip().split('^') #指定一个特殊的分割符号。
                if len(self.attributes) != len(attr_values):
                    print("the item and values of the attribute are not matched, creating item failed!")
                else:
                    self.item_list.append(ITEM(self.attributes,attr_values))
            self.__update_len_item()
        except:
            print("the database of {} is empty!".format(self.group_name))

    def add_item(self):
        print("please input the value one by one, if not value, enter ' '")
        attr_value = []
        for attr in self.attributes:
            value = input(attr)
            attr_value.append(value)
        self.item_list.append(ITEM(self.attributes,attr_value))
        self.__storage_items__()


class WARDROBE():
    def __init__(self):
        self.group_list = []
        self.__load_groups__()

    def __update_len_group__(self):
        self.num_group = len(self.group_list)
        return self.num_group

    def __storage_group_(self):
        file = codecs.open(osp.join('dataset','group_info.txt'),'w')
        for group in self.group_list:
            file.write(group.group_name+'^')
            file.write('^'.join(group.attributes))
            file.write('\n')
        print("the update of group is finished")

    def __load_groups__(self):
        try:
            group_file = codecs.open(osp.join('database','group_info.txt'),'r','utf-8')
            group_info = group_file.readlines() #第一项是 group_name ，后面是属性
            for line in group_info:
                data = line.strip().split('^')
                group_name = data[0]
                group_attr = data[1:]
                self.group_list.append(GROUP(group_name,group_attr))
            self.__update_len_group__()

        except:
            print("the database is empty!")
    def get_group_name_list(self):
        return [group.group_name for group in self.group_list]

    def __add_group__(self,group_name,group_attr):
        self.group_list.append(GROUP(group_name, group_attr))
        print('group {} is created successfully'.format(group_name))
        self.__update_len_group__()
        self.__storage_group_()

    def F_add_group(self,group_name,group_attr):
        if group_name in self.get_group_name_list():
            print('the group named {} is exsisted.'.format(group_name))
        else:
            self.__add_group__(group_name,group_attr)
            order = input('would you want add items for it? [y/n]')
            if order == 'y':
                self.F_add_item_for_group(group_name)


    def __add_item__(self,group_name):
        group = [group for group in self.group_list if group.group_name == group_name][0]
        group.add_item()



    def F_add_item_for_group(self,group_name):
        if group_name not in self.get_group_name_list():
            print('the group named {} is not exsisted'.format(group_name))
        while(True):
            self.__add_item__(group_name)
            order = input('would you want add item continue? [y/n]')
            if order == 'n':
                break

if __name__=='__main__':
    wardrobe = WARDROBE()
    # 主要考虑增加和查看功能










