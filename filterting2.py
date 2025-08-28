import constants
import pandas as pd
import filter_information
from filter_information import get_information

def write_to_data_file(food_service_dict): #writes the information onto the csv file
    panda = pd.DataFrame(food_service_dict)
    Data = str(get_information(panda))
    with open("data.cvs","a") as f:
        f.write(Data)

