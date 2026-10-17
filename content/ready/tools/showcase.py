"""Showcase reel: smooth scroll of a real site inside a phone, on a calm background. Minimal text."""
import os, sys, base64, subprocess
from playwright.sync_api import sync_playwright
from PIL import Image, ImageDraw, ImageFilter

ROOT = os.path.dirname(os.path.abspath(__file__))
URL, NAME, LINE1, LINE2, BG = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]
OUT = os.path.join(ROOT, "out", NAME); FR = os.path.join(OUT, "f"); os.makedirs(FR, exist_ok=True)
FD = os.path.join(ROOT, "node_modules/@fontsource")

def text_layer(b):
    def f(w):
        return "".join(f"@font-face{{font-family:M;font-weight:{w};src:url(data:font/woff2;base64,{base64.b64encode(open(f'{FD}/manrope/files/manrope-{s}-{w}-normal.woff2','rb').read()).decode()})}}" for s in ("cyrillic","latin"))
    pg = b.new_page(viewport={"width": 1080, "height": 260})
    pg.set_content(f"<html><head><style>{f(500)}{f(800)}*{{margin:0}}body{{background:transparent;font-family:M;text-align:center;padding-top:60px}}"
                   f".a{{font-weight:800;font-size:54px;color:#F3ECE2;letter-spacing:-.01em}}.b{{font-weight:500;font-size:34px;color:#CBBFB2;margin-top:14px}}</style></head>"
                   f"<body><div class='a'>{LINE1}</div><div class='b'>{LINE2}</div></body></html>")
    p = os.path.join(OUT, "text.png"); pg.screenshot(path=p, omit_background=True); pg.close()
    return Image.open(p).convert("RGBA")

FD_SS = os.path.join(ROOT, "node_modules/@fontsource")
css = ""
for fam, pkg, ws in [("Source Serif 4", "source-serif-4", [400, 500]), ("Source Sans 3", "source-sans-3", [300, 400, 500, 600])]:
    for w in ws:
        for st in (["normal", "italic"] if "Serif" in fam else ["normal"]):
            for sub in ["cyrillic", "latin"]:
                css += "@font-face{font-family:'%s';font-style:%s;font-weight:%d;src:url(https://localfont.test/%s/%s-%s-%d-%s.woff2) format('woff2');}" % (fam, st, w, pkg, pkg, sub, w, st)

W, H = 1080, 1920
PW, PH = 640, 1386          # phone outer size
SW, SH = 600, 1300          # screen inside
with sync_playwright() as p:
    b = p.chromium.launch()
    txt = text_layer(b)
    ctx = b.new_context(viewport={"width": 390, "height": 845}, device_scale_factor=SW / 390, is_mobile=True, has_touch=True, locale="ru-RU")
    ctx.route("**/fonts.googleapis.com/**", lambda r: r.fulfill(status=200, content_type="text/css", body=css))
    ctx.route("https://localfont.test/**", lambda r: r.fulfill(status=200, content_type="font/woff2", body=open(FD_SS + "/" + r.request.url.split("localfont.test/")[1].split("/")[0] + "/files/" + r.request.url.split("/")[-1], "rb").read()))
    ctx.route("**/*supabase.co/**", lambda r: r.abort())
    pg = ctx.new_page(); pg.goto(URL, wait_until="networkidle")
    pg.add_style_tag(content="nextjs-portal{display:none!important}html{scroll-behavior:auto!important}")
    pg.wait_for_timeout(2000)
    total = min(pg.evaluate("document.body.scrollHeight") - 845, 845 * 7)
    # background + phone shell (static)
    base = Image.new("RGB", (W, H), BG)
    shell = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(shell)
    x0, y0 = (W - PW) // 2, 330
    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(shadow).rounded_rectangle([x0 + 10, y0 + 30, x0 + PW + 10, y0 + PH + 30], 90, fill=(0, 0, 0, 110))
    base.paste(shadow.filter(ImageFilter.GaussianBlur(40)), (0, 0), shadow.filter(ImageFilter.GaussianBlur(40)))
    d.rounded_rectangle([x0, y0, x0 + PW, y0 + PH], 86, fill=(18, 16, 15, 255))
    base.paste(shell, (0, 0), shell); base.paste(txt, (0, 0), txt)
    mask = Image.new("L", (SW, SH), 0); ImageDraw.Draw(mask).rounded_rectangle([0, 0, SW, SH], 66, fill=255)
    sx, sy = x0 + (PW - SW) // 2, y0 + (PH - SH) // 2
    # timeline: hold top, scroll with easing, hold end
    import math
    n_scroll = 210
    pos = [0] * 30 + [int(total * (0.5 - 0.5 * math.cos(math.pi * i / n_scroll))) for i in range(n_scroll + 1)] + [total] * 30
    for i, y in enumerate(pos):
        pg.evaluate(f"window.scrollTo(0,{y})")
        if i == 0 or pos[i] != pos[i - 1] or i % 15 == 0:
            pg.wait_for_timeout(40)
            pg.screenshot(path=os.path.join(OUT, "s.png"))
            scr = Image.open(os.path.join(OUT, "s.png")).convert("RGB").resize((SW, SH))
        fr = base.copy(); fr.paste(scr, (sx, sy), mask); fr.save(f"{FR}/{i:04d}.jpg", quality=90)
    b.close()
mp4 = os.path.join(OUT, f"{NAME}.mp4")
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", "30", "-i", f"{FR}/%04d.jpg", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "19", "-movflags", "+faststart", mp4], check=True)
Image.open(f"{FR}/0010.jpg").resize((540, 960)).save(os.path.join(OUT, "poster.jpg"), quality=80)
print(mp4, len(pos) / 30, "sec")
