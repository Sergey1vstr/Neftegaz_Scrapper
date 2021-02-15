# -*- coding: utf-8 -*-

from lib import schedule_parser as scp

if __name__ == "__main__":
    keywords = ("DATES", "COMPDAT", "COMPDATL")
    parameters = ()
    input_inc = "input_data/test_schedule.inc"
    output_csv = "output_data/schedule.csv"

    schedule_dataframe = scp.tr_schedule(keywords, parameters, input_file = input_inc, output_file = output_csv)
    print("Пыщ пыщ ололо")
>>>>>>> Trial commit through dialogue window
