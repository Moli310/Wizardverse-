import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import base64
from pathlib import Path

# -------------------- Page Config --------------------
st.set_page_config(
    page_title="WizardVerse AI Dashboard",
    layout="wide",
    page_icon="🪄"
)

# -------------------- Background Image --------------------
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_local("assets/dark_data_bg.png")

# -------------------- Title --------------------
st.markdown("<h1 style='color: gold; text-align: center;'>WizardVerse AI: Books vs Movies</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='color: #FFD700; text-align: center;'>Analyzing the Magic of Harry Potter — Sentiments, Houses, and More</h4>", unsafe_allow_html=True)

# -------------------- Load Data --------------------
novels_df = pd.read_csv("data/novels_data.csv")
movies_df = pd.read_csv("data/movies_data.csv")

# -------------------- Section 1: Overview --------------------
st.markdown("## 📊 Overview")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Novel Entries", novels_df.shape[0])
col2.metric("Total Movie Entries", movies_df.shape[0])
col3.metric("Unique Houses", novels_df['house'].nunique())
col4.metric("Sentiment Classes", novels_df['sentiment'].nunique())

# -------------------- Section 2: Sentiment Analysis --------------------
st.markdown("## 🧙 Sentiment Analysis Comparison")
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Novels")
    fig1 = px.histogram(
        novels_df, x="sentiment", color="house", barmode="group",
        color_discrete_sequence=px.colors.sequential.Gold
    )
    fig1.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="gold")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.markdown("### Movies")
    fig2 = px.histogram(
        movies_df, x="sentiment", color="house", barmode="group",
        color_discrete_sequence=px.colors.sequential.Gold
    )
    fig2.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="gold")
    st.plotly_chart(fig2, use_container_width=True)

# -------------------- Section 3: House Distribution --------------------
st.markdown("## 🏰 House Distribution")
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Novels")
    house_counts_novels = novels_df['house'].value_counts().reset_index()
    fig3 = px.pie(house_counts_novels, names='index', values='house', color_discrete_sequence=px.colors.sequential.Gold)
    fig3.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color="gold")
    st.plotly_chart(fig3, use_container_width=True)

with col2:
    st.markdown("### Movies")
    house_counts_movies = movies_df['house'].value_counts().reset_index()
    fig4 = px.pie(house_counts_movies, names='index', values='house', color_discrete_sequence=px.colors.sequential.Gold)
    fig4.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color="gold")
    st.plotly_chart(fig4, use_container_width=True)

# -------------------- Section 4: Sentiment Trends --------------------
st.markdown("## 📈 Sentiment Trends Over Time")
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Novels Timeline")
    fig5 = px.line(novels_df, x="chapter_number", y="sentiment_score", color="house",
                   color_discrete_sequence=px.colors.sequential.Gold)
    fig5.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="gold")
    st.plotly_chart(fig5, use_container_width=True)

with col2:
    st.markdown("### Movies Timeline")
    fig6 = px.line(movies_df, x="scene_number", y="sentiment_score", color="house",
                   color_discrete_sequence=px.colors.sequential.Gold)
    fig6.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="gold")
    st.plotly_chart(fig6, use_container_width=True)

# -------------------- Section 5: Additional Insights --------------------
st.markdown("## 🔮 Additional Insights")
st.markdown("- Compare sentiment distributions between books and movies")
st.markdown("- Identify most emotionally intense chapters/scenes")
st.markdown("- Track house-specific sentiment trends")

# -------------------- Footer --------------------
st.markdown("<p style='color: gold; text-align: center;'>Made with ❤️ by Moli | Data & AI Enthusiast</p>", unsafe_allow_html=True)

