
import streamlit as st
import random

# Load episode links from file
with open('episode_links.txt', 'r') as f:
    episode_links = f.readlines()
    episode_links = [link.strip() for link in episode_links]

# Function to embed a random episode
def embed_random_episode():
    episode_number = random.randint(0, len(episode_links) - 1)
    episode_url = episode_links[episode_number]
    
    # Extract the video ID from the YouTube URL
    video_id = episode_url.split('v=')[-1]
    embed_url = f"https://www.youtube.com/embed/{video_id}"
    
    # Responsive embedding with a fallback link
    
    st.components.v1.html(f"""
        <style>
            .responsive-iframe {{
                position: relative;
                width: 100%;
                height: 0;
                padding-bottom: 56.25%;
            }}
            .responsive-iframe iframe {{
                position: absolute;
                width: 100%;
                height: 100%;
                left: 0;
                top: 0;
                border: 0;
            }}
            .responsive-text {{
                font-size: 20px;
                color: red;
                text-align: center;
                font-weight: bold;
            }}
            @media only screen and (max-width: 600px) {{
                .responsive-text {{
                    font-size: 16px;
                }}
            }}
        </style>
        <div class="responsive-iframe">
            <iframe src="{embed_url}" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </div>
        <p class="responsive-text">
            If the video shows unavailable, <a href="{episode_url}" target="_blank">click here to watch the episode on YouTube</a>.
        </p>
    """, height=500)

# Streamlit app layout
st.set_page_config(
    page_icon="👓",
    page_title="Retro TMKOC Streamer",
)
st.title("Taarak Mehta Ka Ooltah Chashmah - Random Old Episode Player")
st.write("Developed by Arghyadeep Aich")

if st.button("Play a Random Episode"):
    embed_random_episode()
