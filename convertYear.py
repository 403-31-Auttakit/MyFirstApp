import streamlit as st
st.title("แอปพลิเคชั่นแปลงปี พ.ศ. เป็น ค.ศ.")

be_year = st.number_input("กรุณาใส่ปี พ.ศ.",value=2569)

ce_year = be_year - 543

st.header(f"ปี ค.ศ. คือ : {ce_year}")
