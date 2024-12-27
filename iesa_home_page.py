import streamlit as st
import base64

# Function to convert an image to Base64
def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    return f"data:image/png;base64,{encoded_image}"

# Local image path (Replace with your actual image path)
image_path = "IESA_logo.png"

# CSS and JavaScript for dynamic button states
st.markdown("""
    <style>
    /* General Styling */
    header {
        border-bottom: 3px solid  #136a8a !important; 
    }
    [data-testid="stSidebar"] {
        background: linear-gradient(135deg, #73C8A9, #0b8793); /* Gradient background */
        color: white;
        margin-top:58px;
    }
    .sidebar-content {
        margin-top: -60px;
        padding: 20px;
    }
    .logo-title-container {
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: space-between;
        }
    .logo img {
        width: 60px;
        border-radius: 50%;
    }
    .app-name {
        font-size: 1.5em;
        font-weight: bold;
    }
    
    .top-bar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-top: -10px;
    }
   
    /* Apply styles specifically to buttons inside nav-links */
    .nav-links > button {
        background-color: transparent;
        border: none;
        font-size: 1em;
        font-weight: 500;
        cursor: pointer;
        margin: 0 5px;
        border-bottom: 2px solid transparent;
        transition: all 0.3s ease;
    }
    .nav-links > button.active {
        border-bottom: 2px solid red; /* Persistent red border for active button */
    }
    .nav-links > button:hover {
        border-bottom: 2px solid green; /* Green border on hover */
    }
    .nav-links a {
        text-decoration: none;
        color: #0F403F;
    }
    .auth-buttons {
        display: flex;
        gap: 10px;
    }
    .auth-buttons button {
        background-color: transparent;
        border: 1px solid #0F403F;
        border-radius: 20px;
        color: #0F403F;
        font-size: 0.9em;
        font-weight: bold;
        padding: 6px 20px;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .auth-buttons button:hover {
        background-color: #0F403F;
        color: white;
    }
    .auth-buttons .contactus {
         background-color: #0F403F;
        color: white;
        
        }
    </style>

    <script>
    // JavaScript to dynamically update active button
    document.addEventListener('DOMContentLoaded', function () {
        const navButtons = document.querySelectorAll('.nav-links button');
        navButtons.forEach(button => {
            button.addEventListener('click', function () {
                navButtons.forEach(btn => btn.classList.remove('active'));
                this.classList.add('active');
            });
        });
    });
    </script>
""", unsafe_allow_html=True)
# Sidebar Content
with st.sidebar:
    
    st.markdown(
        f"""
        <div class="sidebar-content">
            <div class="logo-title-container">
                <div class="logo">
                    <img src="{image_to_base64(image_path)}" alt="IESA Logo">
                </div>
                <div class="app-name">IESA Dashboard</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Top Bar Content
st.markdown(
    """
    <div class="top-bar">
        <div class="nav-links">
            <button class="active"><a href="#home">Home</a></button>
            <button><a href="#scenarios">Scenarios</a></button>
            <button><a href="#predictions">Predictions</a></button>
            <button><a href="#report">Report</a></button>
            <button><a href="#recommendations">Recommendations</a></button>    
        </div>
        <div class="auth-buttons">
            <button class="logout">Logout</button>
            <button class="contactus">Contact Us</button>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
