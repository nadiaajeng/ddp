def nilai(n = 0):
    if n <= 60:
        print(f"Nilai {n} Tidak Lulus")
    elif n > 60 and n <= 100:
        print(f"Nilai {n} Lulus")
    else:
        print(f"Nilai {n} Tidak Diketahui")

nilai(80)
nilai()