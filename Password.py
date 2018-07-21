# Password 小程式

#建立密碼
password = 'a123456'

#錯了以後還可以輸入兩次
tryit = 2

#迴圈區塊 START
while True:											
	ask = input('請輸入密碼: ')

	if ask == password:
		print ('登入成功!')
		break
	if ask != password and tryit == 0:
		print ('登入失敗! OUT!')
		break
	else:
		print ('密碼輸入錯誤, 還有',tryit,'機會')
		tryit = tryit - 1
#迴圈區塊 END
													
