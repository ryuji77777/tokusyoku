import streamlit as st

ss = st.session_state

def question(qp):
    if qp == 10:
        # 年齢性別 
        age = st.text_input("年齢は? :不明は0", value="70", key="age_input")
        gender = st.radio("性別は?", ("男性", "女性", "不明"), index=2, horizontal=True, key="gender_radio")
        ss.gender = gender
        
        if st.button("次へ", key="next_10"):
            try:
                ss.age = float(age)
                ss.qp = 15
                st.rerun()
            except ValueError:
                st.warning("数値を入力してください")
    
    elif qp == 15:
        # 身長体重 
        height = st.text_input("身長は? :不明は0", value="150", key="height_input")
        weight = st.text_input("体重は? :不明は0", value="50", key="weight_input")

        if st.button("次へ"):
            try:
                ss.height = float(height)
                ss.weight = float(weight)
                ss.bmi = ss.weight / (ss.height ** 2) * 10000 if ss.height != 0 else 0
                ss.qp = 20
                st.rerun()
            except ValueError:
                st.warning("数値を入力してください")

    elif ss.qp == 20:
        # 合併症　※病名追加,貧血はその後の分岐必要
        st.markdown("##### 合併している病名は？")

        cols = st.columns(7)

        with cols[0]: PMH_hf = st.checkbox("心疾患", key="PMH_hf") #心疾患算定基準確認※
        with cols[1]: PMH_dm = st.checkbox("糖尿病", key="PMH_dm")
        with cols[2]: PMH_hl = st.checkbox("脂質異常症", key="PMH_hl")
        with cols[3]: PMH_ht = st.checkbox("高血圧症", key="PMH_ht")
        with cols[4]: PMH_kd = st.checkbox("腎疾患", key="PMH_kd")
        with cols[5]: PMH_none = st.checkbox("該当なし", key="PMH_none")
        with cols[6]: PMH_cannot = st.checkbox("判断できない", key="PMH_cannot")

        # 選択された病名をリスト化
        selected_PMHs = []
        if PMH_hf: selected_PMHs.append("心疾患")
        if PMH_dm: selected_PMHs.append("糖尿病")
        if PMH_hl: selected_PMHs.append("脂質異常症")
        if PMH_ht: selected_PMHs.append("高血圧症")
        if PMH_kd: selected_PMHs.append("腎疾患")
        if PMH_none: selected_PMHs.append("該当なし")
        ss.PMH = selected_PMHs  

        if st.button("次へ", key="next_20"):
            
            meal_list = [
            ("心疾患", "心臓食"),
            ("糖尿病", "糖尿病食"),
            ("脂質異常症", "脂質異常症食"),
            ("腎疾患", "腎臓食"),
            ]   

            for disease, meal in meal_list:
            
                if disease in ss.PMH:
                    ss.meal = meal
                    ss.reason = f"理由：{disease}の病名あり。治療状況を確認すること"
                    ss.decision = 2
                    break  # 最優先の疾患を設定したらループを抜ける

                elif "該当なし" in ss.PMH:
                    ss.qp = 30
                    break
                elif "高血圧症" in ss.PMH:
                    ss.risk += 1
                    ss.qp = 30
                    break
                else :        
                    ss.qp = 30
                    ss.suggest.append("身体疾患の病歴を確認")

            st.rerun() 


    elif qp == 30:
        #d_は処方薬
        st.markdown("##### 処方薬の情報がある？")
        d_yn = st.radio("選択", ("あり", "なし"), index=1, horizontal=True, key="d_yn_radio", label_visibility="collapsed")
        ss.d_yn = d_yn  

        if st.button("次へ"):  
            if ss.d_yn  == "あり":
                ss.qp = 35
            elif ss.d_yn  == "なし":
                ss.qp = 50 
                ss.suggest .append("処方薬の情報を取得")
            st.rerun()

    #※薬品名追加
    elif qp == 35:
        st.markdown("#### 処方内容に下記がある？")
        st.markdown("""
            <span 
                title="例: メトホルミン, メトグルコ, ジャヌビア, エクア, 各種インスリン" 
                style="text-decoration:underline;">
                糖尿病の治療薬
            </span>
        """, unsafe_allow_html=True)
        d_DM = st.radio("選択", ("あり", "なし", "判断できない"), index=2, horizontal=True, key="d_DM_radio", label_visibility="collapsed")
        ss.d_DM = d_DM  

        st.markdown("""
            <span 
                title="例: プラバスタチン, ベサフィブラート" 
                style="text-decoration:underline;">
                脂質異常症の治療薬
            </span>
        """, unsafe_allow_html=True)
        d_HL = st.radio("選択", ("あり", "なし", "判断できない"), index=2, horizontal=True, key="d_HL_radio", label_visibility="collapsed")
        ss.d_HL = d_HL  

        st.markdown("""
            <span 
                title="例: アムロジピン" 
                style="text-decoration:underline;">
                高血圧の治療薬
            </span>
        """, unsafe_allow_html=True)
        d_HT = st.radio("選択", ("あり", "なし", "判断できない"), index=2, horizontal=True, key="d_HT_radio", label_visibility="collapsed")
        ss.d_HT = d_HT  
        
        st.markdown("""
            <span 
                title="例: リクシアナ" 
                style="text-decoration:underline;">
                抗凝固薬, 抗血小板薬, 抗不整脈薬
            </span>
        """, unsafe_allow_html=True)
        d_HF = st.radio("選択", ("あり", "なし", "判断できない"), index=2, horizontal=True, key="d_HF_radio", label_visibility="collapsed")
        ss.d_HF = d_HF  

        # 特食選択はまだ、変数変更のみ
        if st.button("次へ"):

            conditions_d = {
            "糖尿病薬": ss.d_DM,
            "脂質異常薬": ss.d_HL,
            "降圧薬": ss.d_HT,
            "心疾患薬": ss.d_HF
            }
            
            for condition_d, status in conditions_d.items():
                if status == "あり":
                    ss.risk += 1
                elif status == "判断できない":
                    ss.suggest.append("処方薬の内容を再確認")    
            ss.qp = 50

            st.rerun()

    elif qp == 50:
        #b_は血液検査値
        st.markdown("##### 血液検査データがある？")
        b_yn = st.radio("選択", ("あり", "なし"), index=1, horizontal=True, key="b_yn_radio", label_visibility="collapsed")
        ss.b_yn = b_yn  

        if st.button("次へ"):  
            if ss.b_yn  == "あり":
                ss.qp = 55
            elif ss.b_yn  == "なし":
                ss.suggest .append("血液検査を実施")
                ss.decision = 1
            st.rerun()

    elif qp == 55:
        st.markdown("#### 血液検査結果は？")
        
        a1c = st.text_input("HbA1c(%) :不明は0", value="5.0", key="a1c_input")
        ldl = st.text_input("LDL-cho(mg/dL) :不明は0", value="100", key="ldl_input")
        hdl = st.text_input("HDL-cho(mg/dL) :不明は0", value="50", key="hdl_input")
        tg_b = st.text_input("TG(mg/dL) :不明は0", value="100", key="tg_b_input")
        bnp = st.text_input("BNP(pg/dL) :不明は0", value="18.4", key="bnp_input")
        probnp = st.text_input("NT-proBNP(%) :不明は0", value="55", key="probnp_input")
        cre = st.text_input("Cre(mg/dL) :不明は0", value="1.0", key="cre_input")

        if st.button("次へ"):
            try:
                ss.a1c = float(a1c)
                ss.ldl = float(ldl)
                ss.hdl = float(hdl)
                ss.tg_b = float(tg_b)
                ss.bnp = float(bnp)
                ss.probnp = float(probnp)
                ss.cre = float(cre)

                if ss.meal == "tbd" and ss.risk >0 :
                    ss.qp = 1100
                else :
                    ss.decision = 1
                st.rerun()

            except ValueError:
                st.warning("数値を入力してください")

#血圧質問でrisk評価※

    elif ss.qp == 1100:
        st.markdown("##### 心エコーの結果がある？")
        hus = st.radio("選択", ("あり", "なし"), index=1, horizontal=True, key="hus_radio", label_visibility="collapsed")
        ss.hus = hus 

        if st.button("次へ"):  
            if ss.hus  == "あり":
                ss.qp = 1110
            elif ss.hus  == "なし":
                ss.decision = 2  
                ss.meal ="none"
                ss.suggest .append("心エコーの実施")
            st.rerun()


    elif qp == 1110:
        st.markdown("##### 心エコーに心疾患の所見がある？")
        usf = st.radio("選択", ("あり", "なし", "結果が判断できない"), index=2, horizontal=True, key="usf_radio", label_visibility="collapsed")
        st.write("例:EF<50※変更")
        ss.usf = usf  

        if st.button("次へ"):  
            if ss.usf  == "あり":
                ss.decision = 1
            elif ss.usf  == "なし":                
                ss.decision = 2  
                ss.meal ="none"
                ss.suggest .append("心エコーの実施")
            elif ss.usf  == "結果が判断できない":
                ss.decision = 2  
                ss.meal ="none"
            ss.suggest .append("心エコーの結果確認")
            st.rerun()
