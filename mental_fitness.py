import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

df1 = pd.read_csv("prevalence-by-mental-and-substance-use-disorder.csv")
df2 = pd.read_csv("mental-and-substance-use-as-share-of-disease.csv")
data = pd.merge(df1,df2)
#data.drop('Code',axis=1,inplace=True)
data.set_axis(['Country','year','schizophrenia','Bipolar_disorder','Eating_fitness','Anxiety','drug_usage','depression','alcohol','mental_fitness'],axis='columns',inplace=True)
plt.figure(figsize = (12,6))
sns.heatmap(data.corr(),annot=True,cmap='Blues')
plt.plot()
sns.pairplot(data,corner=True)
plt.show()
mean = data['mentl_fitness'].mean()
fig=px.pic(data,values='mental_fitness',names='year')
fig.show()
fig=px.line(data,x="Year",y="mental_fitness",color='Country',markers = True,color_discrete_sequence =['red','blue'],template = 'plotly_dark')
fig.show()