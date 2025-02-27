import streamlit as st

ss = st.session_state

def answer():
    if ss.meal == "none": #削除？※
        if ss.suggest ==[]:
            st.write("常食を継続")
        else: #★推奨の同一重複
            st.write("現時点で検討できる特別食なし")
            st.write(f"以下を推奨")
            for i in ss.suggest:
                st.write(f"・{i}")

    else:
        # 特食表示
        st.write(f"特別食として {ss.meal} を検討")
        st.write(f"{ss.reason}")

