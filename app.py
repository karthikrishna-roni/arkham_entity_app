import streamlit as st 
from data_prep import all_data_prep


st.write("INSTRUCTIONS!")
st.write("1. If Entity is selected 'None', then the balance of all the Entities are displayed")
st.write("2. If required Entity is selected, you coudld go more granular on Label level, else the graph will be on Entity level (i.e Label = None)")

entity = 'None'
label = 'None'

st.sidebar.title("Arkham EDA")
entity = st.sidebar.selectbox("Select Entity",options=('None','Grayscale','BlackRock','U.S. Government','Franklin Templeton','Fidelity'))

if entity!='None':
    if entity=='Grayscale':
        label = st.sidebar.selectbox("Select Label",options=('None','Bitcoin Trust', 'Digital Large Cap Fund', 'UNKNOWN',
        'Coinbase Prime Deposit'))
        
    if entity=='BlackRock':
        label = st.sidebar.selectbox("Select Label",options=('None','IBIT Bitcoin ETF'))

    if entity=='U.S. Government':
        label = st.sidebar.selectbox("Select Label",options=('None','Bitfinex Hacker Seized Funds', 'Ryan Farace Seized Funds',
        'Alexandre Cazes Seized Address', 'UNKNOWN',
        'Edward Cantor Seized Funds', 'Sae-Heng Confiscated Funds',
        'Gery Shanlon Seized Funds',
        'Potapenko/Turogin Funds Seized Address',
        'Potapenko/Turogin Funds Seized Funds',
        'DOJ Confiscated Silk Road Funds',
        'Silk Road Individual X FBI Confiscated Funds',
        'James Zhong Seizure', 'Bitfinex Hack Recovery (FBI)',
        'Gary Harmon Seized Funds', 'Silk Road DOJ Confiscated Funds',
        'Gaurang S. Sharma Seized Funds',
        'Darkside Ransomware Seized Address', 'Gery Shalon Seized Funds',
        'James Zhong Seized Funds', 'Darkside Ransomware Seized Funds'))
        
    if entity=='Franklin Templeton':
        label = st.sidebar.selectbox("Select Label",options=('None','EZBC Bitcoin ETF'))

    if entity=='Fidelity':
        label = st.sidebar.selectbox("Select Label",options=('None','FBTC Bitcoin ETF'))

gh = st.sidebar.selectbox("Select Graph type",options=('Histogram','Line Graph'))
range = st.sidebar.selectbox("Select Range",options=('None','0-44,000','44,000-88,000','88,000-1,32,000','1,32,000-1,76,000','1,76,000-2,20,000','>2,20,000'))

if gh=='Line Graph':
    # info_slot.empty()
    res = all_data_prep(entity,label,gh,range)
    button =  st.sidebar.button('Click Here to Get the Plot the graph')
    if button:
        st.plotly_chart(res)
    
if gh=='Histogram':
    # info_slot.empty()
    res = all_data_prep(entity,label,gh,range)
    button =  st.sidebar.button('Click Here to Get the Plot the graph')
    if button:
        st.plotly_chart(res)
    