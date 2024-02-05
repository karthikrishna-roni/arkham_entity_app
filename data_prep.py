import pandas as pd
import numpy as np
from datetime import datetime
from plot import line_cht_et,line_cht_la,hist_et,hist_la

def all_data_prep(entity,label,gh,range):
    df = pd.read_csv('data.csv')
    if gh == 'Line Graph':
        if entity=='None' and label == 'None':
            btc = df[['date', 'price']]
            df = df[['date', 'arkhamEntity', 'cumulative_sum']]
            df_g = df.groupby(['date', 'arkhamEntity'])['cumulative_sum'].sum().reset_index()

            df_n = pd.merge(df_g,btc, on='date', how='left')
            df_n.drop_duplicates(inplace=True)

            df_n['date'] = pd.to_datetime(df_n['date'])
            df_n['date'] = df_n['date'].dt.date
            df_n = df_n.rename(columns={'cumulative_sum': 'balance'})
            df_n = df_n.sort_values(by='date')

            if range!='None':
                if range =='0-44,000':
                    df_n = df_n[(df_n['balance'] >= 0) & (df_n['balance'] <= 44000)]
                if range == '44,000-88,000':
                    df_n = df_n[(df_n['balance'] > 44000) & (df_n['balance'] <= 88000)]
                if range == '88,000-1,32,000':
                    df_n = df_n[(df_n['balance'] > 88000) & (df_n['balance'] <= 132000)]
                if range == '1,32,000-1,76,000':
                    df_n = df_n[(df_n['balance'] > 132000) & (df_n['balance'] <= 176000)]
                if range == '1,76,000-2,20,000':
                    df_n = df_n[(df_n['balance'] > 176000) & (df_n['balance'] <= 220000)]
                if range =='>2,20,000':
                    df_n = df_n[(df_n['balance']>220000)]

            res = line_cht_et(df_n)
            return(res)
        
        if entity!='None' and label=='None':
            df  = df[df['arkhamEntity']==entity]
            btc = df[['date', 'price']]
            df = df[['date', 'arkhamEntity', 'cumulative_sum']]
            df_g = df.groupby(['date', 'arkhamEntity'])['cumulative_sum'].sum().reset_index()

            df_n = pd.merge(df_g,btc, on='date', how='left')
            df_n.drop_duplicates(inplace=True)

            df_n['date'] = pd.to_datetime(df_n['date'])
            df_n['date'] = df_n['date'].dt.date
            df_n = df_n.rename(columns={'cumulative_sum': 'balance'})
            df_n = df_n.sort_values(by='date')

            if range!='None':
                if range =='0-44,000':
                    df_n = df_n[(df_n['balance'] >= 0) & (df_n['balance'] <= 44000)]
                if range == '44,000-88,000':
                    df_n = df_n[(df_n['balance'] > 44000) & (df_n['balance'] <= 88000)]
                if range == '88,000-1,32,000':
                    df_n = df_n[(df_n['balance'] > 88000) & (df_n['balance'] <= 132000)]
                if range == '1,32,000-1,76,000':
                    df_n = df_n[(df_n['balance'] > 132000) & (df_n['balance'] <= 176000)]
                if range == '1,76,000-2,20,000':
                    df_n = df_n[(df_n['balance'] > 176000) & (df_n['balance'] <= 220000)]
                if range =='>2,20,000':
                    df_n = df_n[(df_n['balance']>220000)]

            res = line_cht_et(df_n)
            return(res)

        if entity!='None' and label!='None':
            df  = df[df['arkhamLabel']==label]
            btc = df[['date', 'price']]
            df = df[['date', 'arkhamLabel', 'cumulative_sum']]
            df_g = df.groupby(['date', 'arkhamLabel'])['cumulative_sum'].sum().reset_index()

            df_n = pd.merge(df_g,btc, on='date', how='left')
            df_n.drop_duplicates(inplace=True)

            df_n['date'] = pd.to_datetime(df_n['date'])
            df_n['date'] = df_n['date'].dt.date
            
            df_n = df_n.rename(columns={'cumulative_sum': 'balance'})
            df_n = df_n.sort_values(by='date')

            if range!='None':
                if range =='0-44,000':
                    df_n = df_n[(df_n['balance'] >= 0) & (df_n['balance'] <= 44000)]
                if range == '44,000-88,000':
                    df_n = df_n[(df_n['balance'] > 44000) & (df_n['balance'] <= 88000)]
                if range == '88,000-1,32,000':
                    df_n = df_n[(df_n['balance'] > 88000) & (df_n['balance'] <= 132000)]
                if range == '1,32,000-1,76,000':
                    df_n = df_n[(df_n['balance'] > 132000) & (df_n['balance'] <= 176000)]
                if range == '1,76,000-2,20,000':
                    df_n = df_n[(df_n['balance'] > 176000) & (df_n['balance'] <= 220000)]
                if range =='>2,20,000':
                    df_n = df_n[(df_n['balance']>220000)]

            res = line_cht_la(df_n)
            return(res)
    
    if gh=='Histogram':
        if entity=='None' and label == 'None':
            btc = df[['date', 'price']]
            df = df[['date', 'arkhamEntity', 'cumulative_sum']]
            df_g = df.groupby(['date', 'arkhamEntity'])['cumulative_sum'].sum().reset_index()

            df_n = pd.merge(df_g,btc, on='date', how='left')
            df_n.drop_duplicates(inplace=True)

            df_n['date'] = pd.to_datetime(df_n['date'])
            df_n['date'] = df_n['date'].dt.date
            df_n = df_n.rename(columns={'cumulative_sum': 'balance'})
            df_n = df_n.sort_values(by='date')

            if range!='None':
                if range =='0-44,000':
                    df_n = df_n[(df_n['balance'] >= 0) & (df_n['balance'] <= 44000)]
                if range == '44,000-88,000':
                    df_n = df_n[(df_n['balance'] > 44000) & (df_n['balance'] <= 88000)]
                if range == '88,000-1,32,000':
                    df_n = df_n[(df_n['balance'] > 88000) & (df_n['balance'] <= 132000)]
                if range == '1,32,000-1,76,000':
                    df_n = df_n[(df_n['balance'] > 132000) & (df_n['balance'] <= 176000)]
                if range == '1,76,000-2,20,000':
                    df_n = df_n[(df_n['balance'] > 176000) & (df_n['balance'] <= 220000)]
                if range =='>2,20,000':
                    df_n = df_n[(df_n['balance']>220000)]

            res = hist_et(df_n)
            return(res)
        
        if entity!='None' and label=='None':
            df  = df[df['arkhamEntity']==entity]
            btc = df[['date', 'price']]
            df = df[['date', 'arkhamEntity', 'cumulative_sum']]
            df_g = df.groupby(['date', 'arkhamEntity'])['cumulative_sum'].sum().reset_index()

            df_n = pd.merge(df_g,btc, on='date', how='left')
            df_n.drop_duplicates(inplace=True)

            df_n['date'] = pd.to_datetime(df_n['date'])
            df_n['date'] = df_n['date'].dt.date
            df_n = df_n.rename(columns={'cumulative_sum': 'balance'})
            df_n = df_n.sort_values(by='date')

            if range!='None':
                if range =='0-44,000':
                    df_n = df_n[(df_n['balance'] >= 0) & (df_n['balance'] <= 44000)]
                if range == '44,000-88,000':
                    df_n = df_n[(df_n['balance'] > 44000) & (df_n['balance'] <= 88000)]
                if range == '88,000-1,32,000':
                    df_n = df_n[(df_n['balance'] > 88000) & (df_n['balance'] <= 132000)]
                if range == '1,32,000-1,76,000':
                    df_n = df_n[(df_n['balance'] > 132000) & (df_n['balance'] <= 176000)]
                if range == '1,76,000-2,20,000':
                    df_n = df_n[(df_n['balance'] > 176000) & (df_n['balance'] <= 220000)]
                if range =='>2,20,000':
                    df_n = df_n[(df_n['balance']>220000)]


            res = hist_et(df_n)
            return(res)

        if entity!='None' and label!='None':
            df  = df[df['arkhamLabel']==label]
            btc = df[['date', 'price']]
            df = df[['date', 'arkhamLabel', 'cumulative_sum']]
            df_g = df.groupby(['date', 'arkhamLabel'])['cumulative_sum'].sum().reset_index()

            df_n = pd.merge(df_g,btc, on='date', how='left')
            df_n.drop_duplicates(inplace=True)

            df_n['date'] = pd.to_datetime(df_n['date'])
            df_n['date'] = df_n['date'].dt.date
            
            df_n = df_n.rename(columns={'cumulative_sum': 'balance'})
            df_n = df_n.sort_values(by='date')

            if range!='None':
                if range =='0-44,000':
                    df_n = df_n[(df_n['balance'] >= 0) & (df_n['balance'] <= 44000)]
                if range == '44,000-88,000':
                    df_n = df_n[(df_n['balance'] > 44000) & (df_n['balance'] <= 88000)]
                if range == '88,000-1,32,000':
                    df_n = df_n[(df_n['balance'] > 88000) & (df_n['balance'] <= 132000)]
                if range == '1,32,000-1,76,000':
                    df_n = df_n[(df_n['balance'] > 132000) & (df_n['balance'] <= 176000)]
                if range == '1,76,000-2,20,000':
                    df_n = df_n[(df_n['balance'] > 176000) & (df_n['balance'] <= 220000)]
                if range =='>2,20,000':
                    df_n = df_n[(df_n['balance']>220000)]

                    
            res = hist_la(df_n)
            return(res)

