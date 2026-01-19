# Audiophile Turntable - Technics SL-1300G Simulator (V3.98)

A high-fidelity, hybrid HTML5 vinyl player that simulates the tactile experience of a high-end Technics turntable directly in your browser. This project bridges the gap between digital convenience and analog nostalgia, allowing you to play local high-res audio files or stream directly from YouTube with a realistic interface.

## 🎛 Features

### 🎧 Hybrid Playback Engine
* **Local Playback:** Supports drag-and-drop or folder selection for MP3, FLAC, WAV, and OGG files.
* **YouTube Streaming:** Integrated YouTube IFrame API allows you to "spin" YouTube videos as if they were vinyl records.

### 🎚 Realistic Physics & UI
* **Accurate Mechanics:** Features a functioning Strobe Tower light, variable pitch slider, and 33/45/78 RPM speed switching with accurate platter physics.
* **Interactive Tonearm:** Drag-and-drop the needle onto the record grooves to seek through tracks (calculates track position based on time).
* **Visualizers:**
    * **Dual Analog VU Meters:** Real-time left/right channel monitoring.
    * **LED Spectrum Analyzer:** 65-band frequency visualization.
* **EQ Control:** Functional Bass and Treble knobs powered by the Web Audio API.

### 🎨 Design
* **Aesthetics:** Technics SL-1300G Aluminum styling with a wood base finish.
* **Dynamic Lighting:** LED indicators for Start/Stop, RPM selection, and Power.
* **Album Art:** Automatic album art rotation and "Cover Art" modal view.

## 🚀 How to Run
1.  Clone the repository:
    ```bash
    git clone [https://github.com/Babuptx/audiophile-turntable.git](https://github.com/Babuptx/audiophile-turntable.git)
    ```
2.  Navigate to the folder and open `index.html` in any modern web browser (Chrome/Edge/Brave recommended for Web Audio API support).

## 🕹 Controls
* **Power:** Click the large Power button to initialize the audio engine.
* **Start/Stop:** Spools up the motor and strobe light.
* **Eject Button (Local):** Opens file picker to load a folder of music.
* **Stream Button (YouTube):** Opens a modal to paste a YouTube URL.
* **Knobs:** Click and drag up/down on Volume, Bass, or Treble to adjust.

## 🛠 Technologies Used
* **Core:** HTML5, CSS3 (Variables, Gradients, Keyframe Animations), Vanilla JavaScript.
* **Audio:** Web Audio API (for EQ and Visualizers).
* **Streaming:** YouTube IFrame API.

## 👨‍💻 Credits
* **Design & Development:** Chittaranjan Panda
* *Dedicated to all Audiophiles.*

## 📄 License
This project is open-source and available under the MIT License.