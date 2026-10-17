"""Pitch mockup: first screen concept for a business without a website. Private file for a 1:1 pitch, not published."""
import os, base64
from playwright.sync_api import sync_playwright
from PIL import Image, ImageDraw, ImageFilter

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "out", "pitch-balsam"); os.makedirs(OUT, exist_ok=True)
FD = os.path.join(ROOT, "node_modules/@fontsource")
def ff(fam, pkg, ws):
    return "".join(f"@font-face{{font-family:'{fam}';font-weight:{w};src:url(data:font/woff2;base64,{base64.b64encode(open(f'{FD}/{pkg}/files/{pkg}-latin-{w}-normal.woff2','rb').read()).decode()})}}" for w in ws)

HTML = f"""<!doctype html><html><head><meta charset=utf-8><style>{ff('Manrope','manrope',[500,700,800])}{ff('Serif','source-serif-4',[400,500])}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:390px;height:844px;font-family:Manrope;background:#F6F8F7;color:#10302B;overflow:hidden}}
.nav{{display:flex;justify-content:space-between;align-items:center;padding:18px 20px}}
.logo{{font-weight:800;font-size:17px;letter-spacing:.01em}} .logo span{{color:#2F8F7E}}
.burger{{width:22px;height:14px;border-top:2px solid #10302B;border-bottom:2px solid #10302B;position:relative}}
.burger:after{{content:'';position:absolute;left:0;right:0;top:4px;border-top:2px solid #10302B}}
.hero{{padding:22px 22px 0}}
.badge{{display:inline-flex;gap:8px;align-items:center;background:#fff;border:1px solid #DCE7E4;border-radius:999px;padding:7px 12px;font-size:13px;font-weight:700}}
.badge b{{color:#E2A100}}
h1{{font-family:Serif;font-weight:500;font-size:38px;line-height:1.08;margin-top:18px;letter-spacing:-.01em}}
h1 i{{font-style:normal;color:#2F8F7E}}
.lead{{font-size:15.5px;line-height:1.5;color:#4A615D;margin-top:14px}}
.btns{{display:flex;flex-direction:column;gap:10px;margin-top:22px}}
.b1{{background:#1F8F5A;color:#fff;border-radius:14px;padding:16px;font-weight:800;font-size:16px;text-align:center}}
.b2{{background:#fff;border:1.5px solid #10302B;border-radius:14px;padding:14px;font-weight:700;font-size:15px;text-align:center}}
.facts{{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:22px}}
.f{{background:#fff;border:1px solid #DCE7E4;border-radius:14px;padding:12px 14px}}
.f small{{display:block;font-size:11px;font-weight:700;color:#7A8E8A;text-transform:uppercase;letter-spacing:.06em}}
.f span{{display:block;font-size:14.5px;font-weight:700;margin-top:4px}}
.f em{{display:block;font-style:normal;font-size:12px;color:#7A8E8A;margin-top:2px}}
.why{{margin-top:22px}}.why h3{{font-size:12px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:#7A8E8A}}
.why div{{display:flex;gap:10px;align-items:center;font-size:15px;font-weight:600;margin-top:10px}}.why div:before{{content:'✓';color:#1F8F5A;font-weight:800}}
.q{{margin-top:16px;background:#E7F3EF;border-radius:14px;padding:14px 16px;font-family:Serif;font-size:16px;line-height:1.4}}
.q small{{display:block;font-family:Manrope;font-size:12px;color:#4A615D;margin-top:6px}}
</style></head><body>
<div class=nav><div class=logo>Balsam <span>Dental</span></div><div class=burger></div></div>
<div class=hero>
<div class=badge><b>★ 4.9</b> · 854 Google reviews</div>
<h1>Calm, careful dental care in <i>Ajman</i></h1>
<div class=lead>Cleaning, treatment and check-ups by doctors patients keep recommending. Walk-ins welcome.</div>
<div class=btns><div class=b1>Book on WhatsApp</div><div class=b2>Call the clinic</div></div>
<div class=facts><div class=f><small>Open daily</small><span>11 AM – 10 PM</span><em>Fri from 2 PM</em></div><div class=f><small>Location</small><span>Al Nuaimiya 1</span></div></div>
<div class=q>“The treatment was completely pain-free.”<small>Google review</small></div>
<div class=why><h3>What patients mention most</h3><div>Spotless, well-organized clinic</div><div>Doctors explain everything clearly</div><div>Friendly, welcoming reception</div></div>
</div></body></html>"""

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 390, "height": 844}, device_scale_factor=3)
    pg.set_content(HTML); pg.wait_for_timeout(400)
    pg.screenshot(path=f"{OUT}/screen.png")
    b.close()

W, H = 1080, 1350
base = Image.new("RGBA", (W, H), (234, 240, 238, 255))
scr = Image.open(f"{OUT}/screen.png").convert("RGB")
sw = 520; shh = int(sw * 844 / 390); x, y = (W - sw) // 2, 90; bz = 22
sh = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(sh).rounded_rectangle([x - bz + 10, y - bz + 30, x + sw + bz + 10, y + shh + bz + 30], 80, fill=(0, 0, 0, 90))
base.alpha_composite(sh.filter(ImageFilter.GaussianBlur(40)))
ImageDraw.Draw(base).rounded_rectangle([x - bz, y - bz, x + sw + bz, y + shh + bz], 78, fill=(16, 20, 19, 255))
m = Image.new("L", (sw, shh), 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, sw, shh], 58, fill=255)
base.paste(scr.resize((sw, shh)), (x, y), m)
base.convert("RGB").save(f"{OUT}/balsam-concept.jpg", quality=92)
print(f"{OUT}/balsam-concept.jpg")
