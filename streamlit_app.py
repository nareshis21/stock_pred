import streamlit as st
import requests

st.title("Predictive Model App")

# Create input fields
high = st.number_input("High", format="%f")
low = st.number_input("Low", format="%f")
open_val = st.number_input("Open", format="%f")  # renamed to avoid conflict with the built-in open function
volume = st.number_input("Volume", format="%f")

url = "https://nareshstp.pythonanywhere.com/predict"

# Create a button to trigger the prediction
if st.button("Predict"):
    # Prepare the parameters for the POST request
    params = {
        "high": str(high),
        "low": str(low),
        "open": str(open_val),
        "volume": str(volume)
    }
    
    # Make the POST request
    try:
        response = requests.post(url, data=params)
        
        # Parse the response and display the result
        if response.status_code == 200:
            result_data = response.json()
            
            # Display the result in a bigger font and inside a text box
            st.markdown(f"## Result")
            st.markdown(f"<div style='background-color: ##050505; padding: 20px; border-radius: 5px;'><span style='font-size: 24px;'>{result_data.get('res')}</span></div>", unsafe_allow_html=True)
        else:
            st.error(f"API Error: {response.status_code}. {response.text}")
            
    except Exception as e:
        st.error(f"Error: {e}")
