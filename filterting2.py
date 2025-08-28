import constants
import pandas as pd
import filter_information
from filter_information import get_information
import maps

server_dict={}
def create_server_dict(address,name,kosher,consept,link):
    server_dict[address]=[name,kosher,consept,link]
    return server_dict

# def write_to_data_file(food_service_dict): #writes the information onto the csv file
#     Data = str(food_service_dict)
#     with open("data.cvs","a") as f:
#         f.write(Data)
filtered_dict={}
def filtering_kosher(server_dict, user_list):
    for i in server_dict.keys():
        j=server_dict[i]
        if j[1]==user_list[1] or (j[1]==False and user_list[1]==True) :
            filtered_dict[i]=server_dict[i]
    return filtered_dict

def filtering_consept(server_dict, user_list,filtered_dict):
    for i in server_dict.keys():
        j=server_dict[i]
        if j[2]==user_list[2] or j[2]=="both":
            if server_dict[i] not in filtered_dict.values():
                filtered_dict[i]=server_dict[i]
    return filtered_dict

address="התאנה 7,פתח תקווה"
name="דניאל מאפים"
kosher=True
consept="diary"
link="uuuuu"
user_list=["הזהבית",True,"diary"]
# filtered_dict=create_server_dict(address,name,kosher,consept,link)
# filtered_dict=filtering_kosher(server_dict, user_list)
# filtered_dict=filtering_consept(server_dict, user_list,filtered_dict)
# print(filtered_dict)

maps.create_map(user_list[0],filtered_dict)

