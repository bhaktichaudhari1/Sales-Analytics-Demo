import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="3D Tech Sales Lab", layout="wide")

st.title("📊 3D Software & Design Services: Sales Suite")
st.markdown("Performance testing suite optimized for large-scale transaction arrays.")

uploaded_file = st.file_uploader("Upload your sales_data_100k.csv file", type="csv")

if uploaded_file is not None:
    # 1. Fast Load Data
    df = pd.read_csv(uploaded_file)
    
    # Convert dates and extract quarters instantly
    df['Transaction_Date'] = pd.to_datetime(df['Transaction_Date'])
    df['Quarter'] = df['Transaction_Date'].dt.to_period('Q').astype(str)

    # 2. Executive Ratios
    total_revenue = df['Revenue'].sum()
    total_profit = df['Profit'].sum()
    margin = (total_profit / total_revenue) * 100

    st.header("1. Financial Summary Overview")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total Ingested Rows", f"{len(df):,}")
    m2.metric("Gross Revenue", f"${total_revenue:,.2f}")
    m3.metric("Net Profit", f"${total_profit:,.2f}")
    m4.metric("Net Profit Margin", f"{margin:.1f}%")

    st.divider()

    # 3. Aggregated Visualizations (Performance Optimized)
    st.header("2. Trend Optimization Analysis")
    
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.subheader("Quarterly Financial Velocity")
        # Crunching 100k rows down to 8 row segments BEFORE sending to Plotly
        q_summary = df.groupby('Quarter')[['Revenue', 'Profit']].sum().reset_index()
        
        fig_trend = px.bar(q_summary, x='Quarter', y=['Revenue', 'Profit'],
                           barmode='group',
                           title="Quarterly Revenue vs Net Profit Performance",
                           color_discrete_sequence=['#636EFA', '#00CC96'])
        st.plotly_chart(fig_trend, use_container_width=True)

    with col_right:
        st.subheader("Segment Composition (Mix)")
        # Crunching 100k rows down to 2 metrics
        segment_summary = df.groupby('Segment')['Revenue'].sum().reset_index()
        
        fig_pie = px.pie(segment_summary, names='Segment', values='Revenue',
                         hole=0.4, title="Revenue Allocation: Software vs. Services",
                         color_discrete_sequence=['#AB63FA', '#FFA15A'])
        st.plotly_chart(fig_pie, use_container_width=True)

    # 4. Regional Drill-Down Component
    st.subheader("Regional Performance Allocation Matrix")
    region_summary = df.groupby(['Region', 'Segment'])['Profit'].sum().reset_index()
    fig_sun = px.sunburst(region_summary, path=['Region', 'Segment'], values='Profit',
                          title="Profit Volume Map: Region > Segment",
                          color='Profit', color_continuous_scale='Blues')
    st.plotly_chart(fig_sun, use_container_width=True)

    # 5. Row-Limiting Data Grid (Prevents Browser Freeze)
    st.header("3. Transaction Ledger Ledger Preview")
    st.markdown("Showing first 100 rows to optimize browser rendering memory limits.")
    st.dataframe(df.head(100), use_container_width=True)