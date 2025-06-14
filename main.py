import streamlit as st

# Tạo tiêu đề cho ứng dụng
st.title("Login Form")

# Tạo form login
with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Login")

    # Kiểm tra thông tin đăng nhập (demo)
    if submitted:
        if username == "admin" and password == "123":
            st.success("Login successful ✅")
        else:
            st.error("Invalid username or password ❌")
