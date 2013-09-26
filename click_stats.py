""" This file take a first glance at the expedia data (9000000):
    the counts for each variable_i is stored in an (2 x variable_i_range) array 
    denoted by the name of variable_i
    first row of the array counts click=1 counts, second row of array counts click=0 counts
    
    run by: data_stats = stats()
            data_stats.stats_count(file_name)
    check stats by: data_stats.$variable_i[0]
                    data_stats.$variable_i[1]
                    for click and non_click stats
"""

import pandas as pd
import numpy as np

class stats:   
    def __init__(self):
        # prop_starrating: range=[0, 1, 2, 3, 4, 5]
        self.prop_starrating = np.zeros((2,6))        
        # prop_review_score: range=[0.0, 0.5, 1.0, 1.5,… 5.0]
        self.prop_review_score = np.zeros((2,11))                
        # prop_brand_bool: range=[0, 1]
        self.prop_brand_bool = np.zeros((2,2))                
        # prop_location_score1:  range = [0, ~1, ~2, ~3, ~4, ~5, ~6, ~7]
        self.prop_location_score1 = np.zeros((2,8))                
        # prop_location_score2:  range = [0, ~0.1, ~0.2, ~0.3, ~0.4, ~0.5, >0.5]
        self.prop_location_score2 = np.zeros((2,7))                
        # prop_log_historical_price: range = [0, ~4.6, ~5, ~5.3, ~5.5, ~5.7, ~5.9, ~6, ~6.1, ~6.2, >6.2]
        self.prop_log_historical_price = np.zeros((2,11))               
        # price_usd: range = [0~49, 50~99, 100~149, 150~199, 200~249, 250~299, 300~399, 400~499, 500~]
        self.price_usd = np.zeros((2,9))                
        # promotion_flag: range=[0,1]
        self.promotion_flag = np.zeros((2,2))               
        # srch_length_of_stay: range = [1,2,3,4,5,5~7,>7]
        self.srch_length_of_stay = np.zeros((2,7))                
        # srch_booking_window: range = [1,3~5,5~7,7~10,11~15,>15]
        self.srch_booking_window = np.zeros((2,6))                
        # srch_adults_count: rang = [1,2,3,>=4]
        self.srch_adults_count = np.zeros((2,4))                
        # srch_children_count: range = [0, >=1]
        self.srch_children_count = np.zeros((2,2))                
        # srch_room_count: range = [1,2,>2]
        self.srch_room_count = np.zeros((2,3))                
        # srch_saturday_night_bool: range = [0,1]
        self.srch_saturday_night_bool = np.zeros((2,2))                
        # orig_destination_distance: range=[~100, ~300,~500, ~1000]
        self.orig_destination_distance = np.zeros((2,4))
        self.var = ['prop_starrating','prop_review_score','prop_brand_bool',\
        'prop_location_score1','prop_location_score2','prop_log_historical_price',\
        'price_usd','promotion_flag','srch_length_of_stay','srch_booking_window',\
        'srch_adults_count','srch_children_count','srch_room_count',\
        'srch_saturday_night_bool','orig_destination_distance']
        self.none_NA_count=dict()        
        for variable in self.var:
            self.none_NA_count[variable] = 0
    def stat_counts(self, v, var_range, count):
        for i in range(len(var_range)):
            if i==0 and v<=var_range[i]:
                count[i]+=1
            elif i!=0 and i!=len(var_range) and v<=var_range[i] and v> var_range[i-1]:
                count[i]+=1
            elif i == len(var_range)-1 and v >= var_range[i]:
                count[i]+=1
    def stats_count(self, file_name):    
        for i in range(10):
            train = pd.read_csv(file_name, nrows = 100000*(i+1), skiprows = range(1,100000*i+2))
            train = train.fillna(0, inplace=True)           
            # count none-NAN values
            for key in self.var:               
                self.none_NA_count[key] += train[key].shape[0]        
            print '# of samples scanned so far: ', 100000*(i+1)
            for j in range(100000):
                if train.click_bool[j]== 1:
                    self.stat_counts(train.prop_starrating[j], [i for i in range(6)], self.prop_starrating[0])              
                    self.stat_counts(train.prop_review_score[j], [i*0.5 for i in range(11)], self.prop_review_score[0])
                    self.stat_counts(train.prop_brand_bool[j], [0, 1], self.prop_brand_bool[0])                                        
                    self.stat_counts(train.prop_location_score1[j], [i for i in range(8)], self.prop_location_score1[0])                    
                    self.stat_counts(train.prop_location_score2[j], [i*0.1 for i in range(7)], self.prop_location_score2[0])                   
                    self.stat_counts(train.prop_log_historical_price[j], [0, 4.6, 5, 5.3, 5.5, 5.7, 5.9, 6, 6.1, 6.2, 6.2001], self.prop_log_historical_price[0])              
                    self.stat_counts(train.price_usd[j], [49.999, 99.999, 149.999, 199.999, 249.999, 299.999, 399.999, 499.999, 500], self.price_usd[0])
                    self.stat_counts(train.promotion_flag[j], [0, 1], self.promotion_flag[0])
                    self.stat_counts(train.srch_length_of_stay[j], [i for i in range(1,8)], self.srch_length_of_stay[0]) 
                    self.stat_counts(train.srch_booking_window[j],  [1,3,5,7,11,15], self.srch_booking_window[0])
                    self.stat_counts(train.srch_adults_count[j],  [1,2,3,4], self.srch_adults_count[0])
                    self.stat_counts(train.srch_children_count[j],  [0,1], self.srch_children_count[0] )
                    self.stat_counts(train.srch_room_count[j],  [1,2], self.srch_room_count[0] )
                    self.stat_counts(train.srch_saturday_night_bool[j],  [0, 1], self.srch_saturday_night_bool[0])                  
                    self.stat_counts(train.orig_destination_distance[j],  [100, 300,500, 1000], self.orig_destination_distance[0] )
                if train.click_bool[j] == 0 :
                    self.stat_counts(train.prop_starrating[j], [i for i in range(6)], self.prop_starrating[1])
                    self.stat_counts(train.prop_review_score[j], [i*0.5 for i in range(11)], self.prop_review_score[1])
                    self.stat_counts(train.prop_brand_bool[j], [0, 1], self.prop_brand_bool[1])
                    self.stat_counts(train.prop_location_score1[j], [i for i in range(8)], self.prop_location_score1[1])
                    self.stat_counts(train.prop_location_score2[j], [i*0.1 for i in range(7)], self.prop_location_score2[1])
                    self.stat_counts(train.prop_log_historical_price[j], [0, 4.6, 5, 5.3, 5.5, 5.7, 5.9, 6, 6.1, 6.2, 6.2001], self.prop_log_historical_price[1])
                    self.stat_counts(train.price_usd[j], [49.999, 99.999, 149.999, 199.999, 249.999, 299.999, 399.999, 499.999, 500], self.price_usd[1])
                    self.stat_counts(train.promotion_flag[j], [0, 1], self.promotion_flag[1])
                    self.stat_counts(train.srch_length_of_stay[j], [i for i in range(1,8)], self.srch_length_of_stay[1]) 
                    self.stat_counts(train.srch_booking_window[j],  [1,3,5,7,11,15], self.srch_booking_window[1])
                    self.stat_counts(train.srch_adults_count[j],  [1,2,3,4], self.srch_adults_count[1])
                    self.stat_counts(train.srch_children_count[j],  [0,1], self.srch_children_count[1] )
                    self.stat_counts(train.srch_room_count[j],  [1,2], self.srch_room_count[1] )            
                    self.stat_counts(train.srch_saturday_night_bool[j],  [0, 1], self.srch_saturday_night_bool[1])                                      
                    self.stat_counts(train.orig_destination_distance[j],  [100, 300,500, 1000], self.orig_destination_distance[1] )
                               
                      
