import streamlit as st

def main():
    st.set_page_config(page_title="Python Web 快速搭建模板", page_icon="🚀")
    st.title("🚀 Python Web 应用模板")
    st.markdown("""
    这是一个基于 Streamlit 的快速开发模板，你可以在此基础上进行功能扩展和自定义开发。
    
    **主要用途：**
    - 快速搭建 Python Web 界面
    - 实现数据展示、交互操作等基础功能
    """)
    st.success("欢迎使用本模板！请开始你的开发吧。")

if __name__ == "__main__":
    main()
