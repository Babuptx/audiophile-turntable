# 🎵 Hybrid Audiophile Turntable

A high-fidelity, browser-based vinyl turntable simulator that bridges the gap between local audio collections and cloud streaming.

**Live Demo:** [https://audiophile-turntable2.netlify.app](https://audiophile-turntable2.netlify.app)

![Version](https://img.shields.io/badge/version-60.0-red) ![Status](https://img.shields.io/badge/build-passing-brightgreen)

## 🌟 Overview
This project is a **client-side web application** that simulates the tactile experience of a high-end Technics turntable. It features a unique "Hybrid Engine" that allows users to seamlessly switch between playing local high-quality audio files and streaming music directly from YouTube, all within a unified, skinnable interface.

## ✨ Key Features

### 🎛️ Hyper-Realistic Interface
* **Physics-Based Tonearm:** Manual drag-and-drop needle drops, synchronized with track time.
* **Strobe Light & Platter Physics:** Accurate 33/45 RPM animations with authentic strobe calibration patterns.
* **Studio-Grade Controls:** * Professional Volume Fader with dynamic percentage readout.
    * Digital Transport Deck with Cue (<< >>) and Time Display.
    * Start/Stop motor inertia logic.

### 🚀 Hybrid Audio Engine
* **Local Playback:** Drag-and-drop support for local folders (MP3, FLAC, WAV).
* **YouTube Integration:** Embeds the YouTube API *inside* the record label, allowing for "Picture Disc" video playback that spins with the music.
* **Digital Playlist:** Auto-generated interactive playlist for local files with active track highlighting.

### 🎨 Customization
* **Hot-Swappable Skins:** Instantly toggle between:
    * **Technics Gold:** Classic brushed metal aesthetic.
    * **Walnut Wood:** Audiophile vintage hi-fi look.
    * **Arctic Marble:** Modern minimalist design.
* **High-Contrast UI:** Smart text coloring that adapts to the chosen skin for maximum readability.

## 🛠️ Tech Stack
* **Core:** HTML5, CSS3 (Advanced Animations & Variables), Vanilla JavaScript (ES6+).
* **Audio:** HTML5 Audio Context & YouTube IFrame Player API.
* **Architecture:** Serverless / Static Site.
* **Deployment:** CI/CD Pipeline via GitHub -> Netlify.

## 🚀 Local Installation
1.  Clone the repository:
    ```bash
    git clone [https://github.com/Babuptx/audiophile-turntable.git](https://github.com/Babuptx/audiophile-turntable.git)
    ```
2.  Navigate to the directory:
    ```bash
    cd audiophile-turntable
    ```
3.  Start a local server (Required for YouTube API security):
    ```bash
    python -m http.server
    ```
4.  Open `http://localhost:8000` in your browser.

## 🤝 Credits
* Concept inspired by "Needledrop" by Thomas Park.
* Developed by **Babu Ptx**.

---
*v60.0 - Gold Master Release*