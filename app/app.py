import streamlit as st
import pandas as pd
import plotly.express as px


# -------------------------
# Page Config
# -------------------------
st.set_page_config(
    page_title="Streaming Dashboard",
    page_icon="🎬",
    layout="wide"
)

# -------------------------
# Load Data
# -------------------------
@st.cache_data
def load_data():
    return pd.read_csv('data/netflix_cleaned.csv')

df = load_data()

# -------------------------
# Sidebar Navigation
# -------------------------
st.markdown("""
        <style>
        /* Sidebar background color */
        [data-testid="stSidebar"] {
            background-color: #2c445c;
        }

        /* Sidebar title and radio button text */
        [data-testid="stSidebar"] h1, [data-testid="stSidebar"] label {
            color: white;
        }

        /* Sidebar footer text */
        .sidebar .markdown-text-container {
            color: #6e6e6e;
        }

        </style>
    """, unsafe_allow_html=True)
st.sidebar.title("📊 Navigation")
section = st.sidebar.radio(
    "📍 Navigate",
    [
        "Home",
        "Content Overview",
        "Genre Insights",
        "Retention Analysis",
        "Duration Distribution",
        "Country Trends",
        "Raw Data"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("👩‍💻 *By Sanaj Jadhav*")

# -------------------------
# Section: Home
# -------------------------
if section == "Home":
    # Custom CSS for modern styling
    st.markdown("""
    <style>
    /* Override Streamlit's default dark theme text colors */
    .main-header {
        background: #2c445c;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        color: white !important;
        margin-bottom: 2rem;
    }
    
    .feature-card {
        background: rgba(255, 255, 255, 0.95) !important;
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 7px solid #6f9eb6;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        margin-bottom: 1rem;
        transition: transform 0.3s ease;
        color: #1f2937 !important;
    }
    
    .feature-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(37, 99, 235, 0.3);
    }
    
    .feature-card h4 {
        color: #1f2937 !important;
        margin-bottom: 0.5rem;
    }
    
    .feature-card p {
        color: #374151 !important;
        margin: 0;
    }
    
    .stats-container {
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem 0;
        color: #ffffff !important;
    }
    
    .stats-container h3 {
        color: #ffffff !important;
    }
    
    .stats-container p {
        color: #ffffff !important;
    }
    
    .tech-badge {
        display: inline-block;
        background: #2c445c !important;
        color: white !important;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        margin: 0.2rem;
        font-weight: 500;
    }
    
    .profile-section {
        background: rgba(255, 255, 255, 0.95) !important;
        border: 1px solid #e2e8f0;
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem 0;
        color: #1f2937 !important;
    }
    
    .profile-section h3 {
        color: #1f2937 !important;
    }
    
    .profile-section p {
        color: #374151 !important;
    }
    
    .profile-section ul {
        color: #374151 !important;
    }
    
    .profile-section li {
        color: #374151 !important;
    }
    
    .social-links {
        display: flex;
        gap: 1rem;
        margin-top: 1rem;
    }
    
    .social-btn {
        background: #2c445c !important;
        color: white !important;
        padding: 0.5rem 1rem;
        border-radius: 25px;
        text-decoration: none;
        font-weight: 500;
        transition: all 0.3s ease;
        margin-bottom: 0.5rem;
    }
    
    .social-btn:hover {
        background: #1e40af !important;
        transform: translateY(-1px);
        text-decoration: none;
        color: white !important;
    }
    
    /* Force light text on dark backgrounds */
    .light-text {
        color: #f8fafc !important;
    }
    
    .light-text h2 {
        color: #f8fafc !important;
    }
    
    .light-text p {
        color: #e2e8f0 !important;
    }
    
    .dataset-info {
        color: #f8fafc !important;
    }
    
    .dataset-info a {
        color: #60a5fa !important;
    }
    
    .dataset-info ul {
        color: #e2e8f0 !important;
    }
    
    .dataset-info li {
        color: #e2e8f0 !important;
    }
    
    .footer-text {
        color: #cbd5e1 !important;
    }
    
    .footer-text strong {
        color: #f8fafc !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Main Header
    st.markdown("""
    <div class="main-header">
        <h1>🎬 Streaming Service Insights</h1>
        <p style="font-size: 1.2rem; margin-top: 1rem; opacity: 0.9;">
            Discover trends, patterns, and insights from Netflix's global content library
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Welcome Section
    st.markdown("""
    <div class="light-text" style="text-align: center; margin: 2rem 0;">
        <h2 style="color: #f8fafc !important; margin-bottom: 1rem;">Welcome to Your Data Journey</h2>
        <p style="font-size: 1.1rem; color: #e2e8f0 !important; max-width: 800px; margin: 0 auto;">
            Dive deep into Netflix's content ecosystem with interactive visualizations and comprehensive analytics. 
            Uncover hidden patterns in streaming entertainment data.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Features Grid
    st.markdown('<h2 style="color: #f8fafc !important;">🔍 Explore These Insights</h2>', unsafe_allow_html=True)
    st.markdown('<p style="color: #e2e8f0 !important; margin-bottom: 1.5rem;">Click on any feature to learn more about what insights you can discover.</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h4>📊 Content Overview</h4>
            <p>Visualize how Netflix’s content library has evolved with an interactive donut chart showing the balance between Movies and TV Shows, along with release trends across months, years, and decades.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h4>🎭 Genre Intelligence</h4>
            <p>Analyze the most popular genres and their trends over time. Filter by content type to see how genre preferences vary between Movies and TV Shows.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h4>⏱️ Retention Analysis by Genre</h4>
            <p>Compare average movie durations and TV show seasons by genre to understand which genres may retain users longer.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h4>⏳ Duration Distribution</h4>
            <p>Understand how long Netflix content typically is with interactive histograms showing the distribution of movie runtimes and TV show season counts.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h4>🌍 Country-Wise Contribution</h4>
            <p>Explore which countries contribute the most to Netflix’s content library using bar charts and a global choropleth map, highlighting regional strengths in content production.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h4>📊 Raw Data Exploration</h4>
            <p>Access the raw Netflix dataset used for analysis. Download the CSV file to explore the data in your own tools.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Navigation Info
    st.markdown("""
    <div class="stats-container">
        <h3 style="text-align: center; margin-bottom: 1rem;">🧭 Navigation Guide</h3>
        <p style="text-align: center; font-size: 1.1rem;">
            Use the <strong>📊 Navigation</strong> sidebar to explore each analytical section. 
            Each page offers interactive filters and detailed visualizations.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Dataset Info
    st.markdown('<h2 style="color: #f8fafc !important;">📂 Dataset Information</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="dataset-info">
        <strong>Source</strong>: <a href="https://www.kaggle.com/datasets/shivamb/netflix-shows" style="color: #60a5fa !important;">Netflix Titles Dataset on Kaggle</a>
        
        <p style="color: #e2e8f0 !important; margin-top: 1rem;">
        This comprehensive dataset contains detailed information about Netflix's content library including:
        </p>
        <ul style="color: #e2e8f0 !important;">
            <li>Content titles, descriptions, and metadata</li>
            <li>Release dates and production countries</li>
            <li>Genre classifications and duration data</li>
            <li>Cast and director information</li>
            <li>Content ratings and classifications</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.info("""
        📊 **Dataset Stats**
        - 8,000+ titles analyzed
        - 10+ years of data
        - 200+ countries covered
        - 20+ genres tracked
        """)
    

# -------------------------
# Section: Content Overview
# -------------------------
elif section == "Content Overview":
    st.header("📅 Content Overview")
    st.markdown("Explore how Netflix content types and release patterns have changed over time.")

    st.subheader("Content Type Analysis")

    # Filter by Year
    years_sorted = sorted(df['release_year'].dropna().unique(), reverse=True)
    selected_year = st.selectbox("Filter by Release Year", years_sorted)

    filtered_df = df[df['release_year'] == selected_year]

    if not filtered_df.empty:
        type_counts = filtered_df['type'].value_counts()

        fig = px.pie(
            names=type_counts.index,
            values=type_counts.values,
            hole=0.5,
            color_discrete_sequence=['#4e79a7', '#f28e2b']
        )
        fig.update_traces(
            textinfo='percent+label',
            marker=dict(line=dict(color='#FFFFFF', width=2))
        )
        fig.update_layout(
            title=f"Distribution in {selected_year}",
            showlegend=False,
            height=400,
            margin=dict(t=50, b=0, l=0, r=0)
        )

        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning(f"No data available for {selected_year}.")
    
    st.markdown("---")
    import plotly.express as px

    st.markdown("## Content Over Time")
    st.markdown("How Netflix’s content output has changed over time by format.")

    # --- Monthly Trend ---
    st.subheader(" Monthly Release Trend (by Type)")
    df['month_added'] = pd.to_datetime(df['date_added'], errors='coerce').dt.month
    month_grouped = df.groupby(['month_added', 'type']).size().reset_index(name='count')
    month_grouped['month_added'] = month_grouped['month_added'].fillna(0).astype(int)

    # Map month number to names
    month_map = {
        1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
        7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
    }
    month_grouped['month'] = month_grouped['month_added'].map(month_map)
    month_grouped = month_grouped.sort_values(by='month_added')

    fig_month = px.bar(
        month_grouped, x='month', y='count', color='type',
        barmode='group', title="Monthly Releases by Type"
    )
    st.plotly_chart(fig_month, use_container_width=True)

    # --- Yearly Trend ---
    st.subheader(" Yearly Release Trend (by Type)")
    year_grouped = df.groupby(['release_year', 'type']).size().reset_index(name='count')
    year_grouped = year_grouped[year_grouped['release_year'] >= 2000]  # Clean early noisy years

    fig_year = px.line(
        year_grouped, x='release_year', y='count', color='type',
        markers=True, title="Yearly Releases by Type"
    )
    st.plotly_chart(fig_year, use_container_width=True)

    # --- Decade-wise Trend ---
    st.subheader(" Decade-wise Release Trend")
    df['decade'] = (df['release_year'] // 10) * 10
    decade_grouped = df.groupby(['decade', 'type']).size().reset_index(name='count')

    fig_decade = px.bar(
        decade_grouped, x='decade', y='count', color='type',
        barmode='group', title="Content by Decade and Type"
    )
    st.plotly_chart(fig_decade, use_container_width=True)


# -------------------------
# Section: Genre Insights
# -------------------------
elif section == "Genre Insights":
    st.header("🎭 Genre Patterns")
    st.markdown("Explore the most frequent genres across Netflix content. You can filter by type (Movie/TV Show).")

    content_type = st.selectbox("Select Content Type", ["All", "Movie", "TV Show"])

    # --- Preprocess Genre Column ---
    df['genre'] = df['listed_in'].str.split(',').str[0].str.strip()

    if content_type != "All":
        genre_data = df[df['type'] == content_type]
    else:
        genre_data = df

    genre_counts = genre_data['genre'].value_counts().head(15).reset_index()
    genre_counts.columns = ['Genre', 'Count']

    # --- Horizontal Bar Chart ---
    fig_genre = px.bar(
        genre_counts.sort_values('Count'),
        x='Count', y='Genre',
        orientation='h',
        color='Count',
        color_continuous_scale='plasma',
        title=f"Top 15 Genres ({content_type})"
    )

    st.plotly_chart(fig_genre, use_container_width=True)


# -------------------------
# Section: Retention Analysis
# -------------------------
elif section == "Retention Analysis":
    st.subheader("🕒 Retention Proxies by Genre")
    st.markdown("Compare average **movie durations** and **TV show seasons** by genre to understand which genres may retain users longer.")

    col1, col2 = st.columns(2)

    # --- Movie Durations by Genre ---
    with col1:
        st.markdown("**🎥 Average Movie Duration (mins)**")
        movie_df = df[df['type'] == 'Movie'].copy()
        movie_df['genre'] = movie_df['listed_in'].str.split(',').str[0].str.strip()
        movie_df['duration'] = movie_df['duration'].str.extract('(\d+)').astype(float)

        avg_movie_duration = movie_df.groupby('genre')['duration'].mean().sort_values(ascending=False).head(10)
        fig_duration = px.bar(
            avg_movie_duration,
            x=avg_movie_duration.values,
            y=avg_movie_duration.index,
            orientation='h',
            color=avg_movie_duration.values,
            color_continuous_scale='burg',
            labels={'x': 'Average Duration (mins)', 'y': 'Genre'},
            title="Top 10 Genres by Movie Duration"
        )
        st.plotly_chart(fig_duration, use_container_width=True)
        

    # --- TV Show Seasons by Genre ---
    with col2:
        st.markdown("**📺 Average TV Show (seasons)**")
        show_df = df[df['type'] == 'TV Show'].copy()
        show_df['genre'] = show_df['listed_in'].str.split(',').str[0].str.strip()
        show_df['seasons'] = show_df['duration'].str.extract('(\d+)').astype(float)

        avg_seasons = show_df.groupby('genre')['seasons'].mean().sort_values(ascending=False).head(10)
        fig_seasons = px.bar(
            avg_seasons,
            x=avg_seasons.values,
            y=avg_seasons.index,
            orientation='h',
            color=avg_seasons.values,
            color_continuous_scale='burg',
            labels={'x': 'Average Seasons', 'y': 'Genre'},
            title="Top 10 Genres by TV Show Seasons"
        )
        st.plotly_chart(fig_seasons, use_container_width=True)

    st.markdown("This analysis helps identify which genres may have longer content, potentially leading to higher user retention. For example, genres with longer average movie durations or more seasons in TV shows might indicate deeper engagement.")


# -------------------------
# Section: Duration Distribution
# -------------------------
elif section == "Duration Distribution":
    st.header("⏱️ Duration Distribution")
    st.markdown("Explore how long Netflix content typically is.")

    # Filter data
    movie_df = df[df['type'] == 'Movie']
    tv_df = df[df['type'] == 'TV Show']

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🎥 Movie Durations (minutes)")
        fig_movie = px.histogram(
            movie_df,
            x="duration_int",
            nbins=30,
            title="Movie Duration Distribution",
            color_discrete_sequence=['indianred']
        )
        fig_movie.update_layout(xaxis_title="Minutes", yaxis_title="Count")
        st.plotly_chart(fig_movie, use_container_width=True)

    with col2:
        st.subheader("📺 TV Show (seasons)")
        fig_tv = px.histogram(
            tv_df,
            x="duration_int",
            nbins=15,
            title="TV Show Seasons Distribution",
            color_discrete_sequence=['darkblue']
        )
        fig_tv.update_layout(xaxis_title="Seasons", yaxis_title="Count")
        st.plotly_chart(fig_tv, use_container_width=True)

# -------------------------
# Section: Country Trends
# -------------------------
elif section == "Country Trends":
    st.header("🌍 Country-Wise Contribution")
    st.markdown("Explore which countries produce the most Netflix content. Use the filters below:")

    # 🎛️ Filters (inside main page)
    col1, col2 = st.columns(2)
    with col1:
        selected_type = st.selectbox("Select Content Type", ["All", "Movie", "TV Show"])
    with col2:
        min_year, max_year = int(df['release_year'].min()), int(df['release_year'].max())
        year_range = st.slider("Select Release Year Range", min_year, max_year, (min_year, max_year))

    # Filter dataset
    filtered_df = df[
        (df['release_year'] >= year_range[0]) &
        (df['release_year'] <= year_range[1])
    ]
    if selected_type != "All":
        filtered_df = filtered_df[filtered_df['type'] == selected_type]

    # Count countries
    country_counts = (
        filtered_df['country']
        .dropna()
        .str.split(', ')
        .explode()
        .value_counts()
        .reset_index()
    )
    country_counts.columns = ['Country', 'Count']

    st.info(f"Showing results for **{selected_type}** content from **{year_range[0]} to {year_range[1]}** ({len(filtered_df)} titles).")

    # 🌍 Choropleth Map
    st.subheader("Global Contribution Map")
    fig_map = px.choropleth(
        country_counts,
        locations='Country',
        locationmode='country names',
        color='Count',
        color_continuous_scale='sunset',
        title=""
    )
    fig_map.update_geos(showcoastlines=False, showframe=False)
    st.plotly_chart(fig_map, use_container_width=True)

    # 📊 Bar Chart
    st.subheader("Top 15 Content Producing Countries")
    fig_bar = px.bar(
        country_counts.head(15),
        x='Count',
        y='Country',
        orientation='h',
        color='Count',
        color_continuous_scale='oxy'
    )
    fig_bar.update_layout(yaxis={'categoryorder': 'total ascending'})
    st.plotly_chart(fig_bar, use_container_width=True)

# -------------------------
# Section: Raw Data
# -------------------------
elif section == "Raw Data":
    st.header("📊 Raw Data")
    st.markdown("Explore the raw Netflix dataset used for analysis.")

    # Display raw data
    st.dataframe(df, use_container_width=True)

    # Download button
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name='netflix_data.csv',
        mime='text/csv'
    )