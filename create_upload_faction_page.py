import streamlit as st

from web_app_utils import *
from Faction import Faction

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def create_faction_callback(name, racial_trait, description):
    st.info(f'{name} faction created!')

    st.session_state[ACTIVATE_FACTION_KEY] = Faction(name=name, 
                                                     description=description, 
                                                     racial_trait=racial_trait)
    
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def create_upload_faction_page():

    st.title('Create/Upload Faction')

    faction_name_col, racial_trait_col = st.columns(2)

    faction_name = faction_name_col.text_input('Faction Name', 
                                               #placeholder='Enter the name of your faction here...',
                                               'Righteous Elves')

    racial_trait = racial_trait_col.selectbox(  'Racial Traits', 
                                                options=list(st.session_state[FACTION_BUILDER_KEY].traits_dict.keys()),
                                                index=13)

    description = st.text_input('Faction Description', 
                                #placeholder='Enter a description of your faction here...',
                                'The Righteous Elves are a noble, and good, but kinda pricks too.')
    
    st.button('Create Faction',
              on_click=create_faction_callback,
              args=(faction_name, racial_trait, description))