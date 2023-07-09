### Code to input user excel file, process some required computations and download the file in excel format
##    **************  Author  : mhwahab ****************
##   ****************  Date Created: 07 July 2023 *************




import streamlit as st
import os
import pandas as pd
import numpy as np
import math
from io import BytesIO
import tempfile
import openpyxl

st.title("New Assay Computations Portal")
uploaded_file = st.file_uploader("Please upload excel file")

def compute_indv(df, df5, file_name):
    index = [0, 4, 8, 12, 16]
    df_indv = pd.DataFrame(columns=['filename', 'label', '%age', 'diff', 'SSF'])
    for i in index:
        avg_time_1 = (df.iloc[i]['Time1'] + df.iloc[i+1]['Time1'] + df.iloc[i+2]['Time1'] + df.iloc[i+3]['Time1'])/4
        avg_time_5 = (df.iloc[i]['Time5'] + df.iloc[i+1]['Time5'] + df.iloc[i+2]['Time5'] + df.iloc[i+3]['Time5'])/4
        blank_avg_1 = (df5.iloc[0]['Time1'] + df5.iloc[1]['Time1'] + df5.iloc[2]['Time1'] + df5.iloc[3]['Time1'])/4
        blank_avg_5 = (df5.iloc[0]['Time5'] + df5.iloc[1]['Time5'] + df5.iloc[2]['Time5'] + df5.iloc[3]['Time5'])/4
        norm_1 = avg_time_1 - blank_avg_1
        norm_5 = avg_time_5 - blank_avg_5
        diff = norm_1 - norm_5
        percen = norm_5/norm_1*100
        if i==0:
            wt_percen = percen
        ssf = -1*math.log10(percen/wt_percen)
        df_indv.loc[i/4] = [file_name, 'NA', percen, diff, ssf]
    return df_indv

if uploaded_file is not None:
   df = pd.read_excel(uploaded_file)
   df.drop(['Unnamed: 8'], axis = 1, inplace = True)
   df = df.iloc[40:]
   df.columns = ['index_alpha', 'Time1', 'Time2', 'Time3', 'Time4', 'Time5', 'Time6', 'Time7']
   file_name = uploaded_file.name
   df = df.iloc[0:96]
   df.reset_index(inplace = True)
   df.drop(['index'], axis = 1, inplace = True)
   df1 = df.iloc[0:20]
   df2 = df.iloc[24:44]
   df3 = df.iloc[48:68]
   df4 = df.iloc[72:92]
   df5 = df.iloc[92:96]
   
   df1.reset_index(inplace = True)
   df2.reset_index(inplace = True)
   df3.reset_index(inplace = True)
   df4.reset_index(inplace = True)
   df5.reset_index(inplace = True)

   df_test = compute_indv(df1, df5, file_name)
   df_test1 = compute_indv(df2, df5, file_name)
   df_test2 = compute_indv(df3, df5, file_name)
   df_test3 = compute_indv(df4, df5, file_name)

  

   wb = openpyxl.load_workbook(uploaded_file)

   sh = wb['Sheet2']

   sh['I41']='Percentage'
   sh['J41']='difference'
   sh['K41']='SSF'

   sh['I42']=df_test.iloc[0]['%age']
   sh['I46'] = df_test.iloc[1]['%age']
   sh['I50'] = df_test.iloc[2]['%age']
   sh['I54'] = df_test.iloc[3]['%age']
   sh['I58'] = df_test.iloc[4]['%age']

   sh['I66']= df_test1.iloc[0]['%age']
   sh['I70'] = df_test1.iloc[1]['%age']
   sh['I74'] = df_test1.iloc[2]['%age']
   sh['I78'] = df_test1.iloc[3]['%age']
   sh['I82'] = df_test1.iloc[4]['%age']

   sh['I90']= df_test2.iloc[0]['%age']
   sh['I94'] = df_test2.iloc[1]['%age']
   sh['I98'] = df_test2.iloc[2]['%age']
   sh['I102'] = df_test2.iloc[3]['%age']
   sh['I106'] = df_test2.iloc[4]['%age']

   sh['I114']= df_test3.iloc[0]['%age']
   sh['I118'] = df_test3.iloc[1]['%age']
   sh['I122'] = df_test3.iloc[2]['%age']
   sh['I126'] = df_test3.iloc[3]['%age']
   sh['I130'] = df_test3.iloc[4]['%age']

   sh['J42']=df_test.iloc[0]['diff']
   sh['J46'] = df_test.iloc[1]['diff']
   sh['J50'] = df_test.iloc[2]['diff']
   sh['J54'] = df_test.iloc[3]['diff']
   sh['J58'] = df_test.iloc[4]['diff']

   sh['J66']= df_test1.iloc[0]['diff']
   sh['J70'] = df_test1.iloc[1]['diff']
   sh['J74'] = df_test1.iloc[2]['diff']
   sh['J78'] = df_test1.iloc[3]['diff']
   sh['J82'] = df_test1.iloc[4]['diff']

   sh['J90']= df_test2.iloc[0]['diff']
   sh['J94'] = df_test2.iloc[1]['diff']
   sh['J98'] = df_test2.iloc[2]['diff']
   sh['J102'] = df_test2.iloc[3]['diff']
   sh['J106'] = df_test2.iloc[4]['diff']

   sh['J114']= df_test3.iloc[0]['diff']
   sh['J118'] = df_test3.iloc[1]['diff']
   sh['J122'] = df_test3.iloc[2]['diff']
   sh['J126'] = df_test3.iloc[3]['diff']
   sh['J130'] = df_test3.iloc[4]['diff']

   sh['K42']=df_test.iloc[0]['SSF']
   sh['K46'] = df_test.iloc[1]['SSF']
   sh['K50'] = df_test.iloc[2]['SSF']
   sh['K54'] = df_test.iloc[3]['SSF']
   sh['K58'] = df_test.iloc[4]['SSF']

   sh['K66']= df_test1.iloc[0]['SSF']
   sh['K70'] = df_test1.iloc[1]['SSF']
   sh['K74'] = df_test1.iloc[2]['SSF']
   sh['K78'] = df_test1.iloc[3]['SSF']
   sh['K82'] = df_test1.iloc[4]['SSF']

   sh['K90']= df_test2.iloc[0]['SSF']
   sh['K94'] = df_test2.iloc[1]['SSF']
   sh['K98'] = df_test2.iloc[2]['SSF']
   sh['K102'] = df_test2.iloc[3]['SSF']
   sh['K106'] = df_test2.iloc[4]['SSF']

   sh['K114']= df_test3.iloc[0]['SSF']
   sh['K118'] = df_test3.iloc[1]['SSF']
   sh['K122'] = df_test3.iloc[2]['SSF']
   sh['K126'] = df_test3.iloc[3]['SSF']
   sh['K130'] = df_test3.iloc[4]['SSF']
   #wb.close()

   #temp = tempfile.TemporaryFile()
   data = BytesIO()
   wb.save(data)
   data.seek(0)
   #wb.save(temp.name)
   wb.close()
   #data = BytesIO(temp.read())
   file_name_download = uploaded_file.name.replace(".xlsx", "_SSF.xlsx")
   st.download_button("Download the Processed File", data = data, mime='xlsx', file_name = file_name_download)
    
