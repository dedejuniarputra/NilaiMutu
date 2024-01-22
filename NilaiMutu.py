tugas = float(input("Masukkan nilai tugasmu: "))
uts = float(input("Masukkan nilai UTSMU: "))
uas = float(input("Masukkan nilai UASMU: "))
nilai= (0.15*tugas) + (0.35*uts) + (0.50*uas)

if nilai > 8:
    mutu = 'A'
elif nilai > 70:
    mutu = 'B'
elif nilai > 60:
    mutu = 'C'
elif nilai > 50:
    mutu = 'D'
else:
    mutu = 'E'

if nilai > 60:
    status = 'Lulus'
else:
    status = 'Tidak Lulus'

print("+"*40)
print("        Program menentukan nilai" )
print("+"*40)

print(f'Nilai Akhir: {nilai:.2f}')
print(f'Mutu: {mutu}')
print(f'Status: {status}')
print("+"*40)
