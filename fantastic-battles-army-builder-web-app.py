import streamlit as st

from utils import *
from web_app_utils import *

from home_page import home_page
from create_upload_faction_page import create_upload_faction_page
from edit_faction_page import edit_faction_page

st.set_page_config(page_title="Fantastic Battles Army Builder", page_icon="🎲",
                   layout="wide")

initialize_session_state()

user_page_selection = st.sidebar.radio('Pages', 
                                        options=PAGES_LIST)

if user_page_selection == CREATE_UPLOAD_FACTION_PAGE:
    create_upload_faction_page()
elif user_page_selection == EDIT_FACTION_PAGE:
    edit_faction_page()
else:
    home_page()
