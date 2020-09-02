import streamlit as st
from execbox import execbox

s = {}

st.write(s)

execbox("""
import time
import streamlit as st

placeholder = st.empty()

for i in range(11):
    placeholder.text(i)
    time.sleep(.5)
""")

st.write(s)

execbox()
