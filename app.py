import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
col1,col2 = st.columns(2)
u = np.linspace(-10,10,100).tolist()
with col1:
    miu = st.select_slider(label="μ",options=np.round(u,2))
with col2:
    sig = st.select_slider("σ",options=np.round(np.linspace(0.1,10,100),2))
def lol(x,miu,sig):
    bruh = -((x-miu)**2/(2*sig))
    y = 1/((sig**.5)*((2*np.pi)**.5)) * np.exp(bruh)
    return y
x = np.linspace(-20,20,1000)
fig,ax = plt.subplots()
ax.set_title('Gauss Mass Function')
ax.set_xlabel('x')
ax.set_ylabel('p(x)')
ax.axhline(y=0,color='g')
ax.axvline(x=0, color='g')
ax.plot(x,lol(x,miu,sig))
st.pyplot(fig)