import streamlit as st

# Dữ liệu sản phẩm mẫu (bạn có thể thêm ảnh nếu muốn)
products = [
    {"name": "iPhone 15 Pro Max", "price": 35000000},
    {"name": "Samsung Galaxy S24 Ultra", "price": 28000000},
    {"name": "Xiaomi 14 Pro", "price": 19000000},
    {"name": "OPPO Find X6", "price": 17000000},
    {"name": "Realme GT5", "price": 13000000}
]

# Giao diện trang chính
st.set_page_config(page_title="Cửa hàng điện thoại", page_icon="📱")
st.title("📱 CỬA HÀNG BÁN ĐIỆN THOẠI")
st.markdown("### Vui lòng chọn sản phẩm cần mua:")

# Form đặt hàng
order = {}
total = 0

with st.form("order_form"):
    for i, p in enumerate(products):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"**{p['name']}** - {p['price']:,} VND")
        with col2:
            qty = st.number_input("Số lượng", min_value=0, max_value=10, step=1, key=f"qty_{i}")
        order[p['name']] = qty

    submitted = st.form_submit_button("🛒 Đặt hàng")

# Xử lý khi nhấn nút "Đặt hàng"
if submitted:
    st.markdown("## 🧾 Hóa đơn mua hàng")
    for p in products:
        qty = order[p["name"]]
        if qty > 0:
            line_total = qty * p["price"]
            st.write(f"{p['name']} x {qty} = {line_total:,} VND")
            total += line_total

    if total == 0:
        st.warning("Bạn chưa chọn sản phẩm nào.")
    else:
        st.markdown("---")
        st.success(f"💰 Tổng cộng: **{total:,} VND**")
        st.balloons()

