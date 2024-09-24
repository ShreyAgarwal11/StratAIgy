import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(page_title="startAIgy", layout="wide")

# Home Section
st.title("StartAIgy")
st.write("")
st.write("")
st.title("Let AI Help You with Your Business")
st.markdown(
    """
    <style>
    .fade-in-text {
        animation: fadeIn 3s ease-in;
    }

    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
    </style>

    <h3 class="fade-in-text">Harness the power of AI to drive your business forward with our innovative solutions.</h3>
    """,
    unsafe_allow_html=True
)
st.write("")
st.write("")
st.write("")
st.write("")

# Solutions Section
st.header("Our AI Business Solutions")
st.subheader("Pricing")
st.write("Let AI help you set the right price for your product")

# Generate random pricing data
np.random.seed(0)
dates = pd.date_range(start='2024-01-01', periods=30)
prices = np.random.randint(50, 150, size=30)

# Create a DataFrame
data = pd.DataFrame({'Date': dates, 'Price': prices})

# Set the index to the date for better charting
data.set_index('Date', inplace=True)

# Display the line chart
st.line_chart(data, use_container_width=True)

# Inventory Management Section
st.subheader("Inventory Management")
st.write("Forecast orders including seasonal changes to properly manage your inventory")

# Generate random inventory data
categories = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
values = np.random.randint(10, 100, size=len(categories))

# Create a DataFrame
inventory_data = pd.DataFrame({'Category': categories, 'Values': values})

# Set the index to the category for better charting
inventory_data.set_index('Category', inplace=True)

# Display the bar chart
st.bar_chart(inventory_data)

# Customer Insight Section
st.subheader("Customer Insight")
st.write("Find unrealized upside and target potential customers")

# Generate random customer data
num_customers = 10
latitudes = np.random.uniform(low=-90.0, high=90.0, size=num_customers)
longitudes = np.random.uniform(low=-180.0, high=180.0, size=num_customers)
customer_names = [f'Customer {i + 1}' for i in range(num_customers)]

# Create a DataFrame for customers with renamed columns
customers = pd.DataFrame({
    'Name': customer_names,
    'lat': latitudes,    # Renamed to 'lat'
    'lon': longitudes    # Renamed to 'lon'
})

# Display customer locations on a map
st.map(customers)

# Contact Us Section
st.title("Contact Us")
st.write("For inquiries, please reach out:")
st.write("📞 **Phone Number:** +1 (213) 691-9782")
st.write("📧 **Email:** info@startAIgy.com")

# Footer
st.markdown("---")
st.markdown("### © 2024 StartAIgy. All Rights Reserved.")








