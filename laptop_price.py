import pandas as pd
from sklearn.linear_model import LinearRegression
import streamlit as st
import math
st.header("Laptop Fiyat Tahmin Edicisi 3000")

data = pd.read_csv('laptop_price.csv',encoding='latin-1')

brandlist = list(data["Company"].unique())
gpulist = list(data["Gpu"].unique())
cpulist = list(data["Cpu"].unique())
ramlist = list(data["Ram"].unique())
memorylist = list(data["Memory"].unique())
screenlist = list(data["ScreenResolution"].unique())

brand=st.sidebar.selectbox("Brand: ", brandlist)
bos=[0]
b0=bos*len(brandlist)
sira=brandlist.index(brand)
b0[sira]=1
b0=b0[1:]


gpu=st.sidebar.selectbox("GPU: ", gpulist)
bos=[0]
g0= bos * len(gpulist)
sira=gpulist.index(gpu)
g0[sira]=1
g0= g0[1:]


cpu=st.sidebar.selectbox("CPU: ", cpulist)
bos=[0]
c0= bos * len(cpulist)
sira=cpulist.index(cpu)
c0[sira]=1
c0= c0[1:]


ram=st.sidebar.selectbox("RAM: ", ramlist)
bos=[0]
r0= bos * len(ramlist)
sira=ramlist.index(ram)
r0[sira]=1
r0= r0[1:]


memory=st.sidebar.selectbox("Memory: ", memorylist)
bos=[0]
m0= bos * len(memorylist)
sira=memorylist.index(memory)
m0[sira]=1
m0= m0[1:]


screen=st.sidebar.selectbox("ScreenResolution: ", screenlist)
bos=[0]
s0= bos * len(screenlist)
sira=screenlist.index(screen)
s0[sira]=1
s0= s0[1:]

pred=[]
pred=pred+b0 +g0+ c0+ r0+ m0+ s0

dm=pd.get_dummies(data, columns=["Company","Ram","Gpu","Cpu","Memory","ScreenResolution"],drop_first=True)
df=dm.drop(["laptop_ID","Product","TypeName","OpSys","Weight","Inches"],axis=1)
df["Price_euros"]=df["Price_euros"].astype(str)

y=df["Price_euros"]
x=df.drop(["Price_euros"],axis=1)

reg=LinearRegression()
model=reg.fit(x,y)
tahmin=model.predict([pred])

st.subheader("Tahmini Fiyat: ")
st.header(math.floor(tahmin))