# Sistema de Recomendação Baseado em Regras
Atualmente está preparado para inferir a existência ou não de doença renal crônica em um paciente baseado na base Chronic Kidney Desease Data Set (https://archive.ics.uci.edu/ml/datasets/chronic_kidney_disease#).
O motor de inferência é baseado no método de Encadeamento para Trás.<br/><br/>
## Funcionamento
- <b>Alteração</b>: Para que seja adaptado a qualquer problema é necessário <b>criar as perguntas</b> que o sistema irá realizar no método "generateGoodQuestions". As <b>regras</b> devem estar no formato igual as que saem do Weka Apriori (visualizar regras.txt para entender o formato)<br/>
## Informações sobre os dados da base
1.Age(numerical)<br/>
age in years<br/>
2.Blood Pressure(numerical)<br/>
bp in mm/Hg  (Valores: 40~140)<br/>
3.Specific Gravity(nominal)<br/>
sg - (1.005,1.010,1.015,1.020,1.025)<br/>
4.Albumin(nominal)<br/>
al - (0,1,2,3,4,5)<br/>
5.Sugar(nominal)<br/>
su - (0,1,2,3,4,5)<br/>
6.Red Blood Cells(nominal)<br/>
rbc - (normal,abnormal)<br/>
7.Pus Cell (nominal)<br/>
pc - (normal,abnormal)<br/>
8.Pus Cell clumps(nominal)<br/>
pcc - (present,notpresent)<br/>
9.Bacteria(nominal)<br/>
ba - (present,notpresent)<br/>
10.Blood Glucose Random(numerical)<br/>
bgr in mgs/dl (Valores: 60~500)<br/>
11.Blood Urea(numerical)<br/>
bu in mgs/dl  (Valores: 10~170)<br/>
12.Serum Creatinine(numerical)<br/>
sc in mgs/dl (Valores: 0~30)<br/>
13.Sodium(numerical)<br/>
sod in mEq/L (Valores: 100~170)<br/>
14.Potassium(numerical)<br/>
pot in mEq/L (Valores: 2~10)<br/>
15.Hemoglobin(numerical)<br/>
hemo in gms (Valores: 7~18)<br/>
16.Packed Cell Volume(numerical) (Valores: 30~60)<br/>
17.White Blood Cell Count(numerical)<br/>
wc in cells/cumm (Valores: 4000~16000)<br/>
18.Red Blood Cell Count(numerical)<br/>
rc in millions/cmm (Valores: 4~7)<br/>
19.Hypertension(nominal)
htn - (yes,no)<br/>
20.Diabetes Mellitus(nominal)<br/>
dm - (yes,no)<br/>
21.Coronary Artery Disease(nominal)<br/>
cad - (yes,no)<br/>
22.Appetite(nominal)<br/>
appet - (good,poor)<br/>
23.Pedal Edema(nominal)<br/>
pe - (yes,no)<br/>
24.Anemia(nominal)<br/>
ane - (yes,no)<br/>
25.Class (nominal)<br/>
class - (ckd,notckd)<br/>

