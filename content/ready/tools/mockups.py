"""Device mockups (laptop + phone) carousel and FleetDesk phone slideshow reel."""
import os, base64, subprocess
from playwright.sync_api import sync_playwright
from PIL import Image, ImageDraw, ImageFilter

ROOT = os.path.dirname(os.path.abspath(__file__))
SH = os.path.join(ROOT, "..", "shots")
FD = os.path.join(ROOT, "node_modules/@fontsource")
css_ss = ""
for fam, pkg, ws in [("Source Serif 4", "source-serif-4", [400, 500]), ("Source Sans 3", "source-sans-3", [300, 400, 500, 600])]:
    for w in ws:
        for st in (["normal", "italic"] if "Serif" in fam else ["normal"]):
            for sub in ["cyrillic", "latin"]:
                css_ss += "@font-face{font-family:'%s';font-style:%s;font-weight:%d;src:url(https://localfont.test/%s/%s-%s-%d-%s.woff2) format('woff2');}" % (fam, st, w, pkg, pkg, sub, w, st)

def manrope():
    return "".join(f"@font-face{{font-family:M;font-weight:{w};src:url(data:font/woff2;base64,{base64.b64encode(open(f'{FD}/manrope/files/manrope-{s}-{w}-normal.woff2','rb').read()).decode()})}}" for w in (500, 800) for s in ("cyrillic", "latin"))

def text_png(b, w, h, a, c, color="#26221F", sub="#6E655D", size=60, path="t.png"):
    pg = b.new_page(viewport={"width": w, "height": h})
    pg.set_content(f"<html><head><style>{manrope()}*{{margin:0}}body{{background:transparent;font-family:M;text-align:center;padding-top:70px}}.a{{font-weight:800;font-size:{size}px;color:{color};letter-spacing:-.015em;line-height:1.1}}.b{{font-weight:500;font-size:34px;color:{sub};margin-top:16px}}</style></head><body><div class='a'>{a}</div><div class='b'>{c}</div></body></html>")
    pg.screenshot(path=path, omit_background=True); pg.close()
    return Image.open(path).convert("RGBA")

