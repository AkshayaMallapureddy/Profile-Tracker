import streamlit as st
import requests

def check_social_media_accounts(name):
    platforms = {
        "Twitter": f"https://twitter.com/{name}",
        "Instagram": f"https://www.instagram.com/{name}",
        "Facebook": f"https://www.facebook.com/{name}",
        "TikTok": f"https://www.tiktok.com/@{name}",
        "GitHub": f"https://github.com/{name}"
    }
    
    results = {}
    for platform, url in platforms.items():
        response = requests.get(url)
        if response.status_code == 200:
            results[platform] = url
        else:
            results[platform] = "Not Found"
    
    return results

st.title("PROFILE TRACKER")
input_name = st.text_input("Enter your name")

if input_name:
    output = check_social_media_accounts(input_name)
    st.write("Here are the social media profiles found:")
    for platform, link in output.items():
        if link != "Not Found":
            st.write(f"[{platform}]({link})")
        else:
            st.write(f"{platform}: Not Found")