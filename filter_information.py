import pandas as pd
import constants
def get_information(food_service_dict):
    food_service_panda=pd.DataFrame(food_service_dict)
    # להכניס את זה בכל פעם לפייל ששומר גם את מה שהיה לפני זה
    return food_service_panda
food_service_panda = get_information(constants.food_service_dict)
print(food_service_panda)
.../