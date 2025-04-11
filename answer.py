import streamlit as st

ss = st.session_state

def answer():
    if ss.meal == "none": 
        unique_suggestions = set(ss.suggest)
        st.write("常食を継続")
        if unique_suggestions == set():
            st.write("現時点の情報では、特別食の必要性なし")
        else:
            st.write("現時点の情報では、提案できる特別食なし")
            st.write("以下を推奨")
            for i in unique_suggestions:
                st.write(f"・{i}")        
    else:
        # 特食表示
        st.write(f"特別食として {ss.meal} を提案")
        st.write(f"{ss.reason}")

            

