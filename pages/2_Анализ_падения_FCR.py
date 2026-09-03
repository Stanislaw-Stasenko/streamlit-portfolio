import streamlit as st

st.set_page_config(
    page_title="Анализ падения FCR",
    page_icon="📞",
    layout="wide"
)

st.title("📞 Анализ падения FCR в контакт-центре")
st.markdown("""
**Дата:** сентябрь 2026  
**Задача:** Проверить гипотезу, что падение FCR (First Call Resolution) в августе связано с работой новых операторов.

---

## 📊 Суть проекта

Проанализировал 10 000 звонков за август 2026 и выяснил:

1. Новички действительно хуже решают звонки — разница **10 п.п.** (p < 0.001)
2. Падение FCR после 20 августа вызвано **изменением состава смен**
3. **Время разговора не влияет** на успешность решения проблемы

---

## 📈 Ключевые метрики
""")

# Метрики без загрузки данных
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Всего звонков", "10 000")
with col2:
    st.metric("Средний FCR", "63%")
with col3:
    st.metric("Средний AHT", "308 сек")
with col4:
    st.metric("Операторов", "50")

st.divider()

# --- ВСТАВЛЯЕМ СКРИНШОТЫ ---
st.subheader("📉 Динамика FCR по дням")
st.image("images/fcr_dynamics.png", caption="Динамика FCR: новички vs опытные", use_container_width=True)

st.subheader("⏱️ Сравнение AHT")
st.image("images/aht_boxplot.png", caption="Время разговора по типам сотрудников", use_container_width=True)

st.divider()

# --- КЛЮЧЕВЫЕ ВЫВОДЫ ---
st.header("🎯 Ключевые выводы и рекомендации")

col_left, col_right = st.columns(2)

with col_left:
    st.markdown("""
    ### 🔍 Что выяснили
    1. **Новички хуже решают звонки** — разница 10 п.п. (p < 0.001)
    2. **Падение FCR после 20 августа** — связано с изменением состава смен
    3. **Время разговора не влияет** на FCR
    """)

with col_right:
    st.markdown("""
    ### 💡 Рекомендации
    1. Норматив: **≥ 50% опытных** в смене
    2. Пересмотреть **распределение нагрузки**
    3. Дополнительное **обучение новичков**
    4. Еженедельный **мониторинг** состава смен
    """)

st.divider()

# --- ССЫЛКА НА GITHUB ---
st.markdown("""
<div style="text-align: center; margin-top: 20px; padding: 30px; background: #F8FAFC; border-radius: 16px;">
    <h3>📂 Полный анализ на GitHub</h3>
    <p style="color: #475569;">
        Весь код, данные и Jupyter Notebook с полным исследованием доступны в репозитории.
    </p>
    <a href="https://github.com/Stanislaw-Stasenko/Analysis_FCR_Drop" target="_blank" style="
        background: #1E3A8A;
        color: #FFFFFF !important;
        padding: 12px 40px;
        border-radius: 12px;
        text-decoration: none;
        font-weight: 600;
        display: inline-block;
        margin-top: 10px;
    ">
        🔗 Открыть репозиторий на GitHub
    </a>
</div>
""", unsafe_allow_html=True)