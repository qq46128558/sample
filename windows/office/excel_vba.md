# excel vba

## hello world 

檔案>>選項>>勾選開發人員的工具

頁簽>>開發人員>>巨集

新建巨集(sub),代碼:

	MsgBox ("Hello, world!")

彈出訊息視窗

### 程式註解與換行

	'單引號是註釋
	_ '行與行之間的結尾處要加上一個下底線，就是換行

## 基礎代碼

	Range("A1").Value = "Hello"
	Range("A1:A4").Value = 5
	Range("A1:A2,B3:C4").Value = 10
	'行，列
	Cells(1, 1).Value = 23
	Range(Cells(1, 1), Cells(4, 2)).Value = 13

	'選取狀態
	Range(Cells(1, 1), Cells(4, 2)).Select
	Rows(3).Select
	Columns(2).Select

	'複製，先select
	Selection.Copy

	'粘貼，先select
	ActiveSheet.Paste

	'清除儲存格
	Range("A1:A2").ClearContents
	Range("A1").Value = ""

	'指定工作表
	Worksheets("工作表1").Range("A1").Value = "工作表1的A1"
	Worksheets(1).Range("A1").Value = "工作表1的A1"
	Worksheets.Add
	Worksheets(1).Name = "新的工作表"
	MsgBox Worksheets.Count

	'活頁簿
	Workbooks("活頁簿1").Worksheets(1).Range("A1").Value = "Hello"
	Workbooks(1).Worksheets(1).Range("A1").Value = "Hello"
	MsgBox Workbooks.Count
	MsgBox Workbooks(1).Name
	Workbooks.Open "C:\VBA\demo.xlsx"
	Workbooks("demo").Save
	Workbooks("demo").SaveAs "C:\VBA\another.xlsx"
	Workbooks("demo").Activate
	Workbooks("demo").Close
	Workbooks.Close
	'關閉整個excel
	Application.Quit

	Dim x As Integer
	x = 5
	Dim x As Double
	Dim x As Boolean
	x = True
	Dim x As String
	x = "G.T.Wang"
	Dim x As Variant
	MsgBox "The value is " & x
	Option Explicit ' 強迫變數宣告
	Public MyVar As Integer
	Const MyInteger As Integer = 42
	Const myDate As Date = #2/2/2020#	

	If rainProb > 0.6  Then
	ElseIf
	Else
	End If
	
	Select Case x
	Case Is <= 5
	Case Else
	End Select

	For i = 1 To 10
	s = s + i
	Exit For
	Next i

	For Each wSheet In Worksheets
	Next wSheet
	
	Do While i <= 10
	Exit Do
	Loop

	Do
	Loop While i <= 10

	Do Until i > 10
	Loop

	Do
	Loop Until i > 10
	
	text1 = String(6, "A") ' 產生 AAAAAA
	text2 = String(3, 100) ' 產生 ddd
	MsgBox Len("Hello, world.")
	pos = InStr("Hello, world.", "world")
	pos = InStr(1, "Hello, World.", "world", vbTextCompare)
	pos = InStrRev("Hello, World.", "l")
	pos = InStrRev("Hello, WORLD.", "l", -1, vbTextCompare)
	MsgBox Left("Hello, world.", 5)
	MsgBox Right("Hello, world.", 6)
	MsgBox Mid("This is a message.", 6, 2)
	MsgBox "After Trim : " & Trim(mystr)
	MsgBox ("Hello," & Space(10) & "world.")
	Replace(字串, 搜尋文字, 替換文字[, 起始位置[, 替換次數[, 比對方式]]])
	StrComp(字串一, 字串二[, 比對方式])
	MsgBox StrReverse("Hello, world.")
	MsgBox UCase("Hello, world.") ' HELLO, WORLD.
	MsgBox LCase("Hello, world.") ' hello, world.
		
