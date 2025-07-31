import streamlit as st

# Page configuration
st.set_page_config(
    page_title="CognitiveCloud.ai Math Apps",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #1f77b4;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .sub-header {
        text-align: center;
        color: #666;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    .app-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 0.5rem;
        text-align: center;
        color: white;
        text-decoration: none;
        transition: transform 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    .app-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.2);
    }
    .app-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    .app-title {
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .app-description {
        font-size: 0.9rem;
        opacity: 0.9;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🧠 CognitiveCloud.ai App Launcher</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Explore Xavier Honablue\'s interactive math apps - Choose your mathematical adventure!</p>', unsafe_allow_html=True)

# App data with correct working URLs
apps = [
    {
        "name": "📐 Algebra Rules",
        "description": "Master algebraic concepts and rules",
        "url": "https://mathcraft-algebrarules1.streamlit.app/",
        "icon": "📐",
        "color": "#FF6B6B"
    },
    {
        "name": "📊 Calculus",
        "description": "Explore derivatives, integrals, and limits",
        "url": "https://calculus.streamlit.app/",
        "icon": "📊",
        "color": "#4ECDC4"
    },
    {
        "name": "🔴 Conic Sections",
        "description": "Visualize circles, ellipses, parabolas & hyperbolas",
        "url": "https://mathcraft-conicsections.streamlit.app/",
        "icon": "🔴",
        "color": "#45B7D1"
    },
    {
        "name": "🔢 Discrete Structures",
        "description": "Logic, sets, and combinatorics",
        "url": "https://mathcraft-discretestructures.streamlit.app/",
        "icon": "🔢",
        "color": "#96CEB4"
    },
    {
        "name": "📈 Distribution Curves",
        "description": "Statistical distributions and probability",
        "url": "https://algebra1rules-q94clpmtxy8hzwvxs6jxwx.streamlit.app/",
        "icon": "📈",
        "color": "#FFEAA7"
    },
    {
        "name": "🌀 Spiral Vision: Fibonacci & Golden Ratio",
        "description": "Discover nature's secret mathematical spiral patterns",
        "url": "https://fibonacci-ratio.streamlit.app/",
        "icon": "🌀",
        "color": "#E17055"
    },
    {
        "name": "🎯 Vision: See the Distribution",
        "description": "Explore normal distributions, real-world data, and global impact",
        "url": "https://vision-distribution.streamlit.app/",
        "icon": "🎯",
        "color": "#FAD02C"
    },
    {
        "name": "🍕 Fractions (Pizza Cutter)",
        "description": "Learn fractions with interactive pizza slices",
        "url": "https://pizza-math.streamlit.app/",
        "icon": "🍕",
        "color": "#DDA0DD"
    },
    {
        "name": "⚡ Irrational Numbers",
        "description": "Explore pi, e, and other irrational numbers",
        "url": "https://mathcraft-irrationalnumbers.streamlit.app/",
        "icon": "⚡",
        "color": "#F7DC6F"
    },
    {
        "name": "🎯 Trigonometry",
        "description": "Sine, cosine, tangent, and more",
        "url": "https://mathcraft-trigonometry.streamlit.app/",
        "icon": "🎯",
        "color": "#BB8FCE"
    },
    {
        "name": "🔄 Particle Motion",
        "description": "Physics and motion visualizations",
        "url": "https://mathcraft-particlemotion.streamlit.app/",
        "icon": "🔄",
        "color": "#85C1E9"
    },
    {
        "name": "📊 Polynomial Zeros",
        "description": "Explore polynomial functions and find their zeros/roots",
        "url": "https://mathcraft-twistedcurves.streamlit.app/",
        "icon": "📊",
        "color": "#F8C471"
    },
    {
        "name": "✏️ Pencil Dashboard",
        "description": "4th grade math lesson with surface area",
        "url": "https://pencil-dashboard.streamlit.app/",
        "icon": "✏️",
        "color": "#82E0AA"
    },
    {
        "name": "🔺 Tessellations",
        "description": "Geometric pattern exploration",
        "url": "https://mathcraft-tesselations.streamlit.app/",
        "icon": "🔺",
        "color": "#D7BDE2"
    },
    {
        "name": "🚂 Train Motion",
        "description": "Algebra with motion problems",
        "url": "https://mathcraft-trainmotion.streamlit.app/",
        "icon": "🚂",
        "color": "#F9E79F"
    },
    {
        "name": "🧲 Magnetism & Math",
        "description": "Explore magnetic fields, equations, and math connections",
        "url": "https://mathofmagnetism.streamlit.app/",
        "icon": "🧲",
        "color": "#00B894"
    }
]

# Create a grid layout
cols_per_row = 3
rows = [apps[i:i + cols_per_row] for i in range(0, len(apps), cols_per_row)]

for row in rows:
    cols = st.columns(len(row))
    for col, app in zip(cols, row):
        with col:
            st.markdown(f"""
            <div style="
                background: linear-gradient(135deg, {app['color']}22 0%, {app['color']}44 100%);
                border: 2px solid {app['color']};
                padding: 1.5rem;
                border-radius: 15px;
                text-align: center;
                margin: 0.5rem 0;
                transition: all 0.3s ease;
            ">
                <div style="font-size: 3rem; margin-bottom: 1rem;">{app['icon']}</div>
                <h3 style="color: #333; margin-bottom: 0.5rem;">{app['name'].split(' ', 1)[1]}</h3>
                <p style="color: #666; font-size: 0.9rem; margin-bottom: 1rem;">{app['description']}</p>
                <a href="{app['url']}" target="_blank" style="
                    background: {app['color']};
                    color: white;
                    padding: 0.75rem 1.5rem;
                    border-radius: 25px;
                    text-decoration: none;
                    font-weight: bold;
                    transition: all 0.3s ease;
                    display: inline-block;
                ">Launch App</a>
            </div>
            """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; margin-top: 2rem; color: #666;">
    <p>💡 <strong>Empowering Young Minds in STEAM</strong></p>
    <p>Innovative learning solutions for grades 4-12 | Created by Xavier Honablue</p>
</div>
""", unsafe_allow_html=True)

# Optional: Add a quick stats section
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("🎯 Total Apps", len(apps))
with col2:
    st.metric("👥 Grade Levels", "4-12")
with col3:
    st.metric("📚 Subject Areas", "13+")
