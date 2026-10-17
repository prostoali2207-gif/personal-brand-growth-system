"""Non-musical UI sounds (soft taps and swipes) synthesized and muxed under silent videos.
No melody, no rhythm loop, no instruments: only short filtered noise and clicks at on-screen events."""
import sys, subprocess, numpy as np, wave, json

SR = 48000
rng = np.random.default_rng(7)

def tap(level=0.22):
    n = int(SR * 0.045)
    t = np.arange(n) / SR
    body = np.sin(2 * np.pi * 1800 * t) * np.exp(-t * 140)
    click = rng.normal(0, 1, n) * np.exp(-t * 400) * 0.35
    s = body + click
    return s / np.abs(s).max() * level

def swipe(dur=0.32, level=0.12):
    n = int(SR * dur)
    noise = rng.normal(0, 1, n)
    # simple band-limited noise: moving-average high-cut, then subtract heavier average for low-cut
    k1, k2 = 6, 60
    hp = np.convolve(noise, np.ones(k1) / k1, "same") - np.convolve(noise, np.ones(k2) / k2, "same")
    env = np.sin(np.pi * np.linspace(0, 1, n)) ** 1.6
    s = hp * env
    return s / np.abs(s).max() * level

def build(duration, events):
    out = np.zeros(int(SR * duration) + SR)
    for t, kind in events:
        s = tap() if kind == "tap" else swipe(*([0.5] if kind == "swipe-long" else []))
        i = int(t * SR); out[i:i + len(s)] += s[: len(out) - i]
    out = out[: int(SR * duration)]
    # fade edges
    f = int(0.02 * SR); out[:f] *= np.linspace(0, 1, f); out[-f:] *= np.linspace(1, 0, f)
    return out

def write(path, x):
    pcm = (np.clip(x, -1, 1) * 32767).astype(np.int16)
    st = np.stack([pcm, pcm], 1).ravel()
    with wave.open(path, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(st.tobytes())

if __name__ == "__main__":
    video, out, duration, ev = sys.argv[1], sys.argv[2], float(sys.argv[3]), json.loads(sys.argv[4])
    wav = out + ".wav"
    write(wav, build(duration, ev))
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", video, "-i", wav, "-c:v", "copy", "-c:a", "aac", "-b:a", "128k", "-shortest", "-movflags", "+faststart", out], check=True)
    print(out)
