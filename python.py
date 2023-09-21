s = int(input('輸入秒數:'))
if s < 60:
  print('%d秒=0天0小時0分%d秒'%(s,s))
elif 60 <= s < 3600:
  a = s % 60
  b = s // 60
  print('%d秒=0天0小時%d分%d秒'%(s,b,a))
elif 3600 <= s < 86400:
  a = s % 60
  c = s //3600
  b = s % 3600 // 60
  print('%d秒=0天%d小時%d分%d秒'%(s,c,b,a))
elif 86400 <= s:
  a = s % 60
  d = s // 86400
  c = s % 86400 // 3600
  b = s % 86400 % 3600
  print('%d秒=%d天%d小時%d分%d秒'%(s,d,c,b,a))