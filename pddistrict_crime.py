import pandas as pd
import numpy as np

def get_pddistrict_crime(df_origin):
    df_origin = df_origin.fillna(0)
    data_2016 = df_origin.loc[df_origin['year'] == 2016].reset_index(drop=True)
    loc_group_1 = data_2016[['pddistrict']]
    loc_group_1['count'] = loc_group_1.groupby('pddistrict').pddistrict.transform('count')#.astype(int)
    loc_group_1 = loc_group_1.drop_duplicates(subset='pddistrict', keep="last").reset_index(drop=True)
    loc_group_1 = loc_group_1.set_index('pddistrict').sort_values('count', ascending = False)
    new_df = loc_group_1.reset_index()
    return new_df