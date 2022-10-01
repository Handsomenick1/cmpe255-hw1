import pandas as pd
import numpy as np

def get_category_crime(df_origin):
    df_origin = df_origin.fillna(0)
    data_2016 = df_origin.loc[df_origin['year'] == 2016].reset_index(drop=True)
    loc_group = data_2016[['category']]
    loc_group['count'] = loc_group.groupby('category').category.transform('count')#.astype(int)
    loc_group = loc_group.drop_duplicates(subset='category', keep="last").reset_index(drop=True)
    loc_group = loc_group.set_index('category').sort_values('count', ascending = False)

    category = loc_group.index.to_numpy()
    count = loc_group[['count']].to_numpy()

    # group all category other than the top 10 into one category and name it "others"
    head_loc = category[:12]
    head_loc = np.append(head_loc, 'OTHERS')    
    tail = count[12:].sum()
    head_count = count[0:12]
    head_count = np.append(head_count, tail)

    loc_group = loc_group.reset_index()
    return head_count, head_loc, loc_group