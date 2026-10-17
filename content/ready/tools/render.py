"""Carousel renderer: slides as HTML -> 1080x1350 PNG."""
import base64, os, sys, json, html
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.abspath(__file__))
SHOTS = os.path.join(ROOT, "..", "shots")
FD = os.path.join(ROOT, "node_modules/@fontsource")

def b64(path):
    ext = path.rsplit(".", 1)[1]
    mime = {"png": "image/png", "jpg": "image/jpeg", "webp": "image/webp", "woff2": "font/woff2"}[ext]
    return f"data:{mime};base64," + base64.b64encode(open(path, "rb").read()).decode()

def fonts():
    css = ""
    for fam, pkg, ws in [("Manrope", "manrope", [500, 700, 800])]:
        for w in ws:
            for sub in ["cyrillic", "latin"]:
                css += f"@font-face{{font-family:'{fam}';font-weight:{w};src:url({b64(f'{FD}/{pkg}/files/{pkg}-{sub}-{w}-normal.woff2')});}}"
    return css

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#F3ECE2;--ink:#26221F;--soft:#6E655D;--acc:#B4532F;--line:#DDD2C4;--card:#FBF7F1}
html,body{width:1080px;height:1350px}
body{background:var(--bg);color:var(--ink);font-family:'Manrope',sans-serif;position:relative;overflow:hidden}
body.dark{background:var(--ink);color:#F3ECE2}
body.dark .meta,body.dark .sub{color:#BDB3A8}
.meta{position:absolute;left:84px;right:84px;top:64px;display:flex;justify-content:space-between;font-weight:700;font-size:26px;color:var(--soft);letter-spacing:.02em}
.meta .dot{display:inline-block;width:18px;height:18px;border-radius:50%;background:var(--acc);margin-right:14px;vertical-align:-2px}
.foot{position:absolute;left:84px;bottom:60px;font-weight:700;font-size:24px;color:var(--soft)}
.wrap{position:absolute;left:84px;right:84px;top:150px;bottom:130px;display:flex;flex-direction:column}
h1{font-weight:800;font-size:84px;line-height:1.04;letter-spacing:-.02em}
h2{font-weight:800;font-size:62px;line-height:1.08;letter-spacing:-.015em}
.acc{color:var(--acc)}
.sub{font-weight:500;font-size:34px;line-height:1.38;color:var(--soft);margin-top:30px}
.body{font-weight:500;font-size:36px;line-height:1.42;margin-top:28px}
.phone{margin-top:auto;align-self:center;border-radius:46px;overflow:hidden;border:10px solid var(--ink);box-shadow:0 30px 60px rgba(38,34,31,.22);background:#fff}
.phone img{display:block}
.split{display:flex;gap:56px;flex:1;align-items:flex-end;margin-top:36px}
.split .txt{flex:1;align-self:center}
.list{margin-top:40px;display:flex;flex-direction:column;gap:26px}
.li{display:flex;gap:26px;align-items:flex-start;font-size:36px;font-weight:500;line-height:1.35}
.num{flex:none;width:58px;height:58px;border-radius:50%;background:var(--acc);color:#fff;font-weight:800;font-size:28px;display:flex;align-items:center;justify-content:center;margin-top:-4px}
.quote{margin:auto 0;font-weight:800;font-size:76px;line-height:1.1;letter-spacing:-.02em}
.quote .bar{display:block;width:110px;height:12px;background:var(--acc);margin-bottom:48px;border-radius:6px}
.table{margin-top:40px;background:var(--card);border-radius:28px;padding:30px 34px;border:2px solid var(--line);font-size:30px}
.row{display:grid;grid-template-columns:1.1fr 1.3fr 1fr;padding:18px 0;border-bottom:2px solid var(--line);font-weight:500}
.row:last-child{border:none}
.row.h{font-weight:800;color:var(--soft);font-size:24px;text-transform:uppercase;letter-spacing:.06em}
.row.bad{background:#F6DED3;margin:0 -34px;padding:18px 34px;color:#8A3415;font-weight:700}
.tag{display:inline-block;font-weight:800;font-size:24px;letter-spacing:.08em;text-transform:uppercase;color:var(--acc);margin-bottom:26px}
.price{font-weight:800;font-size:150px;letter-spacing:-.03em;line-height:1;margin-top:30px}
.cta{margin-top:auto;display:inline-flex;align-self:flex-start;gap:18px;align-items:center;background:var(--acc);color:#fff;font-weight:800;font-size:38px;padding:30px 46px;border-radius:999px}
.thumbs{display:flex;gap:36px;margin-top:auto;justify-content:center}
.thumbs .phone{margin-top:0}
.wrap.center{justify-content:center}
.center h2{font-size:80px;line-height:1.06}
.center .body{font-size:44px;line-height:1.4;margin-top:40px}
.center .sub{font-size:40px}
.center .cta{margin-top:70px}
.card{margin-top:56px;background:var(--card);border:2px solid var(--line);border-radius:28px;padding:34px 38px;font-size:32px;font-weight:600;display:flex;flex-direction:column;gap:20px}
.card .r{display:flex;justify-content:space-between;gap:20px}
.pill{font-weight:800;font-size:24px;padding:8px 18px;border-radius:999px;background:#E3EEDF;color:#2F6B2A;white-space:nowrap}
.pill.w{background:#F6DED3;color:#8A3415}
.mono{font-family:monospace;color:var(--soft)}
.cap{font-size:26px;font-weight:700;color:var(--soft);text-align:center;margin-top:20px}
"""

def phone(img, w=420, h=760, crop_top=0):
    return f'<div class="phone" style="width:{w}px;height:{h}px"><img src="{b64(os.path.join(SHOTS, img))}" style="width:{w-20}px;margin-top:-{crop_top}px"></div>'

def page(n, total, inner, dark=False, center=False):
    cls = " center" if center else ""
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{fonts()}{CSS}</style></head>
<body class="{'dark' if dark else ''}"><div class="meta"><span><span class="dot"></span>Ali · Websites · CRM · Automation</span><span>{n}/{total}</span></div>
<div class="wrap{cls}">{inner}</div><div class="foot">{'' if n == total else 'листай →'}</div></body></html>"""

def render(name, slides):
    out = os.path.join(ROOT, "out", name)
    os.makedirs(out, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1350})
        for i, s in enumerate(slides, 1):
            pg.set_content(page(i, len(slides), s.get("html", ""), s.get("dark", False), s.get("center", False)), wait_until="load")
            pg.wait_for_timeout(250)
            pg.screenshot(path=os.path.join(out, f"{i:02d}.png"))
        b.close()
    return out
