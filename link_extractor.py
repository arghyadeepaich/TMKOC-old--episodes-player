import yt_dlp

def extract_youtube_links(playlist_url):
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'skip_download': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(playlist_url, download=False)
        if 'entries' in result:
            video_urls = [entry['url'] for entry in result['entries']]
            return video_urls
        return []

# Replace with the actual playlist URL
playlist_url = "https://www.youtube.com/playlist?list=PLyBAqOWU1mfUGnBl8IMAcutxMeeHw1--p"  # The actual playlist URL goes here
episode_links = extract_youtube_links(playlist_url)

# Print the extracted links (for verification)
for link in episode_links:
    print(link)

# Optionally, save to a file
with open('episode_links.txt', 'w') as f:
    for link in episode_links:
        f.write(link + '\n')





