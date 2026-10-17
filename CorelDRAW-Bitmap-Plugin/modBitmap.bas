Attribute VB_Name = "modBitmap"
Option Explicit

' =====================================================================
'  BITMAP KONVERTER - CorelDRAW uchun plagin (makros)
'  Ishga tushirish: Tools > Macros > Run Macro > BitmapKonverter
' =====================================================================

Public Sub BitmapKonverter()
    If Documents.Count = 0 Then
        MsgBox "Avval CorelDRAW hujjatini oching.", vbExclamation, "Bitmap konverter"
        Exit Sub
    End If
    frmBitmap.Show
End Sub
