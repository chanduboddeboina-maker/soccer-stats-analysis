

def load_css():
    return '''
    <style>
    
    .stApp {
        background-color: #0e1117;
        color: #f0f6fc;
        font-family: 'Segoe UI', sans-serif;
    }

    
    section[data-testid="stSidebar"] {
        background-color: #161b22;
        border-right: 2px solid #21262d;
        padding-top: 20px;
    }

    section[data-testid="stSidebar"] .stSelectbox label,
    section[data-testid="stSidebar"] .stRadio label {
        color: #8b949e;
        font-size: 13px;
        font-weight: 600;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }

  
    h1 {
        color: #58a6ff;
        font-size: 32px;
        font-weight: 700;
        padding-bottom: 4px;
        border-bottom: 2px solid #21262d;
        margin-bottom: 16px;
    }

    
    h2, h3 {
        color: #f0f6fc;
        font-weight: 600;
        border-bottom: 1px solid #21262d;
        padding-bottom: 6px;
        margin-top: 8px;
    }

  
    [data-testid="stMetricValue"] {
        font-size: 30px;
        font-weight: 700;
        color: #58a6ff;
    }

    [data-testid="stMetricLabel"] {
        font-size: 12px;
        font-weight: 600;
        color: #8b949e;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

   
    [data-testid="stMetric"] {
        background-color: #161b22;
        border: 1px solid #21262d;
        border-radius: 10px;
        padding: 16px 20px;
        margin: 4px 0;
    }

   
    hr {
        border: none;
        border-top: 1px solid #21262d;
        margin: 16px 0;
    }

    
    .stSelectbox > div > div,
    .stRadio > div {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 8px;
        color: #f0f6fc;
    }

    
    .stSpinner > div {
        color: #58a6ff;
        font-size: 14px;
    }

   
    [data-testid="stAlert"] {
        background-color: #161b22;
        border-left: 4px solid #f85149;
        border-radius: 6px;
        color: #f0f6fc;
    }

   
    [data-testid="stPyplotFigure"] {
        background-color: #0e1117;
        border: 1px solid #21262d;
        border-radius: 12px;
        padding: 8px;
    }

    
    .stMarkdown p {
        color: #8b949e;
        font-size: 13px;
    }

    
    .stSidebar h1,
    .stSidebar h2,
    .stSidebar h3 {
        color: #58a6ff;
        border-bottom: 1px solid #21262d;
    }
    </style>
    '''