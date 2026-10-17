"""Reel: 'Форма заявки — не экзамен'. Frames from a real local run of the DasMotors landing, no submit."""
import os, base64, subprocess
from playwright.sync_api import sync_playwright
from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "out", "reel")
FR = os.path.join(OUT, "frames"); os.makedirs(FR, exist_ok=True)
for f in os.listdir(FR): os.remove(os.path.join(FR, f))
CAP = os.path.join(OUT, "caps"); os.makedirs(CAP, exist_ok=True)
FD = os.path.join(ROOT, "node_modules/@fontsource/manrope/files")
PHOTO = "/home/claude/repos/auto-parts-landing/public/gallery/mercedes-headlamps.jpg"
HIDE = "nextjs-portal,[data-nextjs-toast]{display:none!important}"

CAPS = {
    "hook": ("Клиент не знает, как это называется.", "И не обязан."),
    "car": ("Машина — марка, модель, год.", "Не знаешь VIN — пропусти."),
    "part": ("Название, номер, описание или фото —", "хватит одного."),
    "more": ("Нужна ещё одна?", "Добавил — та же заявка."),
    "contact": ("Номер WhatsApp —", "и заявка уходит менеджеру."),
    "end": ("Форма заявки —", "не экзамен для клиента."),
}

def fonts():
    css = ""
    for w in (600, 800):
        for sub in ("cyrillic", "latin"):
            d = base64.b64encode(open(f"{FD}/manrope-{sub}-{w}-normal.woff2", "rb").read()).decode()
            css += f"@font-face{{font-family:M;font-weight:{w};src:url(data:font/woff2;base64,{d})}}"
    return css

def render_caps(b):
    pg = b.new_page(viewport={"width": 1080, "height": 590})
    for k, (a, c) in CAPS.items():
        foot = '<div class="f">Ali · сайты, CRM, автоматизация для бизнеса</div>' if k == "end" else ""
        pg.set_content(f"""<html><head><style>{fonts()}*{{margin:0}}body{{width:1080px;height:590px;background:#F3ECE2;font-family:M;display:flex;flex-direction:column;justify-content:center;padding:0 70px;box-sizing:border-box}}
        .a{{font-weight:800;font-size:68px;line-height:1.08;color:#26221F;letter-spacing:-.02em}}.c{{font-weight:800;font-size:68px;line-height:1.08;color:#B4532F;letter-spacing:-.02em}}
        .f{{margin-top:34px;font-weight:600;font-size:32px;color:#6E655D}}</style></head><body><div class="a">{a}</div><div class="c">{c}</div>{foot}</body></html>""")
        pg.screenshot(path=f"{CAP}/{k}.png")
    pg.close()

frames = []  # (path, seconds)
def snap(pg, cap, secs):
    p = f"{FR}/{len(frames):04d}.png"
    raw = p + ".raw.png"
    pg.screenshot(path=raw)
    canvas = Image.new("RGB", (1080, 1920), "#F3ECE2")
    canvas.paste(Image.open(f"{CAP}/{cap}.png"), (0, 0))
    shot = Image.open(raw).convert("RGB").resize((1080, 1330))
    canvas.paste(shot, (0, 590))
    canvas.save(p); os.remove(raw)
    frames.append((p, secs))

def typ(pg, sel, text, cap):
    loc = pg.locator(sel).first
    loc.click()
    for ch in text:
        loc.press_sequentially(ch)
        snap(pg, cap, 0.09)

with sync_playwright() as p:
    b = p.chromium.launch()
    render_caps(b)
    ctx = b.new_context(viewport={"width": 390, "height": 480}, device_scale_factor=2.77, is_mobile=True, has_touch=True, locale="ru-RU")
    ctx.route("**/fonts.googleapis.com/**", lambda r: r.abort())
    pg = ctx.new_page()
    pg.goto("http://localhost:3101", wait_until="networkidle"); pg.add_style_tag(content=HIDE)
    pg.wait_for_timeout(1500)
    form = pg.locator("form").first
    form.scroll_into_view_if_needed(); pg.wait_for_timeout(600)
    pg.evaluate("window.scrollBy(0, -10)")
    # hook: empty form
    snap(pg, "hook", 2.6)
    typ(pg, "input[name=carMake]", "Toyota", "car")
    typ(pg, "input[name=carModel]", "Camry", "car")
    typ(pg, "input[name=carYear]", "2022", "car")
    snap(pg, "car", 1.2)
    pg.locator("button.stepNext").click(); pg.wait_for_timeout(700)
    form.scroll_into_view_if_needed(); pg.wait_for_timeout(400)
    snap(pg, "part", 1.4)
    pg.locator("input[type=file]").first.set_input_files(PHOTO); pg.wait_for_timeout(700)
    pg.locator("input[type=file]").first.scroll_into_view_if_needed(); pg.evaluate("window.scrollBy(0, 120)"); pg.wait_for_timeout(400)
    snap(pg, "part", 2.4)
    pg.locator("button.addPartButton").click(); pg.wait_for_timeout(600)
    d = pg.locator("textarea[name$=-description], input[name$=-description]").nth(1)
    pg.get_by_text("Деталь 2", exact=True).first.evaluate("e=>{e.scrollIntoView({block:'start'});window.scrollBy(0,-70)}"); pg.wait_for_timeout(300)
    snap(pg, "more", 1.0)
    typ(pg, "input[name$=-name] >> nth=1", "Левое зеркало", "more")
    snap(pg, "more", 1.2)
    pg.locator("button.stepNext").click(); pg.wait_for_timeout(700)
    form.scroll_into_view_if_needed(); pg.wait_for_timeout(400)
    typ(pg, "input[name=contact]", "+971 50 000 0000", "contact")
    snap(pg, "contact", 1.6)
    snap(pg, "end", 3.2)
    b.close()

lst = os.path.join(OUT, "list.txt")
with open(lst, "w") as f:
    for path, s in frames:
        f.write(f"file '{path}'\nduration {s}\n")
    f.write(f"file '{frames[-1][0]}'\n")
mp4 = os.path.join(OUT, "reel-form-not-exam.mp4")
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst,
                "-vf", "fps=30,format=yuv420p", "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-movflags", "+faststart", mp4], check=True)
print(mp4, len(frames), "frames", round(sum(s for _, s in frames), 1), "sec")
