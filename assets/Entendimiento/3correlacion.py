import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("datoslimpios.csv")
#print(df.info())
dfnum = df[['Survived', 'Pclass', 'Age','SibSp', 'Parch','Fare']]
co = dfnum.corr(method='pearson') # pearson, spearman, kendall

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(5, 5))
sns.heatmap(co,annot=True,cbar=False,annot_kws = {"size": 8},vmin=-1,vmax=1,center=0,
    cmap=sns.diverging_palette(20, 220, n=200), square=True,ax=ax)
ax.set_xticklabels(ax.get_xticklabels(),rotation = 45,horizontalalignment = 'right',)
ax.tick_params(labelsize = 10)