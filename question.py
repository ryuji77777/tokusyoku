import streamlit as st

ss = st.session_state

def question(qp):
    if qp == 10:
        # 年齢性別 #※年齢未
        age = st.number_input("年齢は?", min_value=0, max_value=200, step=1, value=70, key="age_input")
        gender = st.radio("性別は?", ("男性", "女性", "不明"), index=2, horizontal=True, key="gender_radio")

        ss.age = age
        ss.gender = gender

        if age > 0 and st.button("次へ"):
            ss.qp = 20
            st.rerun()
        
    elif qp == 20:
        # 既往歴追加※
        st.markdown("##### 合併している病名は？")
        PMH = st.radio("選択", ("なし", "心不全", "不明"), index=2, horizontal=True, key="PMH_radio", label_visibility="collapsed")
        ss.PMH = PMH  
        
        if st.button("次へ"):  
            if ss.PMH == "なし":
                ss.qp = 30
            elif ss.PMH == "心不全":
                ss.meal = "心臓食"
                ss.reason =  "理由：病名あり。現在の治療状況を確認すること"
            elif ss.PMH == "不明":
                ss.qp = 30
                ss.suggest .append("身体疾患の病歴を確認")#サンプル
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
                ss.qp = 1000 #※変更
                ss.suggest .append("処方薬の情報を取得")
            st.rerun()

    #処方がある場合の内容
    #※「判断できない」　
    #※選択後の分岐フロー
    elif qp == 35:
        st.markdown("#### 処方内容に下記がある？")
        st.markdown("###### 糖尿病の治療薬")
        st.write("例:メトホルミン※追加")
        d_DM = st.radio("選択", ("あり", "なし", "処方薬が分からない"), index=2, horizontal=True, key="d_DM_radio", label_visibility="collapsed")
        ss.d_DM = d_DM  

        st.markdown("###### 脂質異常症の治療薬")
        st.write("例:プラバスタチン※追加")
        d_HL = st.radio("選択", ("あり", "なし", "処方薬が分からない"), index=2, horizontal=True, key="d_HL_radio", label_visibility="collapsed")
        ss.d_HL = d_HL  

        st.markdown("###### 高血圧の治療薬")
        st.write("例:アムロジピン※追加")
        d_HT = st.radio("選択", ("あり", "なし", "処方薬が分からない"), index=2, horizontal=True, key="d_HT_radio", label_visibility="collapsed")
        ss.d_HT = d_HT  
        
        st.markdown("###### 抗凝固薬, 抗血小板薬, 抗不整脈薬")
        st.write("例:リクシアナ※追加")
        d_HF = st.radio("選択", ("あり", "なし", "処方薬が分からない"), index=2, horizontal=True, key="d_HF_radio", label_visibility="collapsed")
        ss.d_HF = d_HF  
        

        if st.button("次へ"):  
        #糖尿病薬
            if ss.d_DM  == "あり":
                ss.meal = "糖尿病食"
                ss.reason =  "理由：処方あり。治療状況を確認すること"
            elif ss.d_DM  == "なし":
                ss.qp = 40
            elif ss.d_DM  == "処方薬が分からない":
                ss.qp = 40
                ss.suggest .append("処方薬の内容を再確認")
            st.rerun()

        #脂質異常薬
            if ss.d_HL  == "あり":
                ss.meal = "脂質異常食"
                ss.reason =  "理由：処方あり。治療状況を確認すること"
            elif ss.d_HL  == "なし":
                ss.qp = 50 
            elif ss.d_HL  == "処方薬が分からない":
                ss.qp = 50 
                ss.suggest .append("処方薬の内容を再確認")
            st.rerun()

        #降圧薬　あれば心臓リスク
            if ss.d_HT  == "あり":
                ss.qp = 1000 #変更心臓系
            elif ss.d_HT  == "なし":
                ss.qp = 60 
            elif ss.d_HT  == "処方薬が分からない":
                ss.qp = 60 
                ss.suggest .append("処方薬の内容を再確認")
            st.rerun()

        #心疾患薬　あれば心臓リスク
            if ss.d_HF  == "あり":
                ss.qp = 1000 #変更心臓系
                ss.risk += 1
            elif ss.d_HF  == "なし":
                ss.qp = 1000 #変更
            elif ss.d_HF  == "処方薬が分からない":
                ss.qp = 1000 #変更
                ss.suggest .append("処方薬の内容を再確認")
            st.rerun()


    elif qp == 1000:
        st.markdown("※開発中 なしなら心エコーor 常食")
        fin = st.radio("選択", ("あり", "なし"), index=1, horizontal=True, key="fin_radio", label_visibility="collapsed")
        ss.fin = fin  

        if st.button("次へ"):  
            if ss.fin  == "最後あり":
                ss.meal = "最後食"
                ss.suggest .append("推奨最後")
            elif ss.fin  == "なし":
                if ss.risk == 0:
                    ss.meal = "none"
                else:
                    ss.qp =1100
            st.rerun()

    elif qp == 1100:
        st.markdown("##### 心エコーの結果がある？")
        hus = st.radio("選択", ("あり", "なし"), index=1, horizontal=True, key="hus_radio", label_visibility="collapsed")
        ss.hus = hus 

        if st.button("次へ"):  
            if ss.hus  == "あり":
                ss.qp = 1110
            elif ss.hus  == "なし":
                ss.meal = "none"
                ss.suggest .append("心エコーの実施")
            st.rerun()


    elif qp == 1110:
        st.markdown("##### 心エコーに心不全所見がある？")
        usf = st.radio("選択", ("あり", "なし", "結果が判断できない"), index=2, horizontal=True, key="usf_radio", label_visibility="collapsed")
        st.write("例:EF<50※変更")
        ss.usf = usf  

        if st.button("次へ"):  
            if ss.usf  == "あり":
                ss.meal = "心臓食"
                ss.reason =  "理由：血管リスクあり、エコー所見をともなう。治療状況を確認"
            elif ss.usf  == "なし":
                ss.meal = "none"
            elif ss.usf  == "結果が判断できない":
                ss.meal = "none"
                ss.suggest .append("心エコーの結果確認")
            st.rerun()


#以下変更

    elif qp == 1000:
        st.markdown("※質問開発中 なしなら常食")
        d_fn = st.radio("選択", ("あり", "なし"), index=1, horizontal=True, key="d_fn_radio", label_visibility="collapsed")
        ss.d_fn = d_fn  

        if st.button("次へ"):  
            if ss.d_fn  == "あり":
                ss.meal = "none"
                ss.suggest .append("追加推奨")
            elif ss.d_fn  == "なし":
                ss.meal = "none"
            st.rerun()

#risk＋行の追加
#データ不足の場合　※不要？ suggestありなしで決定
#                ss.meal = "nodata"
