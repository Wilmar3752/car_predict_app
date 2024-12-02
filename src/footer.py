import streamlit as st
def add_footer():
    st.markdown(
        """
        <style>
        footer {
            visibility: hidden;
        }
        .footer {
            margin-top: 50px;
            text-align: center;
            padding: 10px 0;
            font-size: 14px;
            color: var(--text-color);
            background-color: var(--background-secondary-color);
        }
        .footer a {
            color: var(--primary-color);
            text-decoration: none;
            margin: 0 10px;
        }
        .footer a:hover {
            text-decoration: underline;
        }
        .footer img {
            vertical-align: middle;
            width: 20px;
            height: 20px;
            margin-right: 5px;
        }
        </style>
        <div class="footer">
            Hecho con ❤️ por <a href="https://wilmarsepulveda.com/" target="_blank">Wilmar</a> | 
            Contacto: <a href="mailto:wilmar.sepulveda2@gmail.com">wilmar.sepulveda2@gmail.com</a>
            <div style="margin-top: 10px;">
                <a href="https://www.linkedin.com/in/wilmar3752/" target="_blank">
                    <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn"> LinkedIn
                </a>
                <a href="https://github.com/wilmar3752" target="_blank">
                    <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub"> GitHub
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )




