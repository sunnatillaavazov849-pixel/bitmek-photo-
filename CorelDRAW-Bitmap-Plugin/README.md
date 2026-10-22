# Bitmap — CorelDRAW plagini

Obyektlarni bir bosishda bitmapga aylantiradi.

![Ko'rinish](korinish.png)

## Sozlamalar

| Blok | Sozlama | Qiymatlar |
|---|---|---|
| 1 | Qamrov | Tanlangan · Sahifa · Hammasi |
| 1 | Usul | Alohida · Bitta |
| 2 | Rang | RGB · CMYK · Gray |
| 2 | Ruxsat | 30–3000 dpi (− / + tayyor qiymatlar bo‘yicha) |
| 2 | Yorqinlik | −100 … +100 % (− / + qadami 5) |
| 3 | Guruh bitta rasm | Guruh butunligicha bitta bitmap bo‘ladi |
| 3 | PowerClip ichi | PowerClip ichidagilar bitmap qilinadi, ramka vektor qoladi |
| 3 | Faqat rasmlar | Faqat bitmap obyektlar o‘zgaradi |
| 3 | Anti-aliasing | Silliq chetlar |
| 3 | Shaffof fon | Bitmap foni shaffof |

Har bir sozlamaning izohi sichqoncha olib borilganda ko‘rinadi.
Hammasi bitta **Ctrl+Z** bilan qaytariladi. Qulflangan va yashirin qatlamlarga tegmaydi.

## O‘rnatish

1. GitHub’da **Code → Download ZIP** orqali yuklab oling va arxivni oching.
2. CorelDRAW’da **Alt+F11** → chapda **GlobalMacros** ni tanlang.
3. **File → Import File...** → `modBitmap.bas`.
4. **File → Import File...** → `frmBitmap.frm` (`frmBitmap.frx` shu papkada turishi shart).
   Oyna **Forms** ichida `frmBitmap` nomi bilan paydo bo‘ladi.
5. **Ctrl+S**.

Ishga tushirish: **Tools → Macros → Run Macro** → `BitmapKonverter`.
Panelga tugma: **Tools → Customization → Commands → Macros**.

`tools/make_form.py` — `.frm`/`.frx` ni `tools/frmBitmap_code.vba` dan qayta yaratadi.

Yumaloq bloklar `%TEMP%` papkasidagi kichik `bmpk_*.bmp` rasmlar orqali chiziladi.
