Attribute VB_Name = "modBitmap"
Option Explicit

' =====================================================================
'  BITMAP KONVERTER - CorelDRAW uchun plagin (makros)
'  Ishga tushirish: Tools > Macros > Run Macro > BitmapKonverter
' =====================================================================

Public Sub BitmapKonverter()
    Dim f As Object

    If Documents.Count = 0 Then
        MsgBox "Avval CorelDRAW hujjatini oching.", vbExclamation, "Bitmap konverter"
        Exit Sub
    End If

    ' Oyna nomi orqali ochiladi - shunda oyna topilmasa ham kompilyatsiya xatosi chiqmaydi
    On Error Resume Next
    Set f = VBA.UserForms.Add("frmBitmap")
    If f Is Nothing Then
        MsgBox "Oynani ochib bo'lmadi." & vbCrLf & vbCrLf & _
               "Xato: " & Err.Description & vbCrLf & vbCrLf & _
               "Tekshiring:" & vbCrLf & _
               "1) Insert > UserForm qilingan va (Name) = frmBitmap" & vbCrLf & _
               "2) frmBitmap_kod.txt kodi aynan shu UserForm ichiga (View Code) joylangan" & vbCrLf & _
               "3) Debug > Compile GlobalMacros - xato qatorni ko'rsatadi", _
               vbCritical, "Bitmap konverter"
        Exit Sub
    End If
    On Error GoTo 0
    f.Show
End Sub