def shadowed(base, box, r, blur=36, alpha=90):
    sh = Image.new("RGBA", base.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle([box[0] + 8, box[1] + 26, box[2] + 8, box[3] + 26], r, fill=(0, 0, 0, alpha))
    sh = sh.filter(ImageFilter.GaussianBlur(blur)); base.alpha_composite(sh)

def laptop(base, img, x, y, sw):
    sh_ = int(sw * 0.625); bez = int(sw * 0.03)
    shadowed(base, (x - bez, y - bez, x + sw + bez, y + sh_ + bez), 28)
    d = ImageDraw.Draw(base)
    d.rounded_rectangle([x - bez, y - bez, x + sw + bez, y + sh_ + bez], 26, fill=(24, 22, 21, 255))
    base.paste(img.resize((sw, sh_)), (x, y))
    by = y + sh_ + bez
    d.polygon([(x - bez * 4, by), (x + sw + bez * 4, by), (x + sw + bez * 2, by + int(bez * 1.4)), (x - bez * 2, by + int(bez * 1.4))], fill=(196, 188, 178, 255))
    d.rounded_rectangle([x + sw // 2 - 70, by, x + sw // 2 + 70, by + 10], 5, fill=(170, 162, 152, 255))

def phone(base, img, x, y, sw):
    shh = int(sw * 2.165); bz = int(sw * 0.045)
    shadowed(base, (x - bz, y - bz, x + sw + bz, y + shh + bz), 60)
    ImageDraw.Draw(base).rounded_rectangle([x - bz, y - bz, x + sw + bz, y + shh + bz], int(sw * 0.15), fill=(18, 16, 15, 255))
    m = Image.new("L", (sw, shh), 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, sw, shh], int(sw * 0.11), fill=255)
    im = img.convert("RGB"); im = im.resize((sw, int(im.height * sw / im.width)))
    canvas = Image.new("RGB", (sw, shh), "white"); canvas.paste(im.crop((0, 0, sw, min(shh, im.height))), (0, 0))
    base.paste(canvas, (x, y), m)

with sync_playwright() as p:
    b = p.chromium.launch()
    # desktop captures
    ctx = b.new_context(viewport={"width": 1440, "height": 900}, device_scale_factor=1.5, locale="ru-RU")
    ctx.route("**/fonts.googleapis.com/**", lambda r: r.fulfill(status=200, content_type="text/css", body=css_ss))
    ctx.route("https://localfont.test/**", lambda r: r.fulfill(status=200, content_type="font/woff2", body=open(FD + "/" + r.request.url.split("localfont.test/")[1].split("/")[0] + "/files/" + r.request.url.split("/")[-1], "rb").read()))
    ctx.route("**/*supabase.co/**", lambda r: r.abort())
    pg = ctx.new_page()
    for url, name in [("http://localhost:3101", "ap-desk.png"), ("http://localhost:3102", "ls-desk.png")]:
        pg.goto(url, wait_until="networkidle"); pg.add_style_tag(content="nextjs-portal{display:none!important}"); pg.wait_for_timeout(2500)
        pg.screenshot(path=os.path.join(SH, name))
    ctx.close()

    out = os.path.join(ROOT, "out", "06-devices"); os.makedirs(out, exist_ok=True)
    apD, lsD = Image.open(f"{SH}/ap-desk.png"), Image.open(f"{SH}/ls-desk.png")
    apM, lsM = Image.open(f"{SH}/ap-hero.png"), Image.open(f"{SH}/ls-hero.png")
    BG = (243, 236, 226, 255)
    slides = [
        (apD, apM, "Лендинг для магазина автозапчастей", "Тёмный, технический, с заявкой за 3 шага"),
        (lsD, lsM, "Лендинг для преподавателя языков", "Спокойный, тёплый, с записью на пробный урок"),
    ]
    # cover: both laptops stacked
    base = Image.new("RGBA", (1080, 1350), BG)
    t = text_png(b, 1080, 300, "Лендинги, которые<br>я сделал", "Разные бизнесы — разный характер", size=66, path=f"{out}/t0.png")
    base.alpha_composite(t, (0, 0))
    laptop(base, lsD, 150, 380, 640); laptop(base, apD, 300, 760, 640)
    phone(base, apM, 820, 700, 170)
    base.convert("RGB").save(f"{out}/01.jpg", quality=93)
    for i, (D, M, a, c) in enumerate(slides, 2):
        base = Image.new("RGBA", (1080, 1350), BG)
        base.alpha_composite(text_png(b, 1080, 300, a, c, size=54, path=f"{out}/t{i}.png"), (0, 0))
        laptop(base, D, 90, 480, 760); phone(base, M, 740, 640, 250)
        base.convert("RGB").save(f"{out}/{i:02d}.jpg", quality=93)
    base = Image.new("RGBA", (1080, 1350), BG)
    base.alpha_composite(text_png(b, 1080, 1350, "Нужен такой же<br>для вашего бизнеса?", "Лендинг за 7 дней · 2 500 AED<br><br>Напишите в директ", size=70, path=f"{out}/t9.png"), (0, 380))
    base.convert("RGB").save(f"{out}/04.jpg", quality=93)

    # FleetDesk slideshow reel
    rd = os.path.join(ROOT, "out", "showcase-fleet"); fr = os.path.join(rd, "f"); os.makedirs(fr, exist_ok=True)
    W, H = 1080, 1920
    bg = Image.new("RGBA", (W, H), (43, 39, 36, 255))
    bg.alpha_composite(text_png(b, 1080, 300, "Система для автопроката", "Клиент регистрируется сам — с телефона", color="#F3ECE2", sub="#CBBFB2", size=54, path=f"{rd}/t.png"), (0, 0))
    screens = ["client-register-redesign-step-1-mobile.png", "client-register-redesign-step-2-mobile.png",
               "client-register-fixed-step-3-resident-mobile.png", "client-register-fixed-step-4-resident-mobile.png"]
    frames_imgs = []
    for s in screens:
        f = bg.copy(); phone(f, Image.open(f"{SH}/{s}"), (W - 600) // 2, 360, 600); frames_imgs.append(f.convert("RGB"))
    n = 0
    for k, im in enumerate(frames_imgs):
        for _ in range(48):
            im.save(f"{fr}/{n:04d}.jpg", quality=90); n += 1
        if k + 1 < len(frames_imgs):
            for t in range(12):
                Image.blend(im, frames_imgs[k + 1], (t + 1) / 13).save(f"{fr}/{n:04d}.jpg", quality=90); n += 1
    mp4 = os.path.join(rd, "showcase-fleet.mp4")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", "30", "-i", f"{fr}/%04d.jpg", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "19", "-movflags", "+faststart", mp4], check=True)
    b.close()
print("ok", n / 30, "sec")
