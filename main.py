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

# 開発用表示（※削除予定）
st.write("――――――――――――――――――――――――")
st.write("以下、開発用表示")
st.write(f"decision: {ss.get('decision', '未設定')}")
st.write(f"questionpage: {ss.get('qp', '未設定')}")
st.write(f"リスク: {ss.get('risk', '未設定')}")
st.write(f"合併症: {ss.get('PMH', '未設定')}")
st.write(f"meal: {ss.meal}")
st.write(f"suggest: {ss.get('suggest', '未設定')}")
st.write(f"reason: {ss.get('reason', '未設定')}")
st.write(
    f"年齢: {ss.get('age', '未設定')}"
    f" 性別: {ss.gender}"
    )
st.write(
    f"身長: {ss.get('height', '未設定')}"
    f" 体重: {ss.get('weight', '未設定')}"
    f" BMI: {ss.get('bmi', '未設定')}"
    )
st.write(
    f"糖尿病薬:{ss.get('d_DM', '未設定')}"
    f" 脂質異常薬: {ss.get('d_HL', '未設定')}"
    f" 降圧薬: {ss.get('d_HT', '未設定')}"
    f" 心疾患薬: {ss.get('d_HF', '未設定')}"
    )

st.write(
    f"HbA1c: {ss.get('a1c', '未設定')}"
    f" LDL: {ss.get('ldl', '未設定')}"
    f" HDL: {ss.get('hdl', '未設定')}"
    f" TG: {ss.get('tg_b', '未設定')}"
    f" BNP: {ss.get('bnp', '未設定')}"
    f" NT-proBNP: {ss.get('probnp', '未設定')}"
    f" Cre: {ss.get('cre', '未設定')}"
    )


