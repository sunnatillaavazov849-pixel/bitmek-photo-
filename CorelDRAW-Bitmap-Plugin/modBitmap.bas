Attribute VB_Name = "modBitmap"
Option Explicit

' Bitmap konverter - ishga tushirish: Tools > Macros > Run Macro > BitmapKonverter

Public Sub BitmapKonverter()
    Dim f As Object

    If Documents.Count = 0 Then
        MsgBox "Hujjat ochilmagan.", vbExclamation, "Bitmap"
        Exit Sub
    End If

    ' Oyna nomi orqali ochiladi - oyna topilmasa kompilyatsiya xatosi chiqmaydi
    On Error Resume Next
    Set f = VBA.UserForms.Add("frmBitmap")
    If f Is Nothing Then
        MsgBox "Oyna ochilmadi: " & Err.Description & vbCrLf & _
               "UserForm nomi: frmBitmap", vbCritical, "Bitmap"
        Exit Sub
    End If
    On Error GoTo 0
    f.Show
End Sub
