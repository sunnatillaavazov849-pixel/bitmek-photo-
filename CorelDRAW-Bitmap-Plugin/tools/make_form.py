"""frmBitmap.frm + frmBitmap.frx yaratish.

Ishlatish:  python tools/make_form.py
Kod manbai: tools/frmBitmap_code.vba (faqat ASCII).
"""
import os
import struct
import uuid

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
NAME = "frmBitmap"
CAPTION = "Bitmap"
CLIENT_W_PT = 294          # oyna ichki eni (pt)
CLIENT_H_PT = 522          # oyna ichki bo'yi (pt)

FORM_CLSID = uuid.UUID("C62A69F0-16DC-11CE-9E98-00AA00574A4F").bytes_le
FREESECT, ENDOFCHAIN, FATSECT, NOSTREAM = 0xFFFFFFFF, 0xFFFFFFFE, 0xFFFFFFFD, 0xFFFFFFFF


def himetric(pt):
    return int(round(pt * 2540 / 72))


# ---------------------------------------------------------------- streams
def ansi(s):
    b = s.encode("ascii") + b"\0"
    return struct.pack("<I", len(b)) + b


def uni(s):
    b = (s + "\0").encode("utf-16-le")
    return struct.pack("<I", len(s) + 1) + b


def compobj_stream():
    # [MS-OLEDS] 2.3.8 CompObjStream
    data = struct.pack("<II", 0xFFFE0001, 0x00000A03)
    data += struct.pack("<I", 0xFFFFFFFF) + FORM_CLSID
    data += ansi("Microsoft Forms 2.0 Form")
    data += ansi("Embedded Object")
    data += ansi("Forms.Form.1")
    data += struct.pack("<I", 0x71B239F4)
    data += uni("Microsoft Forms 2.0 Form")
    data += uni("Embedded Object")
    data += uni("Forms.Form.1")
    return data


def f_stream(w_hm, h_hm):
    # [MS-OFORMS] 2.2.10.1 FormControl - bo'sh oyna (elementlar kodda yaratiladi)
    propmask = (1 << 10) | (1 << 11) | (1 << 27)   # fDisplayedSize, fLogicalSize, fDrawBuffer
    body = struct.pack("<I", propmask)
    body += struct.pack("<I", 32000)               # DataBlock: DrawBuffer
    body += struct.pack("<ii", w_hm, h_hm)          # ExtraDataBlock: DisplayedSize
    body += struct.pack("<ii", w_hm, h_hm)          #                 LogicalSize
    data = struct.pack("<BBH", 0, 4, len(body)) + body
    # FormSiteData: CountOfSiteClassInfo, CountOfSites, CountOfBytes
    data += struct.pack("<HII", 0, 0, 0)
    return data


# ---------------------------------------------------------------- CFB v3
def dir_entry(name, typ, left=NOSTREAM, right=NOSTREAM, child=NOSTREAM,
              clsid=b"\0" * 16, start=ENDOFCHAIN, size=0):
    n = name.encode("utf-16-le") + b"\0\0"
    e = n.ljust(64, b"\0")
    e += struct.pack("<HBB", len(n), typ, 1)                 # 1 = black
    e += struct.pack("<III", left, right, child)
    e += clsid
    e += struct.pack("<I", 0) + b"\0" * 16                   # state, ctime, mtime
    e += struct.pack("<II", start, size) + struct.pack("<I", 0)
    assert len(e) == 128
    return e


def build_cfb(streams):
    """streams: [(name, bytes)] - hammasi < 4096 bayt (mini oqimda)."""
    mini = b""
    minifat = []
    placed = []
    for name, data in streams:
        if not data:
            placed.append((name, ENDOFCHAIN, 0))
            continue
        first = len(minifat)
        count = (len(data) + 63) // 64
        for i in range(count):
            minifat.append(first + i + 1 if i < count - 1 else ENDOFCHAIN)
        mini += data.ljust(count * 64, b"\0")
        placed.append((name, first, len(data)))

    # sektorlar: 0 FAT, 1 Directory, 2 MiniFAT, 3.. mini oqim
    mini_secs = max(1, (len(mini) + 511) // 512)
    assert len(minifat) <= 128
    fat = [FATSECT, ENDOFCHAIN, ENDOFCHAIN]
    for i in range(mini_secs):
        fat.append(3 + i + 1 if i < mini_secs - 1 else ENDOFCHAIN)
    fat += [FREESECT] * (128 - len(fat))

    # katalog: Root -> "o" (ildiz); o.left = "f"; o.right = "\x01CompObj"
    by = {n: (s, z) for n, s, z in placed}
    dirs = dir_entry("Root Entry", 5, child=2, clsid=FORM_CLSID,
                     start=3 if mini else ENDOFCHAIN, size=len(mini))
    dirs += dir_entry("f", 2, start=by["f"][0], size=by["f"][1])
    dirs += dir_entry("o", 2, left=1, right=3, start=by["o"][0], size=by["o"][1])
    dirs += dir_entry("\x01CompObj", 2, start=by["\x01CompObj"][0], size=by["\x01CompObj"][1])

    hdr = bytes.fromhex("D0CF11E0A1B11AE1") + b"\0" * 16
    hdr += struct.pack("<HHHHH", 0x3E, 3, 0xFFFE, 9, 6) + b"\0" * 6
    hdr += struct.pack("<IIIIIIIII", 0, 1, 1, 0, 4096, 2, 1, ENDOFCHAIN, 0)
    hdr += struct.pack("<I", 0) + struct.pack("<I", FREESECT) * 108
    assert len(hdr) == 512

    out = hdr
    out += struct.pack("<128I", *fat)
    out += dirs
    out += struct.pack("<128I", *(minifat + [FREESECT] * (128 - len(minifat))))
    out += mini.ljust(mini_secs * 512, b"\0")
    return out


def build_frx(w_hm, h_hm):
    cfb = build_cfb([("f", f_stream(w_hm, h_hm)), ("o", b""),
                     ("\x01CompObj", compobj_stream())])
    return struct.pack("<6I", 0x0008424C, len(cfb), 0, 0, w_hm, h_hm) + cfb


# ---------------------------------------------------------------- .frm
def build_frm(code):
    hdr = [
        "VERSION 5.00",
        "Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} %s" % NAME,
        '   Caption         =   "%s"' % CAPTION,
        "   ClientHeight    =   %d" % (CLIENT_H_PT * 20),
        "   ClientLeft      =   120",
        "   ClientTop       =   465",
        "   ClientWidth     =   %d" % (CLIENT_W_PT * 20),
        '   OleObjectBlob   =   "%s.frx":0000' % NAME,
        "   StartUpPosition =   1  'CenterOwner",
        "End",
        'Attribute VB_Name = "%s"' % NAME,
        "Attribute VB_GlobalNameSpace = False",
        "Attribute VB_Creatable = False",
        "Attribute VB_PredeclaredId = True",
        "Attribute VB_Exposed = False",
    ]
    lines = hdr + code.replace("\r\n", "\n").rstrip("\n").split("\n")
    text = "\r\n".join(lines) + "\r\n"
    return text.encode("ascii")    # ASCII bo'lmasa xato beradi


def main():
    with open(os.path.join(HERE, "frmBitmap_code.vba"), "rb") as fh:
        code = fh.read().decode("ascii")
    with open(os.path.join(OUT, NAME + ".frm"), "wb") as fh:
        fh.write(build_frm(code))
    with open(os.path.join(OUT, NAME + ".frx"), "wb") as fh:
        fh.write(build_frx(himetric(CLIENT_W_PT), himetric(CLIENT_H_PT)))


if __name__ == "__main__":
    main()
