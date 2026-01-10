import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# =============================
# PAGE CONFIGURATION
# =============================
st.set_page_config(
    page_title="StreamElite | Premium Streaming Analytics",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================
# GOLD + BLACK PREMIUM THEME
# =============================
def apply_premium_theme():
    st.markdown("""
    <style>
    /* MAIN BACKGROUND */
    body, .stApp {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 100%);
        color: #f5c77a;
        font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
    }
    
    /* CARD DESIGN - PREMIUM GLASS EFFECT */
    .card {
        background: linear-gradient(145deg, rgba(15, 15, 15, 0.95), rgba(26, 26, 26, 0.95));
        backdrop-filter: blur(10px);
        border-radius: 24px;
        padding: 30px;
        margin-bottom: 25px;
        border: 1px solid rgba(245, 199, 122, 0.25);
        box-shadow: 
            0 8px 32px rgba(245, 199, 122, 0.15),
            inset 0 1px 0 rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
    }
    
    .card:hover {
        border-color: rgba(245, 199, 122, 0.4);
        box-shadow: 
            0 12px 48px rgba(245, 199, 122, 0.25),
            inset 0 1px 0 rgba(255, 255, 255, 0.15);
        transform: translateY(-2px);
    }
    
    /* TYPOGRAPHY - LUXURY STYLE */
    h1, h2, h3 {
        color: #f5c77a !important;
        font-weight: 800 !important;
        letter-spacing: 0.5px;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
        margin-bottom: 1.5rem !important;
    }
    
    h1 {
        font-size: 2.8rem !important;
        background: linear-gradient(90deg, #f5c77a, #ffd98e);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        position: relative;
    }
    
    h1:after {
        content: '';
        position: absolute;
        bottom: -10px;
        left: 0;
        width: 100px;
        height: 3px;
        background: linear-gradient(90deg, #f5c77a, transparent);
        border-radius: 2px;
    }
    
    /* INPUT CONTROLS - LUXURY STYLE */
    .stSelectbox > div, .stNumberInput > div, .stSlider > div, .stRadio > div {
        background: rgba(18, 18, 18, 0.9) !important;
        border: 1.5px solid rgba(245, 199, 122, 0.3) !important;
        border-radius: 12px !important;
        color: #f5c77a !important;
        transition: all 0.3s ease;
    }
    
    .stSelectbox > div:hover, .stNumberInput > div:hover, 
    .stSlider > div:hover, .stRadio > div:hover {
        border-color: rgba(245, 199, 122, 0.6) !important;
        box-shadow: 0 0 20px rgba(245, 199, 122, 0.15);
    }
    
    /* BUTTONS - PREMIUM GOLD GRADIENT */
    .stButton > button {
        background: linear-gradient(135deg, #f5c77a 0%, #ffd98e 100%);
        color: #0a0a0a !important;
        border-radius: 12px;
        padding: 14px 28px;
        font-size: 16px;
        font-weight: 700;
        border: none;
        box-shadow: 
            0 4px 20px rgba(245, 199, 122, 0.4),
            0 2px 4px rgba(0, 0, 0, 0.3);
        transition: all 0.3s ease;
        letter-spacing: 0.5px;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 
            0 8px 30px rgba(245, 199, 122, 0.6),
            0 4px 8px rgba(0, 0, 0, 0.4);
        background: linear-gradient(135deg, #ffd98e 0%, #f5c77a 100%);
    }
    
    /* METRICS - PREMIUM CARDS */
    [data-testid="metric-container"] {
        background: rgba(15, 15, 15, 0.7) !important;
        border: 1px solid rgba(245, 199, 122, 0.2);
        border-radius: 16px;
        padding: 20px;
    }
    
    [data-testid="metric-label"] {
        color: #b0b0b0 !important;
        font-size: 14px;
        font-weight: 600;
        letter-spacing: 0.5px;
    }
    
    [data-testid="metric-value"] {
        color: #f5c77a !important;
        font-size: 2rem;
        font-weight: 800;
    }
    
    /* SIDEBAR - DARK LUXURY */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f0f0f 0%, #1a1a1a 100%);
        border-right: 1px solid rgba(245, 199, 122, 0.1);
    }
    
    .sidebar .sidebar-content {
        background: transparent !important;
    }
    
    /* PROGRESS BAR - GOLD STYLE */
    .stProgress > div > div {
        background: linear-gradient(90deg, #f5c77a, #ffd98e);
        border-radius: 10px;
    }
    
    /* TABS - PREMIUM STYLE */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: rgba(18, 18, 18, 0.8) !important;
        border: 1px solid rgba(245, 199, 122, 0.2) !important;
        color: #b0b0b0 !important;
        border-radius: 12px !important;
        padding: 10px 24px !important;
        transition: all 0.3s ease;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        border-color: rgba(245, 199, 122, 0.4) !important;
        color: #f5c77a !important;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, rgba(245, 199, 122, 0.2), rgba(255, 217, 142, 0.1)) !important;
        border-color: #f5c77a !important;
        color: #f5c77a !important;
    }
    
    /* CONTENT BADGES */
    .content-badge {
        display: inline-block;
        padding: 12px 30px;
        border-radius: 25px;
        font-weight: 800;
        letter-spacing: 1px;
        text-transform: uppercase;
        font-size: 18px;
        margin: 10px;
        text-align: center;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
    }
    
    .movie-badge {
        background: linear-gradient(135deg, rgba(37, 99, 235, 0.2), rgba(30, 64, 175, 0.1));
        color: #60a5fa;
        border: 1px solid rgba(37, 99, 235, 0.3);
    }
    
    .tv-badge {
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.2), rgba(185, 28, 28, 0.1));
        color: #f87171;
        border: 1px solid rgba(239, 68, 68, 0.3);
    }
    
    /* FORM STYLING */
    .form-section {
        background: rgba(20, 20, 20, 0.6);
        border-radius: 16px;
        padding: 20px;
        margin: 15px 0;
        border: 1px solid rgba(245, 199, 122, 0.15);
    }
    
    /* INSIGHT CARDS */
    .insight-card {
        background: rgba(18, 18, 18, 0.7);
        border-radius: 16px;
        padding: 20px;
        margin: 10px 0;
        border: 1px solid rgba(245, 199, 122, 0.1);
        transition: all 0.3s ease;
    }
    
    .insight-card:hover {
        border-color: rgba(245, 199, 122, 0.3);
        transform: translateY(-3px);
        box-shadow: 0 10px 30px rgba(245, 199, 122, 0.15);
    }
    
    /* STATS CARDS */
    .stats-card {
        background: linear-gradient(135deg, rgba(30, 30, 30, 0.9), rgba(20, 20, 20, 0.9));
        border-radius: 16px;
        padding: 20px;
        border: 1px solid rgba(245, 199, 122, 0.2);
        text-align: center;
    }
    
    /* FOOTER */
    .footer {
        position: fixed;
        bottom: 20px;
        right: 30px;
        font-size: 12px;
        color: rgba(245, 199, 122, 0.6);
        letter-spacing: 1px;
        font-weight: 300;
    }
    
    /* TREND INDICATORS */
    .trend-indicator {
        display: inline-block;
        width: 12px;
        height: 12px;
        border-radius: 50%;
        margin-right: 10px;
    }
    
    .trend-up { background-color: #22c55e; }
    .trend-stable { background-color: #f59e0b; }
    .trend-down { background-color: #ef4444; }
    
    /* CHART STYLING OVERRIDES */
    .js-plotly-plot .plotly, .js-plotly-plot .plotly div {
        background-color: transparent !important;
    }
    </style>
    """, unsafe_allow_html=True)

apply_premium_theme()

# =============================
# LOAD AND PREPROCESS DATA
# =============================
@st.cache_data
def load_and_preprocess_data():
    try:
        df = pd.read_csv('data/netflix_cleaned.csv')
        
        # Create copy to avoid modification warnings
        df = df.copy()
        
        # Convert duration to numeric values
        def extract_duration(row):
            if pd.isna(row['duration']):
                return np.nan
            
            if row['type'] == 'Movie':
                # Extract minutes from "X min" format
                try:
                    match = str(row['duration']).split()[0]
                    return float(match) if match.isdigit() else np.nan
                except:
                    return np.nan
            elif row['type'] == 'TV Show':
                # Extract seasons from "X Season(s)" format
                try:
                    match = str(row['duration']).split()[0]
                    return float(match) if match.isdigit() else np.nan
                except:
                    return np.nan
            return np.nan
        
        # Apply duration extraction
        df['duration_numeric'] = df.apply(extract_duration, axis=1)
        
        # Ensure release_year is integer
        if 'release_year' in df.columns:
            df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce').fillna(0).astype(int)
        
        # Parse date_added for month analysis
        if 'date_added' in df.columns:
            df['date_added_parsed'] = pd.to_datetime(df['date_added'], errors='coerce')
            df['month_added'] = df['date_added_parsed'].dt.month
        
        # Extract primary genre
        if 'listed_in' in df.columns:
            df['primary_genre'] = df['listed_in'].str.split(',').str[0].str.strip()
        
        return df
    
    except FileNotFoundError:
        st.error("❌ Data file not found. Please ensure 'data/netflix_cleaned.csv' exists.")
        return pd.DataFrame()
    except Exception as e:
        st.error(f"❌ Error loading data: {str(e)}")
        return pd.DataFrame()

# Load data
df = load_and_preprocess_data()

# =============================
# SIDEBAR NAVIGATION
# =============================
st.sidebar.markdown("<h2 style='text-align: center;'>💎 StreamElite</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<div style='text-align: center; color: rgba(245, 199, 122, 0.7); margin-bottom: 30px;'>PREMIUM STREAMING ANALYTICS</div>", unsafe_allow_html=True)

page = st.sidebar.radio(
    "NAVIGATION",
    ["🏠 Dashboard", "📊 Content Overview", "🎭 Genre Intelligence", 
     "⏱️ Retention Analysis", "⏳ Duration Distribution", 
     "🌍 Global Trends", "📈 Raw Data"],
    label_visibility="collapsed"
)

st.sidebar.markdown("---")
st.sidebar.markdown("<div style='text-align: center; color: rgba(245, 199, 122, 0.7);'>👨‍💻 By Trymore Mhlanga</div>", unsafe_allow_html=True)

# =============================
# COLOR SCHEME DEFINITIONS
# =============================
# Different colors for Movies vs TV Shows
MOVIE_COLOR = '#F5C77A'  # Gold - for Movies
TV_COLOR = '#8B5A2B'     # Brown - for TV Shows (distinct from gold)
GENRE_COLOR_SCALE = 'YlOrBr'  # Valid Plotly color scale
MAP_COLOR_SCALE = 'Oranges'   # Valid Plotly color scale
HISTOGRAM_COLORS = ['#F5C77A', '#D4A94E']  # Gold variations

# =============================
# DASHBOARD PAGE
# =============================
if page == "🏠 Dashboard":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        st.markdown("<h1>STREAMELITE INTELLIGENCE</h1>", unsafe_allow_html=True)
        st.markdown("""
        <div style='color: rgba(245, 199, 122, 0.8); font-size: 18px; line-height: 1.6;'>
        Advanced streaming analytics platform revealing insights from Netflix's global content library. 
        Enterprise-grade analytics with interactive visualizations for content strategy optimization.
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        if not df.empty:
            total_titles = len(df)
            st.metric("Total Titles", f"{total_titles:,}")
        else:
            st.metric("Total Titles", "0")
    
    with col3:
        if not df.empty and 'release_year' in df.columns:
            latest_year = df['release_year'].max()
            st.metric("Latest Data", f"{int(latest_year)}")
        else:
            st.metric("Latest Data", "N/A")
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Key Metrics
    if not df.empty:
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            movies_count = len(df[df['type'] == 'Movie']) if 'type' in df.columns else 0
            st.metric("Movies", f"{movies_count:,}")
        
        with col2:
            tv_count = len(df[df['type'] == 'TV Show']) if 'type' in df.columns else 0
            st.metric("TV Shows", f"{tv_count:,}")
        
        with col3:
            if 'country' in df.columns:
                countries = df['country'].dropna().str.split(', ').explode().nunique()
                st.metric("Countries", f"{countries}")
            else:
                st.metric("Countries", "0")
        
        with col4:
            if 'listed_in' in df.columns:
                genres = df['listed_in'].dropna().str.split(', ').explode().nunique()
                st.metric("Genres", f"{genres}")
            else:
                st.metric("Genres", "0")
    
    # Features Grid
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h2>🔍 Explore Premium Insights</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<div class='insight-card'>", unsafe_allow_html=True)
        st.markdown("### 📊 Content Overview")
        st.markdown("""
        • Movies vs TV Shows distribution  
        • Monthly release patterns  
        • Yearly content trends  
        • Decade-wise analysis
        """)
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='insight-card'>", unsafe_allow_html=True)
        st.markdown("### 🎭 Genre Intelligence")
        st.markdown("""
        • Top genres across content types  
        • Genre popularity trends  
        • Interactive filtering  
        • Comparative analysis
        """)
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='insight-card'>", unsafe_allow_html=True)
        st.markdown("### ⏱️ Retention Analysis")
        st.markdown("""
        • Movie duration by genre  
        • TV show seasons analysis  
        • Engagement metrics  
        • Content longevity insights
        """)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='insight-card'>", unsafe_allow_html=True)
        st.markdown("### ⏳ Duration Distribution")
        st.markdown("""
        • Movie runtime patterns  
        • TV show season counts  
        • Content length trends  
        • Interactive histograms
        """)
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='insight-card'>", unsafe_allow_html=True)
        st.markdown("### 🌍 Global Trends")
        st.markdown("""
        • Country-wise contributions  
        • Choropleth world map  
        • Regional content analysis  
        • Production hotspots
        """)
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='insight-card'>", unsafe_allow_html=True)
        st.markdown("### 📈 Raw Data Explorer")
        st.markdown("""
        • Complete dataset access  
        • Interactive filtering  
        • CSV download  
        • Detailed metadata
        """)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Dataset Info
    st.markdown("<h3>📂 Dataset Information</h3>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div style='color: rgba(245, 199, 122, 0.9); line-height: 1.8;'>
        <strong>Source:</strong> Netflix Titles Dataset on Kaggle
        
        This comprehensive dataset contains detailed information about Netflix's global content library:
        
        • Content titles, descriptions, and metadata  
        • Release dates and production countries  
        • Genre classifications and duration data  
        • Cast and director information  
        • Content ratings and classifications
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='stats-card'>", unsafe_allow_html=True)
        st.markdown("##### 📊 Dataset Stats")
        if not df.empty:
            if 'country' in df.columns and 'listed_in' in df.columns:
                countries = df['country'].dropna().str.split(', ').explode().nunique()
                genres = df['listed_in'].dropna().str.split(', ').explode().nunique()
                years_range = df['release_year'].max() - df['release_year'].min() if 'release_year' in df.columns else 0
                
                st.markdown(f"""
                <div style='color: #f5c77a;'>
                • {len(df):,}+ titles analyzed  
                • {years_range}+ years  
                • {countries}+ countries  
                • {genres}+ genres
                </div>
                """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# =============================
# CONTENT OVERVIEW PAGE
# =============================
elif page == "📊 Content Overview":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h1>📊 CONTENT OVERVIEW ANALYTICS</h1>", unsafe_allow_html=True)
    
    if not df.empty and 'type' in df.columns and 'release_year' in df.columns:
        # Content Type Analysis
        st.markdown("<h3>📅 Content Type Distribution</h3>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([2, 1])
        
        with col2:
            st.markdown("<div class='form-section'>", unsafe_allow_html=True)
            years_available = sorted(df['release_year'].dropna().unique(), reverse=True)
            selected_year = st.selectbox("Select Release Year", years_available)
            st.markdown("</div>", unsafe_allow_html=True)
        
        with col1:
            filtered_df = df[df['release_year'] == selected_year]
            
            if not filtered_df.empty:
                type_counts = filtered_df['type'].value_counts()
                
                # Custom color sequence with distinct colors
                color_map = {'Movie': MOVIE_COLOR, 'TV Show': TV_COLOR}
                colors = [color_map.get(typ, '#808080') for typ in type_counts.index]
                
                fig = px.pie(
                    values=type_counts.values,
                    names=type_counts.index,
                    hole=0.5,
                    color=type_counts.index,
                    color_discrete_map=color_map
                )
                
                fig.update_traces(
                    textinfo='percent+label',
                    marker=dict(line=dict(color='#000000', width=2)),
                    textfont=dict(color='#f5c77a', size=14)
                )
                
                fig.update_layout(
                    title=f"Content Distribution in {selected_year}",
                    showlegend=True,
                    height=400,
                    margin=dict(t=50, b=0, l=0, r=0),
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    font=dict(color='#f5c77a'),
                    legend=dict(font=dict(color='#f5c77a'))
                )
                
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.warning(f"⚠️ No data available for {selected_year}")
        
        st.markdown("---")
        
        # Time-based Trends
        st.markdown("<h3>📈 Content Release Trends</h3>", unsafe_allow_html=True)
        
        # Monthly Trend
        if 'month_added' in df.columns:
            st.markdown("<h4>📅 Monthly Release Pattern</h4>", unsafe_allow_html=True)
            month_grouped = df.groupby(['month_added', 'type']).size().reset_index(name='count')
            month_grouped = month_grouped[month_grouped['month_added'] > 0]
            
            month_map = {
                1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
                7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
            }
            month_grouped['month'] = month_grouped['month_added'].map(month_map)
            
            fig_month = px.bar(
                month_grouped, 
                x='month', 
                y='count', 
                color='type',
                barmode='group',
                color_discrete_map={'Movie': MOVIE_COLOR, 'TV Show': TV_COLOR},
                category_orders={'month': list(month_map.values())}
            )
            fig_month.update_layout(
                title="Monthly Releases by Type",
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#f5c77a'),
                xaxis=dict(gridcolor='rgba(245, 199, 122, 0.1)'),
                yaxis=dict(gridcolor='rgba(245, 199, 122, 0.1)')
            )
            st.plotly_chart(fig_month, use_container_width=True)
        
        # Yearly Trend
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h4>📊 Yearly Release Trend</h4>", unsafe_allow_html=True)
            year_grouped = df.groupby(['release_year', 'type']).size().reset_index(name='count')
            year_grouped = year_grouped[year_grouped['release_year'] >= 2000]
            
            fig_year = px.line(
                year_grouped, 
                x='release_year', 
                y='count', 
                color='type',
                markers=True,
                color_discrete_map={'Movie': MOVIE_COLOR, 'TV Show': TV_COLOR}
            )
            fig_year.update_layout(
                title="Yearly Releases by Type",
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#f5c77a'),
                xaxis=dict(gridcolor='rgba(245, 199, 122, 0.1)'),
                yaxis=dict(gridcolor='rgba(245, 199, 122, 0.1)')
            )
            st.plotly_chart(fig_year, use_container_width=True)
        
        with col2:
            st.markdown("<h4>🕰️ Decade-wise Analysis</h4>", unsafe_allow_html=True)
            df['decade'] = (df['release_year'] // 10) * 10
            decade_grouped = df.groupby(['decade', 'type']).size().reset_index(name='count')
            
            fig_decade = px.bar(
                decade_grouped, 
                x='decade', 
                y='count', 
                color='type',
                barmode='group',
                color_discrete_map={'Movie': MOVIE_COLOR, 'TV Show': TV_COLOR}
            )
            fig_decade.update_layout(
                title="Content by Decade and Type",
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#f5c77a'),
                xaxis=dict(gridcolor='rgba(245, 199, 122, 0.1)'),
                yaxis=dict(gridcolor='rgba(245, 199, 122, 0.1)')
            )
            st.plotly_chart(fig_decade, use_container_width=True)
    
    else:
        st.error("❌ Required columns not available. Please check data structure.")
    
    st.markdown("</div>", unsafe_allow_html=True)

# =============================
# GENRE INTELLIGENCE PAGE
# =============================
elif page == "🎭 Genre Intelligence":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h1>🎭 GENRE INTELLIGENCE DASHBOARD</h1>", unsafe_allow_html=True)
    
    if not df.empty and 'type' in df.columns and 'primary_genre' in df.columns:
        # Sidebar filters
        st.sidebar.markdown("<h3 style='color: #f5c77a;'>⚙️ Filter Settings</h3>", unsafe_allow_html=True)
        
        with st.sidebar:
            content_type = st.selectbox(
                "Content Type",
                ["All", "Movie", "TV Show"]
            )
        
        # Filter data
        if content_type != "All":
            genre_data = df[df['type'] == content_type]
        else:
            genre_data = df
        
        genre_counts = genre_data['primary_genre'].value_counts().head(15).reset_index()
        genre_counts.columns = ['Genre', 'Count']
        
        # Horizontal Bar Chart - Fixed color scale
        fig_genre = px.bar(
            genre_counts.sort_values('Count'),
            x='Count', 
            y='Genre',
            orientation='h',
            color='Count',
            color_continuous_scale=GENRE_COLOR_SCALE,  # Valid Plotly color scale
            title=f"Top 15 Genres - {content_type}"
        )
        
        fig_genre.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#f5c77a'),
            xaxis=dict(gridcolor='rgba(245, 199, 122, 0.1)'),
            yaxis=dict(gridcolor='rgba(245, 199, 122, 0.1)')
        )
        
        st.plotly_chart(fig_genre, use_container_width=True)
        
        # Genre Statistics
        st.markdown("<div class='form-section'>", unsafe_allow_html=True)
        st.markdown("<h4>📊 Genre Statistics</h4>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            total_genres = genre_data['primary_genre'].nunique()
            st.metric("Unique Genres", total_genres)
        
        with col2:
            if len(genre_counts) > 0:
                top_genre = genre_counts.iloc[0]['Genre']
                top_count = genre_counts.iloc[0]['Count']
                st.metric("Top Genre", top_genre, delta=f"{top_count} titles")
            else:
                st.metric("Top Genre", "N/A")
        
        with col3:
            if len(genre_counts) > 0:
                avg_per_genre = genre_counts['Count'].mean()
                st.metric("Avg per Genre", f"{avg_per_genre:.0f}")
            else:
                st.metric("Avg per Genre", "0")
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Genre Distribution by Type
        if content_type == "All":
            st.markdown("<h4>🎬 Genre Distribution by Content Type</h4>", unsafe_allow_html=True)
            
            genre_by_type = df.groupby(['primary_genre', 'type']).size().unstack(fill_value=0)
            # Get top 10 genres overall
            top_genres = df['primary_genre'].value_counts().head(10).index
            genre_by_type = genre_by_type.loc[top_genres]
            
            fig_type = go.Figure()
            
            if 'Movie' in genre_by_type.columns:
                fig_type.add_trace(go.Bar(
                    name='Movies',
                    x=genre_by_type.index,
                    y=genre_by_type['Movie'],
                    marker_color=MOVIE_COLOR
                ))
            
            if 'TV Show' in genre_by_type.columns:
                fig_type.add_trace(go.Bar(
                    name='TV Shows',
                    x=genre_by_type.index,
                    y=genre_by_type['TV Show'],
                    marker_color=TV_COLOR
                ))
            
            fig_type.update_layout(
                barmode='group',
                title="Top 10 Genres by Content Type",
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#f5c77a'),
                xaxis=dict(gridcolor='rgba(245, 199, 122, 0.1)'),
                yaxis=dict(gridcolor='rgba(245, 199, 122, 0.1)'),
                legend=dict(font=dict(color='#f5c77a'))
            )
            
            st.plotly_chart(fig_type, use_container_width=True)
    
    else:
        st.error("❌ Required columns not available. Please check data structure.")
    
    st.markdown("</div>", unsafe_allow_html=True)

# =============================
# RETENTION ANALYSIS PAGE
# =============================
elif page == "⏱️ Retention Analysis":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h1>⏱️ CONTENT RETENTION ANALYTICS</h1>", unsafe_allow_html=True)
    
    if not df.empty and 'type' in df.columns and 'duration_numeric' in df.columns and 'primary_genre' in df.columns:
        st.markdown("<h3>🕒 Engagement Metrics by Genre</h3>", unsafe_allow_html=True)
        st.markdown("Analyze average durations to understand potential user engagement and retention patterns.")
        
        col1, col2 = st.columns(2)
        
        # Movie Durations by Genre
        with col1:
            st.markdown("<div class='insight-card'>", unsafe_allow_html=True)
            st.markdown("##### 🎥 Average Movie Duration")
            
            movie_df = df[df['type'] == 'Movie'].copy()
            # Remove NaN values
            movie_df = movie_df.dropna(subset=['duration_numeric', 'primary_genre'])
            
            if not movie_df.empty:
                avg_movie_duration = movie_df.groupby('primary_genre')['duration_numeric'].mean()
                avg_movie_duration = avg_movie_duration.sort_values(ascending=False).head(10)
                
                # Convert to DataFrame for plotting
                avg_movie_df = avg_movie_duration.reset_index()
                avg_movie_df.columns = ['Genre', 'Average Duration']
                
                fig_duration = px.bar(
                    avg_movie_df,
                    x='Average Duration',
                    y='Genre',
                    orientation='h',
                    color='Average Duration',
                    color_continuous_scale=GENRE_COLOR_SCALE,
                    labels={'Average Duration': 'Average Duration (minutes)'},
                    title="Top 10 Genres by Movie Length"
                )
                
                fig_duration.update_layout(
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    font=dict(color='#f5c77a'),
                    xaxis=dict(gridcolor='rgba(245, 199, 122, 0.1)'),
                    yaxis=dict(gridcolor='rgba(245, 199, 122, 0.1)')
                )
                
                st.plotly_chart(fig_duration, use_container_width=True)
                
                # Display stats
                if len(avg_movie_df) > 0:
                    avg_val = avg_movie_df['Average Duration'].mean()
                    median_val = avg_movie_df['Average Duration'].median()
                    st.metric("Average", f"{avg_val:.1f} min")
                    st.metric("Median", f"{median_val:.1f} min")
            else:
                st.warning("No movie data available for analysis.")
            
            st.markdown("</div>", unsafe_allow_html=True)
        
        # TV Show Seasons by Genre
        with col2:
            st.markdown("<div class='insight-card'>", unsafe_allow_html=True)
            st.markdown("##### 📺 Average TV Show Seasons")
            
            show_df = df[df['type'] == 'TV Show'].copy()
            # Remove NaN values
            show_df = show_df.dropna(subset=['duration_numeric', 'primary_genre'])
            
            if not show_df.empty:
                avg_seasons = show_df.groupby('primary_genre')['duration_numeric'].mean()
                avg_seasons = avg_seasons.sort_values(ascending=False).head(10)
                
                # Convert to DataFrame for plotting
                avg_seasons_df = avg_seasons.reset_index()
                avg_seasons_df.columns = ['Genre', 'Average Seasons']
                
                fig_seasons = px.bar(
                    avg_seasons_df,
                    x='Average Seasons',
                    y='Genre',
                    orientation='h',
                    color='Average Seasons',
                    color_continuous_scale=GENRE_COLOR_SCALE,
                    labels={'Average Seasons': 'Average Seasons'},
                    title="Top 10 Genres by Series Longevity"
                )
                
                fig_seasons.update_layout(
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    font=dict(color='#f5c77a'),
                    xaxis=dict(gridcolor='rgba(245, 199, 122, 0.1)'),
                    yaxis=dict(gridcolor='rgba(245, 199, 122, 0.1)')
                )
                
                st.plotly_chart(fig_seasons, use_container_width=True)
                
                # Display stats
                if len(avg_seasons_df) > 0:
                    avg_val = avg_seasons_df['Average Seasons'].mean()
                    median_val = avg_seasons_df['Average Seasons'].median()
                    st.metric("Average", f"{avg_val:.1f} seasons")
                    st.metric("Median", f"{median_val:.1f} seasons")
            else:
                st.warning("No TV show data available for analysis.")
            
            st.markdown("</div>", unsafe_allow_html=True)
        
        # Insights
        st.markdown("<div class='form-section'>", unsafe_allow_html=True)
        st.markdown("<h4>💡 Business Insights</h4>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **🎬 Movie Duration Insights:**
            • Longer movies may indicate higher production value  
            • Certain genres naturally have different length expectations  
            • Duration correlates with audience engagement time  
            • Impacts content scheduling and programming
            """)
        
        with col2:
            st.markdown("""
            **📺 TV Series Insights:**
            • More seasons indicate successful franchises  
            • Long-running shows build loyal audiences  
            • Impacts content acquisition strategy  
            • Influences original content development
            """)
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    else:
        st.error("❌ Required data not available. Please check data preprocessing.")
    
    st.markdown("</div>", unsafe_allow_html=True)

# =============================
# DURATION DISTRIBUTION PAGE
# =============================
elif page == "⏳ Duration Distribution":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h1>⏳ CONTENT DURATION ANALYSIS</h1>", unsafe_allow_html=True)
    
    if not df.empty and 'type' in df.columns and 'duration_numeric' in df.columns:
        st.markdown("<h3>📊 Content Length Distribution</h3>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<div class='insight-card'>", unsafe_allow_html=True)
            st.markdown("##### 🎥 Movie Runtime Distribution")
            
            movie_df = df[df['type'] == 'Movie'].copy()
            movie_df = movie_df.dropna(subset=['duration_numeric'])
            
            if not movie_df.empty:
                fig_movie = px.histogram(
                    movie_df,
                    x="duration_numeric",
                    nbins=30,
                    color_discrete_sequence=[MOVIE_COLOR]
                )
                
                fig_movie.update_layout(
                    title="Movie Duration Distribution",
                    xaxis_title="Duration (minutes)",
                    yaxis_title="Count",
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    font=dict(color='#f5c77a'),
                    xaxis=dict(gridcolor='rgba(245, 199, 122, 0.1)'),
                    yaxis=dict(gridcolor='rgba(245, 199, 122, 0.1)')
                )
                
                st.plotly_chart(fig_movie, use_container_width=True)
                
                # Movie stats - handle NaN values
                avg_movie = movie_df['duration_numeric'].mean()
                median_movie = movie_df['duration_numeric'].median()
                
                if not pd.isna(avg_movie):
                    st.metric("Average Duration", f"{avg_movie:.1f} min")
                else:
                    st.metric("Average Duration", "N/A")
                
                if not pd.isna(median_movie):
                    st.metric("Median Duration", f"{median_movie:.1f} min")
                else:
                    st.metric("Median Duration", "N/A")
            else:
                st.warning("No movie duration data available.")
            
            st.markdown("</div>", unsafe_allow_html=True)
        
        with col2:
            st.markdown("<div class='insight-card'>", unsafe_allow_html=True)
            st.markdown("##### 📺 TV Show Seasons Distribution")
            
            tv_df = df[df['type'] == 'TV Show'].copy()
            tv_df = tv_df.dropna(subset=['duration_numeric'])
            
            if not tv_df.empty:
                fig_tv = px.histogram(
                    tv_df,
                    x="duration_numeric",
                    nbins=15,
                    color_discrete_sequence=[TV_COLOR]
                )
                
                fig_tv.update_layout(
                    title="TV Show Seasons Distribution",
                    xaxis_title="Number of Seasons",
                    yaxis_title="Count",
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    font=dict(color='#f5c77a'),
                    xaxis=dict(gridcolor='rgba(245, 199, 122, 0.1)'),
                    yaxis=dict(gridcolor='rgba(245, 199, 122, 0.1)')
                )
                
                st.plotly_chart(fig_tv, use_container_width=True)
                
                # TV stats - handle NaN values
                avg_tv = tv_df['duration_numeric'].mean()
                median_tv = tv_df['duration_numeric'].median()
                
                if not pd.isna(avg_tv):
                    st.metric("Average Seasons", f"{avg_tv:.1f}")
                else:
                    st.metric("Average Seasons", "N/A")
                
                if not pd.isna(median_tv):
                    st.metric("Median Seasons", f"{median_tv:.1f}")
                else:
                    st.metric("Median Seasons", "N/A")
            else:
                st.warning("No TV show duration data available.")
            
            st.markdown("</div>", unsafe_allow_html=True)
        
        # Comparative Analysis
        if not df.empty:
            st.markdown("<div class='form-section'>", unsafe_allow_html=True)
            st.markdown("<h4>📈 Duration Statistics Summary</h4>", unsafe_allow_html=True)
            
            movie_stats = df[df['type'] == 'Movie']['duration_numeric'].describe()
            tv_stats = df[df['type'] == 'TV Show']['duration_numeric'].describe()
            
            stats_data = {
                'Metric': ['Mean', 'Median', 'Minimum', 'Maximum', 'Standard Deviation', 'Count'],
                'Movies': [
                    f"{movie_stats['mean']:.1f}" if not pd.isna(movie_stats['mean']) else "N/A",
                    f"{movie_stats['50%']:.1f}" if '50%' in movie_stats.index else "N/A",
                    f"{movie_stats['min']:.0f}" if not pd.isna(movie_stats['min']) else "N/A",
                    f"{movie_stats['max']:.0f}" if not pd.isna(movie_stats['max']) else "N/A",
                    f"{movie_stats['std']:.1f}" if not pd.isna(movie_stats['std']) else "N/A",
                    f"{int(movie_stats['count'])}" if not pd.isna(movie_stats['count']) else "0"
                ],
                'TV Shows': [
                    f"{tv_stats['mean']:.1f}" if not pd.isna(tv_stats['mean']) else "N/A",
                    f"{tv_stats['50%']:.1f}" if '50%' in tv_stats.index else "N/A",
                    f"{tv_stats['min']:.0f}" if not pd.isna(tv_stats['min']) else "N/A",
                    f"{tv_stats['max']:.0f}" if not pd.isna(tv_stats['max']) else "N/A",
                    f"{tv_stats['std']:.1f}" if not pd.isna(tv_stats['std']) else "N/A",
                    f"{int(tv_stats['count'])}" if not pd.isna(tv_stats['count']) else "0"
                ]
            }
            
            stats_df = pd.DataFrame(stats_data)
            st.dataframe(stats_df, use_container_width=True, hide_index=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
    
    else:
        st.error("❌ Duration data not available. Please check data preprocessing.")
    
    st.markdown("</div>", unsafe_allow_html=True)

# =============================
# GLOBAL TRENDS PAGE
# =============================
elif page == "🌍 Global Trends":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h1>🌍 GLOBAL CONTENT TRENDS</h1>", unsafe_allow_html=True)
    
    if not df.empty and 'country' in df.columns and 'release_year' in df.columns and 'type' in df.columns:
        # Filters
        st.markdown("<div class='form-section'>", unsafe_allow_html=True)
        st.markdown("<h4>⚙️ Filter Settings</h4>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            selected_type = st.selectbox(
                "Content Type",
                ["All", "Movie", "TV Show"],
                key="global_type"
            )
        
        with col2:
            min_year = int(df['release_year'].min())
            max_year = int(df['release_year'].max())
            year_range = st.slider(
                "Release Year Range",
                min_year, max_year,
                (2010, max_year)
            )
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Filter dataset
        filtered_df = df[
            (df['release_year'] >= year_range[0]) &
            (df['release_year'] <= year_range[1])
        ]
        
        if selected_type != "All":
            filtered_df = filtered_df[filtered_df['type'] == selected_type]
        
        # Count countries - handle NaN values
        if not filtered_df.empty and 'country' in filtered_df.columns:
            country_counts = (
                filtered_df['country']
                .dropna()
                .astype(str)
                .str.split(', ')
                .explode()
                .value_counts()
                .reset_index()
            )
            country_counts.columns = ['Country', 'Count']
        else:
            country_counts = pd.DataFrame(columns=['Country', 'Count'])
        
        # Metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Titles", len(filtered_df))
        
        with col2:
            st.metric("Countries", country_counts.shape[0])
        
        with col3:
            if len(country_counts) > 0:
                top_country = country_counts.iloc[0]['Country']
                st.metric("Top Country", top_country)
            else:
                st.metric("Top Country", "N/A")
        
        with col4:
            if len(country_counts) > 0:
                top_count = country_counts.iloc[0]['Count']
                st.metric("Top Count", top_count)
            else:
                st.metric("Top Count", "0")
        
        # Choropleth Map - Only if we have country data
        if len(country_counts) > 0:
            st.markdown("<h3>🌐 Global Contribution Map</h3>", unsafe_allow_html=True)
            
            fig_map = px.choropleth(
                country_counts,
                locations='Country',
                locationmode='country names',
                color='Count',
                color_continuous_scale=MAP_COLOR_SCALE,  # Valid Plotly color scale
                title=f"Content Production by Country ({selected_type})"
            )
            
            fig_map.update_geos(
                showcoastlines=True,
                coastlinecolor="rgba(245, 199, 122, 0.3)",
                showland=True,
                landcolor="rgba(30, 30, 30, 0.3)",
                showocean=True,
                oceancolor="rgba(10, 10, 10, 0.8)",
                showframe=False
            )
            
            fig_map.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#f5c77a'),
                coloraxis_colorbar=dict(
                    title="Count",
                    tickfont=dict(color='#f5c77a')
                )
            )
            
            st.plotly_chart(fig_map, use_container_width=True)
        else:
            st.warning("No country data available for the selected filters.")
        
        # Top Countries Bar Chart
        if len(country_counts) > 0:
            st.markdown("<h3>🏆 Top 15 Content Producing Countries</h3>", unsafe_allow_html=True)
            
            top_countries = country_counts.head(15)
            
            fig_bar = px.bar(
                top_countries,
                x='Count',
                y='Country',
                orientation='h',
                color='Count',
                color_continuous_scale=MAP_COLOR_SCALE
            )
            
            fig_bar.update_layout(
                yaxis={'categoryorder': 'total ascending'},
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#f5c77a'),
                xaxis=dict(gridcolor='rgba(245, 199, 122, 0.1)'),
                yaxis=dict(gridcolor='rgba(245, 199, 122, 0.1)')
            )
            
            st.plotly_chart(fig_bar, use_container_width=True)
        
        # Regional Analysis
        if len(country_counts) > 0:
            st.markdown("<div class='form-section'>", unsafe_allow_html=True)
            st.markdown("<h4>📈 Regional Analysis</h4>", unsafe_allow_html=True)
            
            # Group by continent/region (simplified)
            region_mapping = {
                'United States': 'North America',
                'India': 'Asia',
                'United Kingdom': 'Europe',
                'Canada': 'North America',
                'France': 'Europe',
                'Japan': 'Asia',
                'Spain': 'Europe',
                'South Korea': 'Asia',
                'Mexico': 'Latin America',
                'Australia': 'Oceania',
                'Germany': 'Europe',
                'Italy': 'Europe',
                'Brazil': 'Latin America',
                'China': 'Asia',
                'Russia': 'Europe'
            }
            
            country_counts['Region'] = country_counts['Country'].map(region_mapping)
            region_counts = country_counts.dropna(subset=['Region']).groupby('Region')['Count'].sum().reset_index()
            
            if not region_counts.empty:
                fig_pie = px.pie(
                    region_counts,
                    values='Count',
                    names='Region',
                    color_discrete_sequence=px.colors.sequential.Oranges
                )
                
                fig_pie.update_traces(
                    textinfo='percent+label',
                    marker=dict(line=dict(color='#000000', width=1))
                )
                
                fig_pie.update_layout(
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    font=dict(color='#f5c77a'),
                    showlegend=True
                )
                
                st.plotly_chart(fig_pie, use_container_width=True)
            else:
                st.info("Insufficient data for regional analysis.")
            
            st.markdown("</div>", unsafe_allow_html=True)
    
    else:
        st.error("❌ Required columns not available. Please check data structure.")
    
    st.markdown("</div>", unsafe_allow_html=True)

# =============================
# RAW DATA PAGE
# =============================
elif page == "📈 Raw Data":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h1>📈 RAW DATA EXPLORER</h1>", unsafe_allow_html=True)
    
    if not df.empty:
        st.markdown("<h3>📊 Complete Dataset</h3>", unsafe_allow_html=True)
        st.markdown("Explore the full Netflix dataset with interactive filtering and sorting.")
        
        # Dataset Information
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total Rows", len(df))
        
        with col2:
            st.metric("Total Columns", len(df.columns))
        
        with col3:
            st.metric("Memory Usage", f"{df.memory_usage(deep=True).sum() / 1024**2:.1f} MB")
        
        # Interactive Data Explorer
        st.markdown("<div class='form-section'>", unsafe_allow_html=True)
        st.markdown("<h4>🔍 Data Explorer</h4>", unsafe_allow_html=True)
        
        # Filters
        col1, col2, col3 = st.columns(3)
        
        with col1:
            content_filter = st.multiselect(
                "Filter by Content Type",
                df['type'].unique() if 'type' in df.columns else []
            )
        
        with col2:
            if 'release_year' in df.columns:
                year_filter = st.multiselect(
                    "Filter by Release Year",
                    sorted(df['release_year'].dropna().unique(), reverse=True)[:20]
                )
            else:
                year_filter = []
        
        with col3:
            if 'country' in df.columns:
                country_filter = st.multiselect(
                    "Filter by Country",
                    df['country'].dropna().astype(str).str.split(', ').explode().value_counts().head(20).index.tolist()
                )
            else:
                country_filter = []
        
        # Apply filters
        filtered_data = df.copy()
        
        if content_filter:
            filtered_data = filtered_data[filtered_data['type'].isin(content_filter)]
        
        if year_filter and 'release_year' in filtered_data.columns:
            filtered_data = filtered_data[filtered_data['release_year'].isin(year_filter)]
        
        if country_filter and 'country' in filtered_data.columns:
            # Create a regex pattern to match any of the selected countries
            pattern = '|'.join(country_filter)
            filtered_data = filtered_data[filtered_data['country'].astype(str).str.contains(pattern, na=False)]
        
        # Display data
        st.dataframe(
            filtered_data,
            use_container_width=True,
            height=500
        )
        
        st.markdown(f"**Showing {len(filtered_data)} of {len(df)} records**")
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Download Section
        st.markdown("<div class='form-section'>", unsafe_allow_html=True)
        st.markdown("<h4>💾 Data Export</h4>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 3])
        
        with col1:
            csv = filtered_data.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download Filtered CSV",
                data=csv,
                file_name='netflix_filtered_data.csv',
                mime='text/csv',
                use_container_width=True
            )
        
        with col2:
            st.info("💡 Download the filtered dataset for further analysis in Excel, Python, or other tools.")
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Data Schema
        st.markdown("<div class='form-section'>", unsafe_allow_html=True)
        st.markdown("<h4>📋 Data Schema</h4>", unsafe_allow_html=True)
        
        schema_data = []
        for col in df.columns:
            dtype = str(df[col].dtype)
            non_null = df[col].count()
            null_percent = (1 - non_null/len(df)) * 100 if len(df) > 0 else 100
            
            schema_data.append({
                'Column': col,
                'Data Type': dtype,
                'Non-Null Values': non_null,
                'Null %': f"{null_percent:.1f}%"
            })
        
        schema_df = pd.DataFrame(schema_data)
        st.dataframe(schema_df, use_container_width=True, hide_index=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    else:
        st.error("❌ No data available. Please load the dataset.")
    
    st.markdown("</div>", unsafe_allow_html=True)

# =============================
# FOOTER
# =============================
st.markdown(
    "<div class='footer'>StreamElite Analytics | Premium Streaming Intelligence © 2024</div>",
    unsafe_allow_html=True
)