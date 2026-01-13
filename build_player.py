import os

def generate_player():
    print("Building V60.0: Volume Percentage Display...")
    
    html_content = f"""
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Hybrid Turntable - V60</title>
  <style>
    :root {{ 
        --bg-color: #151515; 
        --led-active: #ff0000;   /* Red LED */
        --led-standby: #4a0000;  /* Dim Red */
        --led-off: #333; 
    }}

    body {{ background-color: var(--bg-color); font-family: 'Arial', sans-serif; margin: 0; height: 100vh; width: 100vw; overflow: hidden; user-select: none; display: flex; flex-direction: column; justify-content: center; align-items: center; gap: 15px; transition: background 0.5s; }}
    
    #center-stage {{ display: flex; flex-direction: column; align-items: center; gap: 30px; margin-right: 250px; transition: margin 0.5s; }}
    #plinth, .btn-3d, #volume-container, .brand-btn {{ transition: all 0.5s ease; background-size: cover; background-position: center; }}

    /* --- SKINS WITH CONTRAST VARIABLES --- */
    
    /* 1. GOLD: Dark Text */
    body.skin-gold {{ --text-color: #e0d1b6; --vol-color: #222; }}
    .skin-gold #plinth, .skin-gold .btn-3d, .skin-gold #volume-container, .skin-gold .brand-btn, .skin-gold #playlist-panel {{ 
        background-color: #e0d1b6; 
        background-image: repeating-linear-gradient(90deg, transparent 0, transparent 2px, rgba(0,0,0,0.03) 3px, transparent 4px), linear-gradient(135deg, #e0d1b6 0%, #f3eadd 40%, #e0d1b6 60%, #c4b496 100%); 
        border: 1px solid rgba(255,255,255,0.4); 
        box-shadow: 5px 5px 15px rgba(0,0,0,0.4), inset 1px 1px 1px rgba(255,255,255,0.6); 
        color: #333; 
    }}
    .skin-gold .brand-btn {{ font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-weight: 900; letter-spacing: 1px; text-transform: uppercase; }}
    .skin-gold .arm-material {{ background: linear-gradient(90deg, #ccc, #fff, #ccc); }} 
    .skin-gold .base-material {{ background: radial-gradient(circle, #e8e8e8, #999); }}

    /* 2. WOOD: White Text */
    body.skin-wood {{ --text-color: #e3d0c2; --vol-color: #fff; }}
    .skin-wood #plinth, .skin-wood .btn-3d, .skin-wood #volume-container, .skin-wood .brand-btn, .skin-wood #playlist-panel {{ 
        background-color: #5d4037; 
        background-image: repeating-linear-gradient(90deg, transparent 0px, transparent 2px, rgba(0,0,0,0.15) 3px, transparent 4px), repeating-radial-gradient(ellipse at 50% -20%, transparent 0, rgba(30,10,0,0.1) 10px, transparent 20px), linear-gradient(135deg, rgba(255,255,255,0.1) 0%, transparent 40%, rgba(0,0,0,0.2) 100%); 
        border: 2px solid #3e2723; 
        box-shadow: 5px 5px 15px rgba(0,0,0,0.6), inset 1px 1px 5px rgba(255,255,255,0.1); 
        color: #e3d0c2; 
    }}
    .skin-wood .brand-btn {{ font-family: 'Arial Black', Gadget, sans-serif; font-weight: 900; letter-spacing: 0px; text-transform: uppercase; }}
    .skin-wood .arm-material {{ background: linear-gradient(90deg, #555, #777, #555); }}
    .skin-wood .base-material {{ background: radial-gradient(circle, #666, #333); }}

    /* 3. MARBLE: Dark Text */
    body.skin-marble {{ --text-color: #00d0ff; --vol-color: #000; }}
    .skin-marble #plinth, .skin-marble .btn-3d, .skin-marble #volume-container, .skin-marble .brand-btn, .skin-marble #playlist-panel {{ 
        background-color: #f0f0f0; 
        background-image: radial-gradient(at 20% 20%, rgba(0,0,0,0.05) 0%, transparent 50%), linear-gradient(115deg, transparent 0%, rgba(0,0,0,0.03) 30%, transparent 30.5%), linear-gradient(45deg,  transparent 40%, rgba(0,0,0,0.02) 45%, transparent 50%); 
        border: 1px solid #fff; 
        box-shadow: 5px 5px 15px rgba(0,0,0,0.3); 
        color: #333; 
    }}
    .skin-marble .brand-btn {{ font-family: 'Verdana', sans-serif; font-weight: 100; letter-spacing: 3px; text-transform: uppercase; }}
    .skin-marble .arm-material {{ background: linear-gradient(90deg, #222, #444, #222); }}
    .skin-marble .base-material {{ background: radial-gradient(circle, #333, #000); }}

    /* COMPONENTS */
    #plinth {{ position: relative; width: 85vmin; height: 65vmin; border-radius: 6px; display: flex; justify-content: center; align-items: center; flex-shrink: 0; }}
    #plinth::before {{ content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0; border-radius: 6px; pointer-events: none; z-index: 1; mix-blend-mode: overlay; background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, transparent 50%); }}

    #strobe-tower {{ position: absolute; bottom: 25px; left: 45px; width: 50px; height: 70px; background: linear-gradient(90deg, #222 0%, #555 15%, #333 50%, #444 85%, #222 100%); border-radius: 8px 8px 4px 4px; box-shadow: inset 1px 1px 1px rgba(255,255,255,0.3), inset -2px -2px 5px rgba(0,0,0,0.9), 4px 4px 10px rgba(0,0,0,0.6); z-index: 50; display: flex; justify-content: center; padding-top: 14px; transition: all 0.2s ease-out; }}
    #strobe-tower::before {{ content: ''; position: absolute; top: 10px; left: 10px; right: 10px; bottom: 12px; background: #000; border-radius: 4px; box-shadow: inset 3px 3px 8px rgba(0,0,0,1); z-index: 0; }}
    #strobe-light {{ position: relative; z-index: 1; width: 14px; height: 14px; background-color: #311; border-radius: 50%; box-shadow: inset 0 0 4px rgba(0,0,0,0.8); transition: all 0.1s ease-out; }}
    #strobe-light.on {{ background-color: #fff; box-shadow: inset 0 0 3px #ffaa00, 0 0 6px #ff5500, 0 0 20px #ff0000, 0 0 40px 5px rgba(255, 0, 0, 0.9); }}
    #strobe-tower:has(#strobe-light.on) {{ background: linear-gradient(90deg, #311 0%, #833 15%, #622 50%, #733 85%, #311 100%); box-shadow: inset 1px 1px 1px rgba(255,200,200,0.5), inset -2px -2px 5px rgba(50,0,0,0.9), 0 0 25px rgba(255, 0, 0, 0.6); }}

    #platter {{ position: absolute; width: 62vmin; height: 62vmin; border-radius: 50%; background: radial-gradient(circle, #ddd 60%, #bbb 95%, #999 100%); box-shadow: 5px 10px 25px rgba(0,0,0,0.4); display: flex; justify-content: center; align-items: center; top: 50%; left: 45%; transform: translate(-50%, -50%); z-index: 2; }}
    #strobe-dots {{ position: absolute; top: 2px; left: 2px; right: 2px; bottom: 2px; border-radius: 50%; border: 6px dotted #444; z-index: 2; }}
    #strobe-reflection {{ position: absolute; top: 0; left: 0; right: 0; bottom: 0; border-radius: 50%; background: radial-gradient(circle at 15% 85%, rgba(255, 50, 50, 1) 0%, rgba(255,0,0,0.6) 15%, transparent 35%); z-index: 3; opacity: 0; transition: opacity 0.1s; pointer-events: none; mix-blend-mode: color-dodge; }}
    #strobe-reflection.on {{ opacity: 1; }}

    #record-container {{ width: 94%; height: 94%; border-radius: 50%; position: relative; z-index: 5; }}
    #record {{ width: 100%; height: 100%; border-radius: 50%; position: relative; background: repeating-radial-gradient(#111, #111 1px, #181818 2px); transition: transform 0.1s linear; }}
    #record::after {{ content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0; border-radius: 50%; background: conic-gradient(rgba(255,255,255,0) 0deg, rgba(255,255,255,0.1) 40deg, rgba(255,255,255,0.05) 50deg, rgba(255,255,255,0) 60deg, rgba(255,255,255,0) 200deg, rgba(255,255,255,0.1) 220deg, rgba(255,255,255,0) 250deg); pointer-events: none; z-index: 10; }}
    .groove-line {{ position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); border-radius: 50%; border: 1px solid rgba(255, 255, 255, 0.4); box-shadow: 0 0 2px rgba(255,255,255,0.2); pointer-events: none; z-index: 5; }}
    .spinning {{ animation: spin 1.8s infinite linear; }}
    .spinning-reverse {{ animation: spinReverse 1.8s infinite linear; }}
    @keyframes spin {{ from {{ transform: rotate(0deg); }} to {{ transform: rotate(360deg); }} }}
    @keyframes spinReverse {{ from {{ transform: rotate(360deg); }} to {{ transform: rotate(0deg); }} }}
    
    #label {{ width: 35%; height: 35%; background-color: #ff4500; border-radius: 50%; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); overflow: hidden; box-shadow: inset 0 0 20px rgba(0,0,0,0.5); border: 5px solid #0a0a0a; z-index: 20; }}
    #label img {{ width: 100%; height: 100%; object-fit: cover; transition: opacity 0.3s; pointer-events: none; }}
    #yt-container {{ width: 300%; height: 300%; position: absolute; top: -100%; left: -100%; pointer-events: none; opacity: 0; }}
    #yt-container.active {{ opacity: 1; }}
    #spindle {{ position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 12px; height: 12px; background: radial-gradient(circle at 30% 30%, #ddd, #888); border-radius: 50%; z-index: 30; box-shadow: 1px 2px 4px rgba(0,0,0,0.6); pointer-events: none; }}

    #arm-assembly {{ position: absolute; top: 25px; right: 25px; width: 140px; height: 140px; z-index: 100; }}
    #arm-base {{ position: absolute; top: 20px; left: 20px; width: 100px; height: 100px; border-radius: 50%; box-shadow: 0 5px 15px rgba(0,0,0,0.3); }}
    #arm-base::after {{ content: ''; position: absolute; top: 25px; left: 25px; width: 50px; height: 50px; background: conic-gradient(#bbb, #fff, #bbb); border-radius: 50%; box-shadow: 0 2px 5px rgba(0,0,0,0.2); }}
    #arm-rotate {{ position: absolute; top: 70px; left: 70px; width: 0; height: 0; transform-origin: center center; transform: rotate(0deg); transition: transform 0.05s linear; }}
    #arm-stick {{ position: absolute; top: 0; left: -9px; width: 18px; height: 48vmin; border-radius: 9px; box-shadow: 8px 8px 15px rgba(0,0,0,0.3); cursor: grab; }}
    #arm-stick:active {{ cursor: grabbing; }}
    #arm-stick::before {{ content: ''; position: absolute; top: -40px; left: -11px; width: 40px; height: 60px; background: inherit; filter: brightness(0.5); border-radius: 4px; box-shadow: 2px 2px 5px rgba(0,0,0,0.3); }}
    #headshell {{ position: absolute; bottom: -30px; left: -8px; width: 34px; height: 55px; border-radius: 4px; box-shadow: 2px 5px 8px rgba(0,0,0,0.2); transform-origin: top center; transform: rotate(23deg); }}
    #headshell::after {{ content: ''; position: absolute; bottom: 5px; right: -8px; width: 15px; height: 4px; background: #bbb; border-radius: 2px; transform: rotate(-10deg); }}

    #metadata-container {{ width: 85vmin; height: 60px; background: none; display: flex; align-items: center; justify-content: center; overflow: hidden; position: relative; z-index: 300; font-size: 22px; }}
    #scrolling-wrapper {{ white-space: nowrap; overflow: hidden; width: 100%; position: absolute; }}
    #scrolling-text {{ display: inline-block; font-family: 'Arial Narrow', Arial, sans-serif; font-weight: normal; padding-left: 100%; letter-spacing: 2px; color: var(--text-color); transition: color 0.5s ease; }}
    @keyframes scroll-left {{ 0% {{ transform: translate(0, 0); }} 100% {{ transform: translate(-100%, 0); }} }}

    #controls-container {{ position: fixed; bottom: 40px; left: 100px; width: 160px; z-index: 200; display: flex; flex-direction: column; align-items: center; gap: 20px; }}
    #right-panel {{ position: fixed; top: 0; right: 0; height: 100vh; width: 280px; display: flex; flex-direction: column; gap: 10px; padding: 20px; box-sizing: border-box; z-index: 400; }}
    
    #playlist-panel {{ flex-grow: 1; border-radius: 10px; padding: 10px; overflow-y: auto; background: rgba(0,0,0,0.5); backdrop-filter: blur(5px); scrollbar-width: thin; scrollbar-color: rgba(255,0,0,0.2) transparent; }}
    .track-item {{ padding: 8px 12px; border-radius: 4px; cursor: pointer; font-family: 'Arial Narrow', sans-serif; font-size: 14px; color: inherit; opacity: 0.7; border-bottom: 1px solid rgba(0,0,0,0.1); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
    .track-item:hover {{ opacity: 1; background: rgba(255,255,255,0.1); }}
    .track-item.active {{ opacity: 1; background: rgba(0,0,0,0.2); border-left: 4px solid var(--led-active); font-weight: bold; padding-left: 8px; color: #fff; }}

    #volume-container {{ 
        position: relative; height: 180px; width: 80px; 
        border-radius: 10px; display: flex; justify-content: center; align-items: center; 
    }}
    
    /* --- NEW PERCENTAGE DISPLAY (TOP) --- */
    #vol-percent {{
        position: absolute; top: 10px;
        font-family: 'Courier New', monospace; font-weight: bold; font-size: 12px;
        color: var(--vol-color); opacity: 0.8; pointer-events: none;
    }}

    /* --- MOVED LABEL (BOTTOM) --- */
    #volume-label {{ 
        position: absolute; bottom: 8px; 
        font-family: 'Arial', sans-serif; font-weight: bold; font-size: 12px; letter-spacing: 1px;
        color: var(--vol-color); 
        opacity: 0.9; pointer-events: none;
    }}
    
    input[type=range] {{ -webkit-appearance: none; width: 150px; height: 12px; background: transparent; transform: rotate(-90deg); cursor: pointer; z-index: 1; }}
    input[type=range]::-webkit-slider-runnable-track {{ width: 100%; height: 10px; background: #333; border-radius: 5px; box-shadow: inset 1px 1px 2px black; }}
    input[type=range]::-webkit-slider-thumb {{ 
        -webkit-appearance: none; height: 24px; width: 40px; 
        border-radius: 4px; background: #555; margin-top: -7px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.5); border: 1px solid #777;
    }}

    #transport-deck {{ 
        display: flex; align-items: center; gap: 15px; 
        background: rgba(0,0,0,0.3); padding: 10px 20px; border-radius: 8px; 
        border: 1px solid rgba(255,255,255,0.1); margin-top: 5px;
    }}
    .cue-btn {{
        width: 40px; height: 40px; border-radius: 50%; border: none; cursor: pointer;
        background: linear-gradient(145deg, #444, #222); box-shadow: 2px 2px 5px rgba(0,0,0,0.5);
        color: #fff; font-weight: bold; font-size: 14px; text-shadow: 0 0 5px var(--led-active);
        display: flex; justify-content: center; align-items: center;
    }}
    .cue-btn:active {{ background: #111; transform: scale(0.95); }}
    
    #time-display {{ 
        font-family: 'Courier New', monospace; font-size: 18px; font-weight: bold; 
        color: var(--led-active); background: #000; padding: 5px 15px; border-radius: 4px;
        box-shadow: inset 0 0 5px rgba(255,0,0,0.2); border: 1px solid #333;
        min-width: 140px; text-align: center;
    }}

    .btn-3d {{ border-radius: 10px; cursor: pointer; display: flex; justify-content: center; align-items: center; position: relative; font-size: 18px; }}
    .btn-3d:active {{ transform: scale(0.98); }}
    #speed-box {{ display: flex; gap: 20px; width: 100%; justify-content: space-between; }}
    .speed-btn {{ width: 80px; height: 50px; padding: 0 10px; font-size: 16px; display: flex; justify-content: space-between; align-items: center; }}
    .led-rect {{ width: 20px; height: 8px; border-radius: 2px; background-color: var(--led-off); box-shadow: inset 1px 1px 2px rgba(0,0,0,0.8); flex-shrink: 0; }}
    .speed-btn.active .led-rect {{ background-color: var(--led-active); box-shadow: 0 0 8px var(--led-active); }}
    
    #playBtn {{ width: 140px; height: 140px; flex-direction: column; gap: 20px; font-size: 20px; }}
    #playBtn .led-rect {{ position: static; width: 50px; height: 12px; background-color: var(--led-standby); box-shadow: 0 0 8px var(--led-standby); transition: background-color 0.2s; border: 1px solid rgba(0,0,0,0.5); }}

    .brand-btn {{ margin-top: 20px; font-size: 20px; border-radius: 6px; padding: 12px 25px; cursor: pointer; white-space: nowrap; text-shadow: 1px 1px 2px rgba(0,0,0,0.2); }}
    .round-btn {{ width: 80px; height: 80px; border-radius: 50%; display: flex; flex-direction: column; justify-content: center; align-items: center; gap: 3px; font-size: 10px; font-weight: bold; letter-spacing: 1px; color: #333; box-shadow: 5px 5px 10px rgba(0,0,0,0.5), inset 1px 1px 1px rgba(255,255,255,0.2); margin: 0 auto; }}
    .round-btn svg {{ width: 24px; height: 24px; fill: #333; }}
    #button-row {{ display: flex; justify-content: space-around; width: 100%; margin-top: auto; }}
    #urlModal {{ display: none; position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: rgba(0,0,0,0.8); z-index: 1000; justify-content: center; align-items: center; }}
    #modalContent {{ background: #222; border: 2px solid #555; padding: 20px; border-radius: 10px; display: flex; flex-direction: column; gap: 15px; width: 300px; }}
    #urlInput {{ padding: 10px; border-radius: 4px; border: none; }}
    #loadUrlBtn {{ padding: 10px; background: #28a745; color: white; border: none; border-radius: 4px; cursor: pointer; }}
    #cancelBtn {{ padding: 10px; background: #d9534f; color: white; border: none; border-radius: 4px; cursor: pointer; }}
  </style>
</head>
<body class="skin-gold">

  <audio id="audio" preload="auto"></audio>
  <input type="file" id="folderInput" webkitdirectory directory multiple style="display:none">

  <div id="urlModal">
      <div id="modalContent">
          <h3 style="color:white; margin:0;">Load YouTube Link</h3>
          <input type="text" id="urlInput" placeholder="Paste YouTube URL here...">
          <button id="loadUrlBtn">LOAD TRACK</button>
          <button id="cancelBtn">CANCEL</button>
      </div>
  </div>

  <div id="center-stage">
      <div id="plinth">
          <div id="strobe-tower"><div id="strobe-light"></div></div>
          <div id="platter">
              <div id="strobe-dots"></div>
              <div id="strobe-reflection"></div>
              <div id="record-container">
                <div id="record">
                  <div id="label">
                      <div id="yt-container"><div id="ytPlayer"></div></div>
                      <img id="label-img" src="" alt="">
                      <div id="spindle"></div>
                  </div>
                </div>
              </div>
          </div>
          <div id="arm-assembly">
            <div id="arm-base" class="base-material"></div>
            <div id="arm-rotate">
                <div id="arm-stick" class="arm-material"><div id="headshell" class="arm-material"></div></div>
            </div>
          </div>
      </div>
      <div id="metadata-container"><div id="scrolling-wrapper"><div id="scrolling-text">Please Load Music...</div></div></div>
  </div>

  <div id="controls-container">
    <div id="volume-container">
        <span id="vol-percent">100%</span>
        
        <input type="range" id="volume" min="0" max="100" step="1" value="100">
        
        <span id="volume-label">Vol</span>
    </div>
    
    <div id="speed-box">
        <button class="btn-3d speed-btn active" id="btn33">33 <div class="led-rect"></div></button>
        <button class="btn-3d speed-btn" id="btn45">45 <div class="led-rect"></div></button>
    </div>
    <button class="btn-3d" id="playBtn">START / STOP<div class="led-rect" id="status-led"></div></button>
    <button class="brand-btn" id="brandBtn">Technics SL-1300G</button>
    
    <div id="transport-deck">
        <button class="cue-btn" id="rwBtn">«</button>
        <div id="time-display">--:-- / --:--</div>
        <button class="cue-btn" id="ffBtn">»</button>
    </div>
  </div>

  <div id="right-panel">
      <div id="playlist-panel">
          <div style="text-align:center; padding:10px; opacity:0.6; font-size:12px;">NO TRACKS LOADED</div>
      </div>
      <div id="button-row">
          <button class="btn-3d round-btn" id="localBtn"><svg viewBox="0 0 24 24"><path d="M10 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2h-8l-2-2z"/></svg>LOCAL</button>
          <button class="btn-3d round-btn" id="streamBtn"><svg viewBox="0 0 24 24"><path d="M10 16.5l6-4.5-6-4.5v9zM12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z"/></svg>STREAM</button>
      </div>
  </div>

  <script src="https://www.youtube.com/iframe_api"></script>
  <script>
    let mode = 'LOCAL';
    let audioFiles = []; let trackNames = []; let imageFiles = []; let currentTrackIndex = 0; 
    let motorOn = false; let isDragging = false; let armAngle = 0; 
    let ytPlayer = null; let ytDuration = 0; let ytTimer = null;
    const REST_ANGLE = 0; const START_GROOVE = 22; const END_GROOVE = 48; const PLAYABLE_ARC = END_GROOVE - START_GROOVE;
    const defaultAlbumArt = "https://via.placeholder.com/300?text=No+Art";

    // DOM
    const audio = document.getElementById('audio');
    const record = document.getElementById('record');
    const strobeDots = document.getElementById('strobe-dots');
    const strobeLight = document.getElementById('strobe-light');
    const strobeReflect = document.getElementById('strobe-reflection');
    const labelImg = document.getElementById('label-img');
    const ytContainer = document.getElementById('yt-container');
    const scrollingText = document.getElementById('scrolling-text');
    const timeDisplay = document.getElementById('time-display');
    const statusLed = document.getElementById('status-led');
    const armRotate = document.getElementById('arm-rotate');
    const folderInput = document.getElementById('folderInput');
    const brandBtn = document.getElementById('brandBtn');
    const urlModal = document.getElementById('urlModal');
    const urlInput = document.getElementById('urlInput');
    const playlistPanel = document.getElementById('playlist-panel');
    const volPercent = document.getElementById('vol-percent');

    const skins = [
        {{ code: 'skin-gold', name: 'Technics SL-1300G', textColor: '#e0d1b6' }}, 
        {{ code: 'skin-wood', name: 'Denon DP-3000NE', textColor: '#e3d0c2' }}, 
        {{ code: 'skin-marble', name: 'Pro-Ject XA', textColor: '#00d0ff' }}
    ];
    let currentSkinIndex = 0;
    scrollingText.style.color = skins[0].textColor;

    brandBtn.addEventListener('click', () => {{
        currentSkinIndex = (currentSkinIndex + 1) % skins.length;
        document.body.className = skins[currentSkinIndex].code;
        brandBtn.innerText = skins[currentSkinIndex].name;
        scrollingText.style.color = skins[currentSkinIndex].textColor;
    }});

    // YOUTUBE
    function onYouTubeIframeAPIReady() {{
        let origin = (window.location.protocol === 'file:') ? undefined : window.location.origin;
        ytPlayer = new YT.Player('ytPlayer', {{
            height: '100%', width: '100%',
            playerVars: {{ 'controls': 0, 'disablekb': 1, 'origin': origin, 'playsinline': 1 }},
            events: {{ 'onStateChange': onPlayerStateChange, 'onReady': onPlayerReady, 'onError': onPlayerError }}
        }});
    }}
    function onPlayerReady(e) {{ e.target.setVolume(100); e.target.unMute(); }}
    function onPlayerError(e) {{ updateScrollingText("YouTube Error " + e.data); stopMotor(); }}
    function onPlayerStateChange(e) {{
        if (e.data == YT.PlayerState.PLAYING) {{ ytDuration = ytPlayer.getDuration(); startYTTimer(); }}
        else {{ stopYTTimer(); }}
        if (e.data == YT.PlayerState.ENDED) {{ stopMotor(); }}
    }}
    function startYTTimer() {{ stopYTTimer(); ytTimer = setInterval(() => {{ if(ytPlayer && ytPlayer.getCurrentTime) {{ let cur = ytPlayer.getCurrentTime(); updateTimeDisplay(cur, ytDuration); updateArmFromTime(cur, ytDuration); if(motorOn && ytPlayer.isMuted()) {{ ytPlayer.unMute(); }} if(motorOn && ytPlayer.getVolume() < 10) {{ ytPlayer.setVolume(100); }} }} }}, 500); }}
    function stopYTTimer() {{ if(ytTimer) clearInterval(ytTimer); }}

    // TRANSPORT BUTTONS
    function skipTime(seconds) {{
        if (mode === 'LOCAL') {{
            audio.currentTime = Math.min(Math.max(audio.currentTime + seconds, 0), audio.duration);
        }} else if (mode === 'YOUTUBE' && ytPlayer) {{
            let newTime = ytPlayer.getCurrentTime() + seconds;
            ytPlayer.seekTo(newTime, true);
        }}
    }}
    document.getElementById('rwBtn').onclick = () => skipTime(-10);
    document.getElementById('ffBtn').onclick = () => skipTime(10);

    // INPUTS
    document.getElementById('localBtn').onclick = () => {{ mode='LOCAL'; folderInput.click(); }};
    document.getElementById('streamBtn').onclick = () => {{
        if(window.location.protocol === 'file:') alert("Please use localhost:8000 for YouTube");
        mode='YOUTUBE'; urlModal.style.display='flex'; urlInput.focus(); 
    }};
    document.getElementById('cancelBtn').onclick = () => {{ urlModal.style.display='none'; }};
    document.getElementById('loadUrlBtn').onclick = () => {{
        let vidId = extractVideoID(urlInput.value);
        if(vidId) {{
            stopMotor();
            urlModal.style.display='none'; 
            labelImg.style.display = 'none'; ytContainer.classList.add('active');
            playlistPanel.innerHTML = '<div style="text-align:center; padding:10px; opacity:0.6;">STREAMING YOUTUBE</div>';
            if(ytPlayer && ytPlayer.loadVideoById) {{
                ytPlayer.loadVideoById(vidId); ytPlayer.pauseVideo();
                const oldGrooves = document.querySelectorAll('.groove-line'); oldGrooves.forEach(el => el.remove()); drawGrooves(1); 
                armAngle = REST_ANGLE; updateArmVisual(); updateScrollingText("Streaming...");
            }}
        }} else {{ alert("Invalid URL"); }}
    }};
    function extractVideoID(url) {{ var match = url.match(/^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=)([^#\&\?]*).*/); return (match && match[2].length == 11) ? match[2] : null; }}

    // LOCAL & PLAYLIST
    folderInput.addEventListener('change', (e) => {{
        const files = Array.from(e.target.files);
        if (files.length === 0) return;
        stopMotor();
        ytContainer.classList.remove('active'); labelImg.style.display = 'block';
        if(ytPlayer && ytPlayer.stopVideo) ytPlayer.stopVideo();

        const audioExts = ['.mp3', '.flac', '.wav', '.ogg', '.m4a'];
        const imgExts = ['.jpg', '.jpeg', '.png', '.gif'];
        let foundAudio = []; let foundImages = [];
        files.forEach(f => {{
            if(f.name.startsWith('.')) return; 
            if (audioExts.some(ext => f.name.toLowerCase().endsWith(ext))) foundAudio.push(f);
            if (imgExts.some(ext => f.name.toLowerCase().endsWith(ext))) foundImages.push(f);
        }});
        if (foundAudio.length === 0) {{ updateScrollingText("No music found!"); return; }}
        foundAudio.sort((a, b) => a.name.localeCompare(b.name));
        foundImages.sort((a, b) => a.name.localeCompare(b.name));
        audioFiles = foundAudio.map(f => URL.createObjectURL(f));
        trackNames = foundAudio.map(f => f.name.substring(0, f.name.lastIndexOf('.')));
        imageFiles = foundImages.map(f => URL.createObjectURL(f));
        if (imageFiles.length === 0) imageFiles = [defaultAlbumArt];
        updateScrollingText("Local: " + foundAudio.length + " Tracks");
        
        const oldGrooves = document.querySelectorAll('.groove-line');
        oldGrooves.forEach(el => el.remove());
        drawGrooves(foundAudio.length);
        renderPlaylist();
        loadTrackLocal(0);
        armAngle = REST_ANGLE; updateArmVisual();
    }});

    function renderPlaylist() {{
        playlistPanel.innerHTML = "";
        trackNames.forEach((name, index) => {{
            let div = document.createElement("div");
            div.className = "track-item";
            div.innerText = (index + 1) + ". " + name;
            div.onclick = () => {{
                loadTrackLocal(index);
                audio.currentTime = 0;
                let trackCount = audioFiles.length;
                let sliceSize = PLAYABLE_ARC / trackCount;
                armAngle = START_GROOVE + (index * sliceSize) + 0.1; 
                updateArmVisual();
                if(motorOn) audio.play();
            }};
            playlistPanel.appendChild(div);
        }});
    }}

    function highlightTrack(index) {{
        let items = document.querySelectorAll('.track-item');
        items.forEach(item => item.classList.remove('active'));
        if(items[index]) {{
            items[index].classList.add('active');
            items[index].scrollIntoView({{ behavior: "smooth", block: "center" }});
        }}
    }}

    function loadTrackLocal(index) {{
        if (index < 0 || index >= audioFiles.length) return;
        currentTrackIndex = index;
        updateScrollingText(trackNames[index]);
        audio.src = audioFiles[index];
        labelImg.src = imageFiles[index % imageFiles.length];
        highlightTrack(index);
    }}

    // CONTROLS
    document.getElementById('playBtn').addEventListener('click', () => {{
        motorOn = !motorOn;
        if (motorOn) {{
            startVisuals();
            if(mode === 'LOCAL') audio.play().catch(e=>console.log(e));
            if(mode === 'YOUTUBE' && ytPlayer) {{ ytPlayer.unMute(); ytPlayer.setVolume(100); ytPlayer.playVideo(); }}
        }} else {{ stopMotor(); }}
    }});

    function startVisuals() {{
        statusLed.style.backgroundColor="var(--led-active)"; statusLed.style.boxShadow="0 0 10px var(--led-active)";
        strobeLight.classList.add('on'); strobeReflect.classList.add('on'); record.classList.add('spinning');
        strobeDots.classList.add('spinning-reverse'); record.style.animationPlayState='running'; strobeDots.style.animationPlayState='running';
    }}
    function stopMotor() {{
        motorOn=false; statusLed.style.backgroundColor="var(--led-standby)"; statusLed.style.boxShadow="0 0 10px var(--led-standby)";
        strobeLight.classList.remove('on'); strobeReflect.classList.remove('on'); record.style.animationPlayState='paused'; strobeDots.style.animationPlayState='paused';
        if(mode==='LOCAL') audio.pause();
        if(mode==='YOUTUBE' && ytPlayer) ytPlayer.pauseVideo();
    }}

    // PHYSICS & UTILS
    const armStick = document.getElementById('arm-stick');
    armStick.addEventListener('mousedown', () => {{ isDragging = true; armRotate.style.transition = 'none'; }});
    document.addEventListener('mouseup', () => {{ 
        if(isDragging) {{ isDragging = false; armRotate.style.transition = 'transform 0.2s ease-out';
            if (armAngle >= START_GROOVE && armAngle <= END_GROOVE) handleNeedleDrop();
            else if (armAngle < -5) {{ armAngle = REST_ANGLE; updateArmVisual(); }}
        }}
    }});
    document.addEventListener('mousemove', (e) => {{
        if (!isDragging) return;
        e.preventDefault();
        const armBox = document.getElementById('arm-assembly').getBoundingClientRect();
        const pivotX = armBox.left + 70; const pivotY = armBox.top + 70;
        let angle = (Math.atan2(e.clientY - pivotY, e.clientX - pivotX) * 180 / Math.PI) - 90;
        if (angle < -10) angle = -10; if (angle > 60) angle = 60;
        armAngle = angle; updateArmVisual();
    }});
    function updateArmVisual() {{ armRotate.style.transform = `rotate(${{armAngle}}deg)`; }}
    function handleNeedleDrop() {{
        let percent = (armAngle - START_GROOVE) / PLAYABLE_ARC; 
        if (mode === 'LOCAL') {{
            if(audioFiles.length === 0) return;
            let trackCount = audioFiles.length;
            let rawIndex = Math.floor(percent * trackCount);
            if (rawIndex >= trackCount) rawIndex = trackCount - 1; if (rawIndex < 0) rawIndex = 0;
            let sliceSize = 1.0 / trackCount;
            let sliceStart = rawIndex * sliceSize;
            let progressInSlice = (percent - sliceStart) / sliceSize; 
            if (rawIndex !== currentTrackIndex) {{ loadTrackLocal(rawIndex); audio.currentTime = 0; if(motorOn) audio.play(); }}
            else if (!isNaN(audio.duration)) {{ audio.currentTime = progressInSlice * audio.duration; if(motorOn) audio.play(); }}
        }} else if (mode === 'YOUTUBE' && ytPlayer) {{
            if (percent < 0) percent = 0; if (percent > 1) percent = 1;
            let seekTo = percent * ytDuration; ytPlayer.seekTo(seekTo, true); if(motorOn) ytPlayer.playVideo();
        }}
    }}
    function updateTimeDisplay(cur, total) {{ timeDisplay.innerText = `${{formatTime(cur)}} / ${{formatTime(total)}}`; }}
    function updateArmFromTime(cur, total) {{
        if(isDragging || total === 0) return;
        let percentGlobal = cur / total;
        if (mode === 'LOCAL') {{
            let sliceSize = PLAYABLE_ARC / audioFiles.length;
            armAngle = START_GROOVE + (currentTrackIndex * sliceSize) + (percentGlobal * sliceSize); 
        }} else {{ armAngle = START_GROOVE + (percentGlobal * PLAYABLE_ARC); }}
        updateArmVisual();
    }}
    audio.addEventListener('timeupdate', () => {{ if (!isNaN(audio.duration)) {{ updateTimeDisplay(audio.currentTime, audio.duration); updateArmFromTime(audio.currentTime, audio.duration); }} }});
    audio.addEventListener('ended', () => {{ if (currentTrackIndex < audioFiles.length - 1) {{ loadTrackLocal(currentTrackIndex + 1); if(motorOn) audio.play(); }} else {{ stopMotor(); }} }});
    function formatTime(s) {{ if(isNaN(s)) return "00:00"; let m = Math.floor(s/60); let sec = Math.floor(s%60); return (m<10?"0"+m:m) + ":" + (sec<10?"0"+sec:sec); }}
    function updateScrollingText(text) {{ scrollingText.style.animation = 'none'; scrollingText.innerText = text + "  *** " + text + "  *** "; scrollingText.offsetHeight; let duration = Math.max(10, text.length / 3) + 's'; scrollingText.style.animation = `scroll-left ${{duration}} linear infinite`; }}
    function drawGrooves(cnt) {{ let step = PLAYABLE_ARC / cnt; for (let i = 1; i < cnt; i++) {{ let groove = document.createElement('div'); groove.className = 'groove-line'; let rp = 100 - (((step*i)/PLAYABLE_ARC) * (100 - 35)); groove.style.width = rp + '%'; groove.style.height = rp + '%'; record.appendChild(groove); }} }}
    
    // VOLUME LOGIC UPDATE
    document.getElementById('volume').addEventListener('input', (e) => {{ 
        let v = e.target.value; 
        audio.volume = v/100; 
        if(ytPlayer) ytPlayer.setVolume(v);
        volPercent.innerText = v + "%";
    }});
    
    document.getElementById('btn33').onclick = () => {{ audio.playbackRate = 1.0; if(ytPlayer) ytPlayer.setPlaybackRate(1.0); record.style.animationDuration = '1.8s'; strobeDots.style.animationDuration = '1.8s'; document.getElementById('btn33').classList.add('active'); document.getElementById('btn45').classList.remove('active'); }};
    document.getElementById('btn45').onclick = () => {{ audio.playbackRate = 1.35; if(ytPlayer) ytPlayer.setPlaybackRate(1.25); record.style.animationDuration = '1.33s'; strobeDots.style.animationDuration = '1.33s'; document.getElementById('btn33').classList.remove('active'); document.getElementById('btn45').classList.add('active'); }};

  </script>
</body>
</html>
    """

    with open("index.html", "w", encoding='utf-8') as f:
        f.write(html_content)
    
    print("Success! V60.0 Volume Percentage Display Created.")
    print("-------------------------------------------------")
    print("Refresh your browser at http://localhost:8000")
    print("-------------------------------------------------")

if __name__ == "__main__":
    generate_player()