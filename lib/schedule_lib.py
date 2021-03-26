import re
import numpy as np

def clean_schedule(file_path):
    """принимает на вход путь к сырому  файлу schedule
       читает файл, редактирует прочитанный текст и записывает в файл handled_schedule.inc

       INPUT:
       file_path: путь к файлу в формате r'dir_name/file_name'
       OUTPUT: файл 'handled_schedue.inc', список строк без лишних символов"""
    with open(file_path, "r", encoding="UTF-8") as file_clean:
        file_clean = file_clean.read()
        file_clean = re.sub("--.*\n", "\n", file_clean)  # Нахождение комментариев и их замена на обычный перенос строки
        file_clean = re.sub("\n{2,}", "\n", file_clean)  # Удаление более одного переноса строки подряд
        file_clean = re.sub("\t", " ", file_clean)  # Удаление табуляции
        list_of_lines = file_clean.split("\n")
        new_list = list()
        for line in list_of_lines:
            line = re.sub(" +", " ", line)
            line = line.strip()
            new_list.append(line)
        new_list_to_string = "\n".join(new_list)
    with open("handled_schedule.inc", "wt") as handled_schedule:
        handled_schedule.write(new_list_to_string)
        print("Создан очищенный файл 'handled_schedule.inc'. Создан список строк из этого файла:")
    return new_list

#---------------------------------------------------------------------------------------------------------------


def parse_kw_DATES(line_from_hsc: str):
    """Принимает дату, вынутую из списка строк (генерируется при использовании clean_schedule())
       Возвращает дату без всяких там '/' """
    date = line_from_hsc.replace(" /","")
    return date

#---------------------------------------------------------------------------------------------------------------


def parse_kw_COMPDAT(line_from_hsc: str):
    """Превращает строку с параметрами перфорации в список"""
    line = re.sub("\d*\*", "DEFAULT", line_from_hsc)
    line = line.replace(" /","")
    params = line.split(' ')
    params.insert(1, np.nan)  # добавление пустого параметра (в COMPDATL этого не требуется)
    params.insert(-2, "DEFAULT")
    params.insert(-2, "DEFAULT")
    return params

#---------------------------------------------------------------------------------------------------------------


def parse_kw_COMPDATL(line_from_hsc: str):
    """Превращает строку с параметрами перфорации COMPDATL в список"""
    line = re.sub("\d*\*", "DEFAULT", line_from_hsc)
    line = line.replace(" /","")
    params = line.split(' ')
    params.insert(-2, "DEFAULT")
    params.insert(-2, "DEFAULT")
    return params