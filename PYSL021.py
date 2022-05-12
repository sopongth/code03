import streamlit as st

st.title("คำนวณผลรวม")
x = st.text_input("ป้อนตัวเลข x : ")
y = st.text_input("ป้อนตัวเลข y : ")

if st.button("คำนวณ"):
    try:
        z = float(x) + float(y)
        st.header("x + y = " + str(z))
    except:
        st.header("ไม่สามารถคำนวณได้")

    



