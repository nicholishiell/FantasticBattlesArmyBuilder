import streamlit as st

from UnitBuilder import UnitBuilder

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

HOME_PAGE = "Home"
CREATE_UPLOAD_FACTION_PAGE = "Create/Upload Faction"
EDIT_FACTION_PAGE = "Edit Faction"

PAGES_LIST = [HOME_PAGE, CREATE_UPLOAD_FACTION_PAGE, EDIT_FACTION_PAGE]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

FACTION_BUILDER_KEY = "FACTION_BUILDER"
ACTIVATE_FACTION_KEY = "ACTIVATE_FACTION"

def initialize_session_state():
    
    if FACTION_BUILDER_KEY not in st.session_state:
        st.session_state[FACTION_BUILDER_KEY] = UnitBuilder()
        
    if ACTIVATE_FACTION_KEY not in st.session_state:
        st.session_state[ACTIVATE_FACTION_KEY] = None
        
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~