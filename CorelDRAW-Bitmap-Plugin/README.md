# Bitmap konverter — CorelDRAW plagini

CorelDRAW'dagi rasmlarni (yoki barcha obyektlarni) bir bosishda **bitmap** qiladi.

Oyna rangi — to'q kulrang, yozuvlar — oq.

## Imkoniyatlar

| Bo'lim | Variantlar |
|---|---|
| **Qamrov** | Faqat tanlanganlar · Joriy list · Barcha listlar |
| **Usul** | Har birini alohida bitmap · Listdagi hammasini bitta bitmap |
| **Rang rejimi** | RGB · CMYK · Grayscale |
| **Razreshenie (DPI)** | 72, 150, 200, 300, 600, 1200 yoki o'zingiz yozasiz (30–3000) |
| **Yorqinlik** | −100 (to'qroq) … 0 … +100 (ochroq) |
| **Qo'shimcha** | Guruhni butunligicha bitta rasm qilish · PowerClip ichidagilarni ham · Faqat rasmlarni o'zgartirish · Anti-aliasing · Shaffof fon |

Hammasi bitta **Undo** (Ctrl+Z) bilan qaytariladi.
Yashirin yoki qulflangan qatlamlar va qulflangan obyektlarga tegmaydi.

## O'rnatish (CorelDRAW X6 … 2024)

1. CorelDRAW'da **Alt + F11** bosing — VBA muharriri ochiladi.
2. Chap tomonda **GlobalMacros** (yoki `GlobalMacros (GlobalMacros.gms)`) ni tanlang.
3. **File → Import File...** → `modBitmap.bas` faylini tanlang.
4. **Insert → UserForm** — yangi bo'sh oyna paydo bo'ladi.
   Pastdagi **Properties** oynasida `(Name)` ni **`frmBitmap`** deb o'zgartiring.
   (Properties ko'rinmasa — **F4** bosing.)
5. Shu oynani o'ng tugma bilan bosib **View Code** ni tanlang,
   u yerdagi hamma narsani o'chirib, `frmBitmap_kod.txt` ichidagi butun kodni joylang.
6. **Ctrl + S** bilan saqlang va VBA muharririni yoping.

Oynaga tugma yoki matn qo'yish shart emas — hammasini kod o'zi chizadi.

## Ishga tushirish

**Tools → Scripts (Macros) → Run Macro...** → `modBitmap.BitmapKonverter`.

### Panelga tugma qo'yish
**Tools → Customization → Commands** → ro'yxatdan **Macros** ni tanlang →
`modBitmap.BitmapKonverter` ni sichqoncha bilan istalgan panelga sudrab qo'ying.

## Eslatma
* **Guruhni butunligicha bitta rasm qilish** (standart yoqilgan): guruh ichidagi hamma narsa
  (rasm, vektor, matn, PowerClip) birlashib **bitta bitmap** bo'ladi. O'chirilsa — guruhdagi har bir
  obyekt alohida bitmap bo'lib, yana guruhlanadi.
* **PowerClip ichidagilarni ham** (standart yoqilgan): PowerClip ichidagi obyektlar bitmap qilinib,
  o'z joyiga qaytariladi (ichidagi guruh ham bitta rasm bo'ladi). PowerClip ramkasi vektor bo'lib qoladi.
* Yorqinlik "Brighten" linzasi yordamida beriladi va bitmapga "yopishib" qoladi.
* "Har birini alohida" — har bir rasm o'z joyida alohida bitmap bo'lib qoladi.
* "Hammasini bitta" — har bir listdagi barcha obyektlar bitta bitmap bo'ladi.
