import streamlit as st
from question import question
from answer import answer

ss = st.session_state

#特食種類　未定はtbd
if "meal" not in ss:
    ss.meal = "tbd"
#質問ページ番号
if "qp" not in ss:
    ss.qp = 10
#リスクありなら心エコー
if "risk" not in ss:
    ss.risk = 0
#提案文
if "suggest" not in ss:
    ss.suggest = []
#特食選択の理由
if "reason" not in ss:
    ss.reason = [""]    


# 表示するもの
if ss.meal == "tbd":
    # 特食未決定のときは質問
    question(ss.qp)

else:
    answer()

# 開発用表示（※削除予定）
st.write("――――――――――――――――――――――――")
st.write("以下、開発用表示")
st.write(f"年齢: {ss.age}")
st.write(f"性別: {ss.gender}")
st.write(f"ss.meal: {ss.meal}")
st.write(f"ss.suggest: {ss.get('suggest', '未設定')}")
st.write(f"ss.reason: {ss.get('suggest', '未設定')}")


