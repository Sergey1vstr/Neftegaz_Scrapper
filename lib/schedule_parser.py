# -*- coding: utf-8 -*-

import re
import numpy
import pandas

def tr_schedule(keywords, parameters, input_file, output_file):
    """
    Transforms an .inc file to .csv file
    :param keywords:
    :param parameters:
    :param input_file:
    :param output_file:
    :return:
    """
    return

def clean_schedule(file_path):
    with open(file_path, "r", encoding = "UTF-8") as file:
        dirty_file = file.read()
        file_without_comments = re.sub("--.*\n", "\n", dirty_file)
        file_without_enters = re.sub("\n{2,}", "\n", file_without_comments)
        clear = re.sub("\t{1,}", "", file_without_enters)
        return clear

def parse_schedule():

def extract_kwblocks():

def extract_strings_from_blocks():

def parse_kwblock():

def parse_kw_DATES(handled_schedule):
    dates = re.findall("DATES\n.*/", handled_schedule)
    list_of_dates = []
    for date in dates:
        date_1 = re.sub("DATES\n", "", date)
        date_2 = re.sub(" /", "", date_1)
        list_of_dates += date_2
    return list_of_dates

def parse_kw_COMPDAT():

def parse_kw_COMPDATL():


