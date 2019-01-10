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
		
## 陣列
	
	'VBA 的陣列索引預設是從 0 開始的	
	Dim MyArray(4) As Integer
	' 把 MyArray 的第 3 個值（索引為 2）設定為 10
	MyArray(2) = 10
	' 輸出 MyArray 的第 3 個值
	MsgBox MyArray(2)
	MsgBox IsArray(MyArray)
	arr = Array(1, 2, 3)
	MsgBox (arr(1))	
	' 索引從 1 開始的陣列
	Dim MyArray2(1 To 5) As Integer
	' 宣告一個 3 x 4 的矩陣
	Dim mat(2, 3) As Integer
	' 指定矩陣內特定元素的值
	mat(0, 0) = 2
	mat(2, 3) = 5
	' 取出矩陣內特定元素的值
	MsgBox (mat(2, 3))
	' 宣告動態陣列
	Dim MyDynArr() As Integer
	' 調整陣列大小
	ReDim MyDynArr(3)
	' 調整陣列大小，保留陣列內部資料
	ReDim Preserve MyDynArr(10)

	Erase MyDynArr

	Dim myTable As Variant
	' 將 Excel 工作表中特定範圍的資料讀取至 VBA 二維陣列中
	myTable = Sheets("工作表1").Range("A1:B5").Value
	
	' 使用 Split 以空白字元分割字串
	arr = Split("This is a test", " ")
	' 取得陣列長度
	ub = UBound(arr)

	' 建立測試用陣列
	arr = Array("ABC", "BCD", "CDE")
	' 篩選出含有 "B" 的元素
	flt = Filter(arr, "B")
	' 尋找 "BCD" 的位置
	pos = Application.Match("BCD", arr, 0)

## 時間

	' 宣告一個 Date 變數
	Dim d As Date
	' 設定日期
	d = DateValue("Jun 19, 2017")
	' DateSerial 可以接受數值的年、月、日，建立日期變數
	d = DateSerial(2016, 5, 10)
	' 時間的設定
	t = TimeValue("20:15")
	t = TimeSerial(20, 15, 20)
	' 設定日期與時間
	d = CDate("15/08/2013 8:25:00 PM")
	' 現在日期
	d = Date
	' 現在時間
	d = Time()
	' 現在日期與時間
	d = Now()
	' Timer 函數可以傳回從當天 12:00 AM 到目前的秒數
	MsgBox ("Timer is: " & Timer())
	MsgBox (IsDate("2017/5/21"))
	' DateAdd 可以計算日期或時間的加法運算，算出某段時間之後的時間點
	MsgBox ("一天後：" & DateAdd("d", 1, d))
	' 計算兩個時間點之間的時間間隔，可以使用 DateDiff 函數
	MsgBox ("相差分鐘: " & DateDiff("n", d1, d2))
	' 使用 Year、Month、Day 與 Weekday 來判斷日期的年、月、日與星期幾
	MsgBox ("年: " & Year(d))
	' 星期名稱
	wdn = WeekdayName(Weekday(d))
	' 月份名稱
	mn = MonthName(Month(d))
	' 時間的部分可以使用 Hour、Minute 與 Second
	MsgBox ("分：" & Minute(Now))
	MsgBox ("日：" & DatePart("d", Now))
	MsgBox ("星期：" & DatePart("w", Now))
	MsgBox ("週數：" & DatePart("ww", Now))
	MsgBox ("季：" & DatePart("q", Now))

	' FormatDateTime 可依據指定的格式輸出日期與時間
	0 或 vbGeneralDate	完整格式（預設值）
	1 或 vbLongDate	完整日期
	2 或 vbShortDate	簡短日期
	3 或 vbLongTime	完整時間
	4 或 vbShortTime	簡短時間
	MsgBox (FormatDateTime(d, 0))

## Function & Sub
	
VBA 的 Function 就像一般程式語言的函數，可傳入各種參數，進行自訂的運算，並將計算結果傳回。

	' 自行定義的函數
	Function myFun(x As Integer, y As Integer) As Integer
	  myFun = x + y
	End Function		

	a = myFun(3, 4)

VBA 的函數定義好之後，除了可以在一般的 VBA 程式碼中呼叫之外，也可以直接在 Excel 中使用，其使用方式就跟一般的 Excel 函數一樣，在儲存格中輸入等於，再加上自訂的函數名稱以及輸入的資料

VBA 的 Sub 與 Function 類似，可傳入各種參數並進行運算，但是沒有傳回值（沒有辦法傳回計算結果）。

	' 自行定義的子程序
	Sub mySub(x As Integer, y As Integer)
	  MsgBox ("x + y = " & x + y)
	End Sub

	' 呼叫 mySub 子程序
	mySub 1, 2

## 檔案的輸入與輸出
	
讀取外部文字檔
	
	Open 檔案位置 For Input As 檔案代碼

	' 文字檔案位置
	FilePath = "C:\ExcelDemo\demo.txt"
	' 開啟 FilePath 文字檔，使用編號 #1 檔案代碼
	Open FilePath For Input As #1
	' 執行迴圈，直到編號 #1 檔案遇到結尾為止
	Do Until EOF(1)
	  ' 從編號 #1 檔案讀取一行資料
	  Line Input #1, LineFromFile
	  ' 輸出一行資料
	  MsgBox (LineFromFile)
	Loop
	' 關閉編號 #1 檔案
	Close #1

寫入外部文字檔

	Open 檔案位置 For Output As 檔案代碼
	' 開啟 OutputFilePath 文字檔，使用編號 #2 檔案代碼
	Open OutputFilePath For Output As #2
	' 要寫入檔案的內容
	Content = "This is a test."
	' 將 Content 的內容寫入編號 #2 的檔案
	Print #2, Content
	' 關閉編號 #2 檔案
	Close #2

	' 以逗號分隔，寫入檔案
	Write #2, "Hello, World", 123

附加方式寫入檔案

	Open OutputFilePath For Append As #3

	' 自動取得檔案代碼
	FileNumber = FreeFile()

	' 取得目前 Excel 檔的儲存路徑
	PathName = Application.ActiveWorkbook.Path

## 錯誤處理
	
	On Error GoTo ErrorHandler   ' 啟用錯誤處理機制
	...
	Exit Sub    ' 結束子程序
	ErrorHandler:       ' 錯誤處理用的程式碼
	...
	Resume Next       ' 繼續往下執行

	On Error Resume Next   ' 忽略錯誤，繼續執行

## 事件
	
	Private Sub Workbook_SheetChange(ByVal Sh As Object, ByVal Target As Range)
	  MsgBox "儲存格 (" & Target.Row & "," & Target.Column _
	    & ") 更新為 " & Target.Value
	End Sub	

## 錄製巨集

將使用者的操作錄起來，自動產生 VBA 的指令稿。

它可以將使用者在 Excel 中的任何動作都記錄下來，然後自動產生可重複使用的 VBA 的程式碼，善用這個功能可以大幅降低 VBA 程式設計者的負擔，也可以讓開發者輕易發掘各種意想不到的 VBA 撰寫方式


