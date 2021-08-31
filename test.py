import pyupbit

access = "HTfwUiBTknxAEVJ3yjYFqzAu3VnPp4Cx9DGiMXsI"          # 본인 값으로 변경
secret = "5xUglTrWXOITeMUPwOxvPgpXH5ct1PvhPXD0hFLx"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회