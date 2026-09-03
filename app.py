import streamlit as st

# --- НАСТРОЙКА СТРАНИЦЫ ---
st.set_page_config(
    page_title="Стас | Аналитик данных",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# --- CSS ---
def local_css():
    st.markdown("""
    <style>
        .stApp {
            background-color: #F4F6F9;
        }

        h1, h2, h3, h4, h5, h6 {
            color: #1E3A8A !important;
            font-weight: 700 !important;
        }

        p, li, span, div, .stMarkdown {
            color: #334155 !important;
            line-height: 1.6;
        }

        .project-card, .skill-block {
            background-color: #FFFFFF;
            padding: 25px;
            border-radius: 16px;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.06);
            margin-bottom: 20px;
            border: 1px solid rgba(0, 0, 0, 0.04);
        }

        .project-card {
            border-left: 6px solid #1E3A8A;
        }

        .tech-tag {
            background-color: #E0F2FE;
            color: #0369A1 !important;
            padding: 5px 16px;
            border-radius: 30px;
            font-size: 13px;
            font-weight: 600;
            display: inline-block;
            margin: 3px 6px 3px 0;
        }

        .stButton button {
            background: #FFFFFF !important;
            color: #1E3A8A !important;
            font-weight: 700 !important;
            border-radius: 12px !important;
            border: 2px solid #DBEAFE !important;
            padding: 0.7rem 2.5rem !important;
            transition: 0.3s !important;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04) !important;
            width: 100% !important;
            font-size: 16px !important;
        }

        .stButton button:hover {
            background: #EFF6FF !important;
            border-color: #93C5FD !important;
            box-shadow: 0 4px 16px rgba(30, 58, 138, 0.10) !important;
            transform: translateY(-2px) !important;
        }

        a {
            color: #1E3A8A !important;
            font-weight: 600;
            text-decoration: none;
            transition: 0.2s;
        }
        a:hover {
            color: #F97316 !important;
            text-decoration: underline;
        }

        .contact-item {
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 12px 16px;
            background-color: #F8FAFC;
            border-radius: 10px;
            margin-bottom: 10px;
            border: 1px solid #E2E8F0;
            transition: 0.2s;
        }
        .contact-item:hover {
            background-color: #EFF6FF;
            border-color: #93C5FD;
        }
        .contact-item .icon {
            font-size: 22px;
            width: 36px;
            text-align: center;
        }
        .contact-item .label {
            font-weight: 600;
            color: #1E3A8A !important;
            min-width: 80px;
        }
        .contact-item .value {
            color: #334155 !important;
        }

        .hero-text {
            font-size: 18px;
            color: #334155 !important;
            line-height: 1.8;
        }

        .coming-soon {
            background: linear-gradient(135deg, #EFF6FF 0%, #F8FAFC 100%);
            padding: 40px;
            border-radius: 20px;
            border: 2px dashed #93C5FD;
            text-align: center;
        }
        .coming-soon h3 {
            color: #1E3A8A !important;
        }
        .coming-soon p {
            color: #475569 !important;
            font-size: 16px;
        }

        .avatar-placeholder {
            background: linear-gradient(135deg, #DBEAFE, #EFF6FF);
            width: 200px;
            height: 200px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 80px;
            color: #1E3A8A;
            box-shadow: 0 8px 30px rgba(30, 58, 138, 0.12);
            border: 4px solid #FFFFFF;
        }

        .footer {
            text-align: center;
            color: #94A3B8 !important;
            margin-top: 50px;
            padding: 25px 0;
            border-top: 2px solid #E2E8F0;
            font-size: 14px;
        }
    </style>
    """, unsafe_allow_html=True)


local_css()

# --- ШАПКА ---
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("""
    <div class="avatar-placeholder">
        📊
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    # Привет, я Стас 👋
    ## Аналитик данных Junior+
    """)
    st.markdown("""
    <div class="hero-text">
        Превращаю сырые данные в понятные инсайты.<br>
        Строю пайплайны, визуализирую метрики и помогаю бизнесу принимать решения на основе данных.
    </div>
    """, unsafe_allow_html=True)

    col_btn1, col_btn2 = st.columns(2)

    with col_btn1:
        st.markdown("""
        <a href="https://your-link-to-resume.pdf" target="_blank">
            <button style="
                background: #FFFFFF;
                color: #1E3A8A;
                font-weight: 700;
                border-radius: 12px;
                border: 2px solid #DBEAFE;
                padding: 0.7rem 2.5rem;
                width: 100%;
                font-size: 16px;
                cursor: pointer;
                transition: 0.3s;
                box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
            " onmouseover="this.style.background='#EFF6FF'; this.style.borderColor='#93C5FD';" 
              onmouseout="this.style.background='#FFFFFF'; this.style.borderColor='#DBEAFE';">
                📄 Скачать резюме
            </button>
        </a>
        """, unsafe_allow_html=True)

    with col_btn2:
        st.markdown("""
        <a href="#contacts">
            <button style="
                background: #FFFFFF;
                color: #1E3A8A;
                font-weight: 700;
                border-radius: 12px;
                border: 2px solid #DBEAFE;
                padding: 0.7rem 2.5rem;
                width: 100%;
                font-size: 16px;
                cursor: pointer;
                transition: 0.3s;
                box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
            " onmouseover="this.style.background='#EFF6FF'; this.style.borderColor='#93C5FD';" 
              onmouseout="this.style.background='#FFFFFF'; this.style.borderColor='#DBEAFE';">
                📬 Связаться
            </button>
        </a>
        """, unsafe_allow_html=True)

st.markdown("---")

# --- СТЕК ---
st.header("🛠️ Мой стек")
st.caption("Инструменты, с которыми я работаю ежедневно")

col_skills1, col_skills2, col_skills3 = st.columns(3)

with col_skills1:
    st.markdown("""
    <div class="skill-block">
        <h4>🗄️ Базы данных & SQL</h4>
        <ul>
            <li>PostgreSQL / Greenplum</li>
            <li>Оконные функции, CTE</li>
            <li>Оптимизация запросов</li>
            <li>SQLAlchemy</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col_skills2:
    st.markdown("""
    <div class="skill-block">
        <h4>🐍 Python & Анализ</h4>
        <ul>
            <li>pandas, NumPy</li>
            <li>requests (API)</li>
            <li>Matplotlib, Seaborn</li>
            <li>ETL-пайплайны</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col_skills3:
    st.markdown("""
    <div class="skill-block">
        <h4>📊 BI & Визуализация</h4>
        <ul>
            <li>Tableau (в процессе)</li>
            <li>DataLens</li>
            <li>Excel: Power Query / Pivot</li>
            <li>Git / GitHub</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- ПРОЕКТЫ ---
st.header("📂 Проекты")

st.markdown("""
<div class="coming-soon">
    <h3>🚀 Проекты в разработке</h3>
    <p>
        Сейчас я активно работаю над кейсами, которые покажу здесь уже в ближайшее время.<br>
        А пока можешь посмотреть мои <strong>учебные проекты</strong> на GitHub.
    </p>
    <br>
    <a href="https://github.com/yourusername" target="_blank" style="font-size: 18px;">
        🔗 Перейти на GitHub →
    </a>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# --- КОНТАКТЫ (СТАНДАРТНЫЙ STREAMLIT) ---
st.header("📬 Свяжитесь со мной")
st.write("Буду рад обсудить сотрудничество или интересные проекты!")

st.markdown("""
**💬 Telegram:** [@your_telegram](https://t.me/your_telegram_username)  
**📧 Email:** [your.email@example.com](mailto:your.email@example.com)  
**🔗 LinkedIn:** [linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile)  
**🐙 GitHub:** [github.com/yourusername](https://github.com/yourusername)  
**📊 Kaggle:** [kaggle.com/yourusername](https://kaggle.com/yourusername)  
""")