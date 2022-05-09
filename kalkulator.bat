@echo off
tittle Kalkulator
echo======================================
echo Kalkulator sederhana
echo======================================
:ulang
set /p A=Masukan Angka Pertama=
set /p B=Masukan Angka Kedua=
set /p o=Pilih Operator Hitung (+, -, *, /)=
echo======================================
set /a "jumlah" = A%o%B
echo Jumlah = %jumlah%
echo======================================
echo Tekan Tombol apa saja untuk mengulangi!!!
pause>null
goto ulang