from datetime import datetime, timedelta

#datetime.now()
print(result)  # 2025-01-17 14:34:21.123456
print(result.year)  # 2025
print(result.month)  # 1
print(result.day)  # 17
print(result.hour)  # 14
print(result.minute)  # 34
print(result.second)  # 21

simdi = datetime.today()
print(result)  # 2025-01-17 14:34:21.123456

#datetime.ctime(simdi)
print(result)  # Fri Jan 17 14:34:21 2025
#datetime.strftime(simdi, "%Y")
print(result)  # 2025
#datetime.strftime(simdi, "%Y-%m-%d %H:%M:%S")
print(result)  # 2025-01-17 14:34:21

t = '21 April 2019 hour 10:12:30'
gun, ay, yil, _, saat = t.split()
print(gun)  # 21
print(ay)  # April
print(yil)  # 2019

#datetime.strptime(t, "%d %B %Y hour %H:%M:%S")
print(result)  # 2019-04-21 10:12:30
print(result.year)  # 2019

birthday = datetime(2005,12,29,9,0,0)
print(birthday)  # 2005-12-29 09:00:00
#datetime.timestamp(birthday)  # saniye
print(result)  # 1135852800.0
#datetime.fromtimestamp(result)  # saniye to datetime
print(result)  # 2005-12-29 09:00:00
#datetime.fromtimestamp(0)
print(result)  # 1970-01-01 00:00:00

#simdi - birthday
print(result)  # 7270 days, 5:34:21.123456
print(result.days)  # 7270
print(result.total_seconds())  # 627613621.123456
print(result.microseconds)  # 123456

#simdi + timedelta(days=10)
print(result)  # 2025-01-27 14:34:21.123456


"""
1970 tarihi, Unix epoch olarak bilinen zaman başlangıcını temsil eder. Unix epoch, 1 Ocak 1970, 00:00:00 UTC'dir ve Unix tabanlı sistemlerde zaman ölçümü bu tarihten başlar.
Bu tarih, bilgisayar sistemlerinde zamanın temsil edilmesi için kullanılan bir referans noktasıdır. Unix sistemlerinde zaman, bu tarihten itibaren geçen saniye sayısı olarak saklanır. Yani, 1970-01-01 00:00:00 UTC, "epoch time" ya da "Unix timestamp" olarak bilinen zaman ölçüm sisteminin başlangıcıdır.
Python'da, datetime.fromtimestamp(0) fonksiyonu, Unix epoch (1970-01-01 00:00:00) tarihine karşılık gelen zamanı verir.
"""
