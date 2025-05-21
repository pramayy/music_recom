import streamlit as st
from emotion_detector import detect_emotion_from_image
from spotify_utils import search_tracks_by_emotion

st.set_page_config(page_title="Emotion-Based Music Recommender 🎵")

st.title("Emotion-Detection Music Recommender")
st.markdown("Use your webcam to detect emotion and get music recommendations!")

img_file = st.camera_input("Take a picture")

if img_file is not None:
    # Save the image
    with open("captured.jpg", "wb") as f:
        f.write(img_file.getbuffer())
    st.image(img_file, caption="Captured Image", use_column_width=True)

    with st.spinner("Detecting emotion..."):
        emotion = detect_emotion_from_image("captured.jpg")

    if emotion:
        st.success(f"Detected Emotion: **{emotion.capitalize()}**")
        st.subheader("🎶 Recommended Tracks:")

        tracks = search_tracks_by_emotion(emotion)
        for track in tracks:
            st.write(f"🔹 [{track['name']} - {track['artist']}]({track['url']})")
    else:
        st.error("Failed to detect emotion. Try again.")

st.markdown("---")
st.markdown("Made by using DeepFace, Streamlit & Spotify API.")
