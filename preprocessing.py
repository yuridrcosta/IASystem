# -*- coding: utf-8 -*-

#OBS.: O preprocessamento foi feito convertendo a base de dados em .arff para .csv, utilizando o python no .csv e após isso retornando para o .arff
import pandas as pd

missing_values = ['?','NaN']
col_names = ['age','bp','sg','al','su','rbc','pc','pcc','ba','bgr','bu','sc','sod','pot','hemo','pcv','wbcc','rbcc','htn','dm','cad','appet','pe','ane','class']

base = pd.read_csv('chronic_kidney_disease.csv', encoding='ISO-8859-1',sep=',',names=col_names,na_values=missing_values)

base.loc[pd.isnull(base['age'])]
base['age'].value_counts()#60
base.loc[pd.isnull(base['bp'])]
base['bp'].value_counts()#80
base.loc[pd.isnull(base['sg'])]
base['sg'].value_counts()#1.020
base.loc[pd.isnull(base['al'])]
base['al'].value_counts()#0
base.loc[pd.isnull(base['su'])]
base['su'].value_counts()#0
base.loc[pd.isnull(base['rbc'])]
base['rbc'].value_counts()#normal
base.loc[pd.isnull(base['pc'])]
base['pc'].value_counts()#normal
base.loc[pd.isnull(base['pcc'])]
base['pcc'].value_counts()#notpresent
base.loc[pd.isnull(base['ba'])]
base['ba'].value_counts()#notpresent
base.loc[pd.isnull(base['bgr'])]
base['bgr'].value_counts()#99
base.loc[pd.isnull(base['bu'])]
base['bu'].value_counts()#46
base.loc[pd.isnull(base['sc'])]
base['sc'].value_counts()#1.2
base.loc[pd.isnull(base['sod'])]
base['sod'].value_counts()#135
base.loc[pd.isnull(base['pot'])]
base['pot'].value_counts()#3.5
base.loc[pd.isnull(base['hemo'])]
base['hemo'].value_counts()#15.0
base.loc[pd.isnull(base['pcv'])]
base['pcv'].value_counts()#52
base.loc[pd.isnull(base['wbcc'])]
base['wbcc'].value_counts()#9800
base.loc[pd.isnull(base['rbcc'])]
base['rbcc'].value_counts()#5.2
base.loc[pd.isnull(base['htn'])]
base['htn'].value_counts()#no
base.loc[pd.isnull(base['dm'])]
base['dm'].value_counts()#257
base.loc[pd.isnull(base['cad'])]
base['cad'].value_counts()#no
base.loc[pd.isnull(base['appet'])]
base['appet'].value_counts()#good
base.loc[pd.isnull(base['pe'])]
base['pe'].value_counts()#no
base.loc[pd.isnull(base['ane'])]
base['ane'].value_counts()#no
base.loc[pd.isnull(base['class'])]
base['class'].value_counts()


base = base.loc[base.dm != '\tyes']
base = base.loc[base.dm != '\tno']
base = base.loc[base.dm != ' yes']
base = base.loc[base.bu != '1.5']
base = base.loc[base.pcv != '\t?']
base = base.loc[base.pcv != '\t43']
base = base.loc[base.wbcc!= '\t8400']
base = base.loc[base.wbcc!= '\t6200']
base = base.loc[base.wbcc!= '\t?']
base = base.loc[base.cad!= '\tno']
base = base.loc[base.appet != 'no']

missing = {'age' : '60', 'bp':'80','sg':'1.020', 'al':'0','su':'0','rbc':'normal','pc':'normal',
           'pcc':'notpresent','ba':'notpresent','bgr':'99','bu':'46','sc':'1.2','sod':'135','pot':'3.5',
           'hemo':'15.0', 'pcv':'52','wbcc':'9800','rbcc':'5.2','htn':'no','dm':'257','cad':'no',
           'appet':'good','pe':'no','ane':'no'}

base = base.fillna(value = missing)

base = base.drop(0)


base.to_csv(r'C:\Users\Home\Desktop\Estudos\Chronic_Kidney_Disease\basededadosarrumada.csv')


#predictors = base.iloc[:,0:24].values
#classes = base.iloc[:, 24].values

#dfp = pd.DataFrame(predictors)
#dfc = pd.DataFrame(classes)

#from sklearn.preprocessing import LabelEncoder 

#labelencoder_predictors = LabelEncoder()

#for i in range(24):
 #   predictors[:,i] = labelencoder_predictors.fit_transform(predictors[:,i])

#classes[:] = labelencoder_predictors.fit_transform(classes[:])

#base.to_csv(r'C:\Users\Home\Desktop\Estudos\Chronic_Kidney_Disease\basededadosarrumada.csv')

#x = base.values #returns a numpy array
#min_max_scaler = preprocessing.MinMaxScaler()
#x_scaled = min_max_scaler.fit_transform(x)
#base = pd.DataFrame(x_scaled)
