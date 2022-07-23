import streamlit as st
from streamlit_player import st_player
from streamlit_ace import st_ace, KEYBINDINGS, LANGUAGES, THEMES

st.set_page_config(page_title='Online IDE',
                   page_icon='🧑🏾‍💻',
                   layout='wide',
                   menu_items={
                       'Get help': 'https://google.com',
                   })

st.markdown("<h1 style='text-align: center;'>Welcome to Online IDE</h1>", unsafe_allow_html=True)
video_link = st.text_input(label='Enter link to video:')
col1, col2 = st.columns([2,1])

with col1:
    st_player(video_link, key='youtube_player')

with col2:
    content = st_ace(
        language= st.selectbox(label='Choose the coding language of your choice', options= ['python','javascript','java']) ,
        theme = st.selectbox(label='Choose a theme', options=['clouds','clouds_midnight']),
        keybinding= st.selectbox(label='Keybinding mode', options=KEYBINDINGS),
        auto_update= st.checkbox('Auto Update', value=False),
        show_gutter=st.checkbox("Show gutter", value=True),
        key='ace'
    )

    if content:
        st.subheader('Content')
        st.text(content)

