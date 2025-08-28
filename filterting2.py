import constants
import pandas as pd
import filter_information
from filter_information import get_information

def write_to_data_file(food_service_dict): #writes the information onto the csv file
    Data = str(food_service_dict)
    with open("data.cvs","a") as f:
        f.write(Data)

def filtering_kosher(food_service_dict, user_list):
    if user_list[1]: # if the user filters to kosher:



