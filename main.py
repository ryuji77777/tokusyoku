import streamlit as st
from question import question
from answer import answer
from select_meal import select_meal

ss = st.session_state

#session_state の初期化 
#決定　未定0,情報あり選択前1,選択済み2
if "decision" not in ss:
    ss.decision = 0
#特食種類　未定はtbd
if "meal" not in ss:
    ss.meal = "tbd"
#質問ページ番号
if "qp" not in ss:
    ss.qp = 10
#リスクありなら心エコー
if "risk" not in ss:
    ss.risk = 0
#薬情報,血液検査値初期化
for key in ("d_DM", "d_HL", "d_HT", "d_HF","a1c", "ldl", "hdl", "tg_b", "bnp", "probnp", "cre"):
    if key not in ss:
        ss[key] = 0
#提案文
if "suggest" not in ss:
    ss.suggest = []
#特食選択の理由
if "reason" not in ss:
    ss.reason = [""]    
#心エコー所見
if "usf" not in ss:
    ss.usf = None


# 表示するもの
if ss.decision == 0:
    question(ss.qp)
elif ss.decision == 1:
    select_meal()
elif ss.decision == 2:
    answer()
    if st.button("最初に戻る", key="restart"):
        st.session_state.clear() 
        st.switch_page("main.py") 
