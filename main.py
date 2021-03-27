from lib import schedule_lib as sl
import numpy as np


def giant_function(file_path):
    line_clean = clean_schedule(file_path)
    count = len(line_clean)

    # ------------------------------------------------------------------------------------------------------------------

    data_list = []
    data = ''
    final_result = []

    # вспомогательные параметры
    identificator_dat = 0
    identificator_compdat = 0
    identificator_compdatl = 0
    for i in range(count - 2):

        compdat_list = []
        compdatl_list = []
        result = []

        parametrs = line_clean[i].split(' ')

        # ---------------------------------------------------------------------------------------------------------------

        # нахождение дат

        # условия для нахождения дат
        if parametrs[0] == 'DATES': identificator_dat = 1
        if parametrs[0] == '/': identificator_dat = 0

        # список дат
        if identificator_dat == 1 and parametrs[0] != 'DATES':
            data = sl.parse_kw_DATES(line_clean[i])
            data_list.append(data)

        # ---------------------------------------------------------------------------------------------------------------

        # нахождение COMPDAT

        # условия для нахождения
        if parametrs[0] == 'COMPDAT': identificator_compdat = 1
        if parametrs[0] == '/': identificator_compdat = 0

        # список COMPDAT
        if identificator_compdat == 1 and parametrs[0] != 'COMPDAT':
            compdat_list = sl.parse_kw_COMPDAT(line_clean[i])

        # ---------------------------------------------------------------------------------------------------------------

        # нахождение COMPDATL

        # условия для нахождения дат
        if parametrs[0] == 'COMPDATL': identificator_compdatl = 1
        if parametrs[0] == '/': identificator_compdatl = 0

        # список COMPDATL
        if identificator_compdatl == 1 and parametrs[0] != 'COMPDATL':
            compdatl_list = sl.parse_kw_COMPDATL(line_clean[i])

        # ------------------------------------------------------------------------------------------------------------------

        # условие для присваивания значений параметров, непривязанных к датам
        if data_list == [] and compdat_list != []:
            result = [np.nan] + compdat_list

        if data_list == [] and compdatl_list != []:
            result = [np.nan] + compdatl_list

        # условие для присваивания значений параметров привязанных к датам
        if data_list != [] and compdat_list != []:
            result = [data] + compdat_list

        if data_list != [] and compdatl_list != []:
            result = [data] + compdatl_list

        # условие для присваивания на тот случай, если на определенную дату нет значений параметров
        if data_list != [] and (line_clean[i + 2] != 'COMPDAT' and line_clean[i + 2] != 'COMPDATL'):
            if bool(re.match(r"\d{2}\s+\w{3}\s+\d{4}", sl.parse_kw_DATES(line_clean[i]))) == True:
                result = [data] + [np.nan]

        # условие для дополнения списка найденной информацией
        if result != [] and (result in final_result) == False:
            final_result.append(result)

    for i in range(len(final_result)):
        print(final_result[i])