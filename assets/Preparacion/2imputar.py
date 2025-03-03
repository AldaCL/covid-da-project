import pandas as pd
from  math import isnan

nombreArch = input("Nombre de archivo CSV: ")
#nombreArch = 'titanic'
datosOrigen = pd.read_csv(nombreArch+'.csv', encoding='UTF8')
salida = open("datoslimpios.csv",'w')
quitarCabin = datosOrigen[['PassengerId','Survived','Pclass','Name','Sex','Age','SibSp','Parch','Ticket','Fare','Embarked']]

variables = ['PassengerId','Survived','Pclass','Name','Lastname','Sex','Age','SibSp','Parch','Ticket','Fare','Embarked']
hayPrimera = False
for unaVar in variables:
    if hayPrimera == False:
        salida.write(unaVar)
        hayPrimera = True
    else:
        salida.write(","+unaVar)
salida.write("\n")
        
for i in range(len(datosOrigen)):
  pa = datosOrigen.loc[i,"PassengerId"]
  su = datosOrigen.loc[i,"Survived"]
  cl = datosOrigen.loc[i,"Pclass"]
  nam = datosOrigen.loc[i,"Name"]
  se = datosOrigen.loc[i,"Sex"]
  ag = datosOrigen.loc[i,"Age"]
  si = datosOrigen.loc[i,"SibSp"]
  pr = datosOrigen.loc[i,"Parch"]
  ti = datosOrigen.loc[i,"Ticket"]
  fa = datosOrigen.loc[i,"Fare"]
  em = datosOrigen.loc[i,"Embarked"]

  #print(pa,su,cl,nam,se,ag,si,pr,ti,fa,em)
  if pd.isnull(em):
    em = 'S'
  if pd.isnull(ag):
    if 'Mr.' in nam: 
      ag = 30
      #print("************************************************")
    elif 'Mrs.' in nam: 
      ag = 35
      #print("************************************************")
    elif 'Miss.' in nam: 
      ag = 21
      #print("************************************************")
    elif 'Master.' in nam: 
      ag = 3.5
      #print("************************************************")
    else: 
      ag = 42
      #print("************************************************")
  #print(pa,su,cl,nam,se,ag,si,pr,ti,fa,em)
  salida.write(''+str(pa)+','+str(su)+','+str(cl)+','+str(nam)+','+str(se)+','+str(ag)+','+str(si)+','+str(pr)+','+str(ti)+','+str(fa)+','+str(em)+'\n')
salida.close()  