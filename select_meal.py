import streamlit as st

ss = st.session_state

def select_meal():
    #データ０のとき推奨へ

    #心臓病食  
    if ss.usf == "あり":
        ss.meal = "心臓食"
        ss.reason =  "理由：血管リスクあり、エコー所見をともなう。治療状況を確認"

    #腎臓食
    elif ss.cre >2.0:#※基準確認
        ss.meal = "腎臓食"
        ss.reason =  "理由：血液検査で腎障害疑い。治療状況を確認すること"    

    #糖尿病食
    elif ss.d_DM == "あり":
        ss.meal = "糖尿病食"
        ss.reason =  "理由：糖尿病治療薬の処方あり。治療状況を確認すること"    
    elif ss.a1c  >5.9 : #※基準確認
        ss.meal = "糖尿病食"
        ss.reason =  "理由：血液検査で糖尿病疑い。治療状況を確認すること"

    #脂質異常食
    elif ss.hdl > 0 and ss.hdl < 40 :
        ss.meal = "脂質異常症食"
        ss.reason =  "理由：血液検査で脂質異常症疑い。治療状況を確認すること" 
    elif ss.ldl > 140 or  ss.tg_b > 150:
        ss.meal = "脂質異常症食"
        ss.reason =  "理由：血液検査で脂質異常症疑い。治療状況を確認すること"        
    elif ss.d_HL == "あり":
        ss.meal = "脂質異常症食"
        ss.reason =  "理由：脂質異常治療薬の処方あり。治療状況を確認すること"    
    elif ss.bmi > 35:
        ss.meal = "脂質異常症食"
        ss.reason =  "理由：高度肥満あり。検査・治療状況を確認すること"    
    
    #該当なし
    else:
        ss.meal = "none"
    
    ss.decision = 2
    st.rerun()  

