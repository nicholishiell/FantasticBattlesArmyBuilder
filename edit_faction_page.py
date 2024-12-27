import streamlit as st
import pandas as pd

from utils import *
from web_app_utils import *

from Unit import Unit

column_names = ['Unit Name', 'Type', 'Res','Mov','Mel','Sht','Def','Traits','Pts','Delete']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def to_pandas_table(unit_roster):
    
    data = []
    for unit in unit_roster:
        data.append([unit.name,unit.unit_type, unit.resolve,unit.movement,unit.melee,f'{unit.shooting_short}/{unit.shooting_long}',unit.defense,unit.trait_strings,unit.points, False])
        
    df = pd.DataFrame(data, columns=column_names)
    
    return df

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def clear_add_new_unit_form():
    st.session_state.unit_name = ''
    st.session_state.unit_type = 'Warlord'
    st.session_state.trait_1 = 'None'
    st.session_state.trait_2 = 'None'
    st.session_state.trait_3 = 'None'
    st.session_state.unit_description = ''  

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def add_unit_callback(unit_name, unit_type, trait_1, trait_2, trait_3, description):
    
    unit = st.session_state.FACTION_BUILDER.create_unit(unit_name=unit_name, 
                                                        unit_description=description, 
                                                        unit_type=unit_type, 
                                                        racial_trait=st.session_state.ACTIVATE_FACTION.racial_trait, 
                                                        company_trait_1=trait_1, 
                                                        company_trait_2=trait_2, 
                                                        company_trait_3=trait_3)
    
    st.session_state.ACTIVATE_FACTION.add_unit(unit)
    
    clear_add_new_unit_form()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def edit_faction_page():
    
    if st.session_state.ACTIVATE_FACTION is None:
        st.warning('No Activate Faction selected. Please upload or create a faction to edit.')
    else:
        st.title(f'{st.session_state.ACTIVATE_FACTION.name}')
        st.markdown(st.session_state.ACTIVATE_FACTION.description)
        st.markdown(f'**Racial Trait:** { st.session_state.ACTIVATE_FACTION.racial_trait}')
        
        st.subheader('Unit Roster')
        st.data_editor( to_pandas_table(st.session_state.ACTIVATE_FACTION.unit_roster),
                        use_container_width=True,
                        hide_index=True,
                        disabled=column_names[1:-1])
        st.divider()
        
        st.subheader('Add Unit to Roster')
        
        name_col, type_col, trait_1_col, trait_2_col, trait_3_col = st.columns(5)
        
        unit_name = name_col.text_input('Unit Name',
                                        key='unit_name')
        
        unit_type = type_col.selectbox('Unit Type', 
                                       BASE_UNIT_TYPES,
                                       key='unit_type')
        
        trait_1 = trait_1_col.selectbox('Company Trait 1', 
                                        st.session_state[FACTION_BUILDER_KEY].traits_dict.keys(),
                                        key='trait_1')
        
        trait_2 = trait_2_col.selectbox('Company Trait 2', 
                                        st.session_state[FACTION_BUILDER_KEY].traits_dict.keys(),
                                        key='trait_2')
        
        trait_3 = trait_3_col.selectbox('Company Trait 3', 
                                        st.session_state[FACTION_BUILDER_KEY].traits_dict.keys(),
                                        key='trait_3')
        
        description = st.text_area('Unit Description',
                                   key='unit_description')
        
        st.button('Add Unit',
                  on_click=add_unit_callback,
                  args=(unit_name, unit_type, trait_1, trait_2, trait_3, description))
       