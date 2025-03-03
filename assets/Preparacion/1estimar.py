import pandas as pd
from  math import isnan
import seaborn as sns

nombreArch = input("Nombre de archivo CSV: ")
datosOrigen = pd.read_csv(nombreArch+'.csv', encoding='UTF8')
#print("10 REGISTROS")
#datosOrigen.head()
#print("ya los desplegué")
#datosOrigen.info()
#datosOrigen.describe()
#sns.heatmap(datosOrigen.isnull(), cbar=False, cmap='viridis')


# SELECCION DE ALGUNOS ATRIBUTOS
#quitarCabin = datosOrigen[['PassengerId','Survived','Pclass','Name','Sex','Age','SibSp','Parch','Ticket','Fare','Embarked']]
#quitarCabin.info()
#print(ds_clean.Embarked.isnull().sum())

# ELIMINACIÓN DE ALGUNOS ATRIBUTOS
#quitaCabin2 = datosOrigen.drop(columns=['Cabin'])
#sns.heatmap(quitaCabin2.isnull(), cbar=False, cmap='viridis')
#quitaCabin2.info()

#SELECCION DE LA COLUMNA A LIMPIAR
#seleccion = datosOrigen[['Embarked']]
#limpia = seleccion.fillna('S')
#limpia.info()

mr = 0
mrs = 0
miss = 0
master = 0
otro = 0

listamr = []
listamiss = []
listamrs = []
listamaster = []
listaotro = []

for i in range(len(datosOrigen)):
  dato = datosOrigen.loc[i,"Name"]
  age = datosOrigen.loc[i,"Age"]
  if isnan(age): # SI EL DATO ES NULO 
#    print("BRINCO******************************")
    if 'Mr.' in dato:
      mr += 1
    elif 'Mrs.' in dato:
      mrs += 1
    elif 'Master.' in dato:
      master += 1
    elif 'Miss.' in dato:
      miss += 1
    else:
      otro += 1
    continue
  age = float(age)
  #print(dato,age)
  if 'Mr.' in dato:
    listamr.append(age)
  elif 'Mrs.' in dato:
    listamrs.append(age)
  elif 'Master.' in dato:
    listamaster.append(age)
  elif 'Miss.' in dato:
    listamiss.append(age)
  else:
    listaotro.append(age)
  #print(datosOrigen.loc[i,"PassengerId"], datosOrigen.loc[i,"Name"])

df = pd.DataFrame(listamr)
print("****\nMISTER:")
print('MEDIANA',df.median())
print('MODA',df.mode())
print('MEDIA',df.mean())
print('Cuenta',len(listamr))
print('faltan',mr)
print()
df = pd.DataFrame(listamrs)
print("****\nMISSTRESS:")
print('MEDIANA',df.median())
print('MODA',df.mode())
print('MEDIA',df.mean())
print('Cuenta',len(listamrs))
print('faltan',mrs)
print()
df = pd.DataFrame(listamaster)
print("****\nMASTER:")
print('MEDIANA',df.median())
print('MODA',df.mode())
print('MEDIA',df.mean())
print('Cuenta',len(listamaster))
print('faltan',master)
print()
df = pd.DataFrame(listamiss)
print("****\nMISS:")
print('MEDIANA',df.median())
print('MODA',df.mode())
print('MEDIA',df.mean())
print('Cuenta',len(listamiss))
print('faltan',miss)
print()
df = pd.DataFrame(listaotro)
print("****\nOTRO:")
print('MEDIANA',df.median())
print('MODA',df.mode())
print('MEDIA',df.mean())
print('Cuenta',len(listaotro))
print('faltan',otro)