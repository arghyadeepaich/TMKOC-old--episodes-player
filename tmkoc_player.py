import streamlit as st
import random

# --- 1. PAGE CONFIGURATION (Must be the first Streamlit command) ---
st.set_page_config(
    page_icon="👓",
    page_title="Retro TMKOC Streamer",
    layout="centered"
)

# --- 2. DATA LOADING ---
def load_links():
    """Loads and cleans links from the text file."""
    try:
        with open('episode_links.txt', 'r') as f:
            # Read lines and remove empty ones or non-links
            return [link.strip() for link in f.readlines() if link.strip().startswith("http")]
    except FileNotFoundError:
        st.error("Error: 'episode_links.txt' file not found. Please upload it.")
        return []

# Load the links once
episode_links = load_links()

# --- 3. HELPER FUNCTIONS ---
def get_video_id(url):
    """Extracts video ID from both youtube.com (v=) and youtu.be (short) URLs"""
    try:
        if "v=" in url:
            return url.split("v=")[1].split("&")[0]
        elif "youtu.be/" in url:
            return url.split("youtu.be/")[1].split("?")[0]
    except IndexError:
        return None
    return None

def embed_random_episode():
    """Selects a random episode and saves it to session state."""
    if episode_links:
        st.session_state.current_episode = random.choice(episode_links)
    else:
        st.warning("No links available to play.")

# --- 4. APP UI & LOGIC ---
st.title("Taarak Mehta Ka Ooltah Chashmah")
st.subheader("Random Old Episode Player")
st.write("Developed by Arghyadeep Aich")

# Initialize session state for the current episode if it doesn't exist
if 'current_episode' not in st.session_state:
    st.session_state.current_episode = None

# Button to pick a new episode
if st.button("Play a Random Episode"):
    embed_random_episode()

# Display the video ONLY if an episode is currently selected in session state
if st.session_state.current_episode:
    episode_url = st.session_state.current_episode
    video_id = get_video_id(episode_url)

    if video_id:
        embed_url = f"https://www.youtube.com/embed/{video_id}"
        
        # Custom HTML for responsive video embedding
        st.components.v1.html(f"""
            <style>
                .video-container {{
                    position: relative;
                    padding-bottom: 56.25%; /* 16:9 Aspect Ratio */
                    height: 0;
                    overflow: hidden;
                    border-radius: 10px;
                    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                }}
                .video-container iframe {{
                    position: absolute;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    border: 0;
                }}
                .fallback-link {{
                    display: block;
                    margin-top: 15px;
                    text-align: center;
                    font-family: sans-serif;
                    color: #FF0000;
                    text-decoration: none;
                    font-weight: bold;
                }}
            </style>
            
            <div class="video-container">
                <iframe src="{embed_url}" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            </div>
            
            <a class="fallback-link" href="{episode_url}" target="_blank">
                Video not playing? Click here to watch on YouTube.
            </a>
        """, height=400)
    else:
        st.error(f"Could not process URL: {episode_url}")
