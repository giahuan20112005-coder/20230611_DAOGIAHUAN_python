
A = 16
B = 3
C = 5


def phep_toan_so_hoc(a, b, c):
    print("--- 1. CÁC PHÉP TOÁN SỐ HỌC ---")
    print(f"Cộng (a + b): {a + b}")
    print(f"Trừ (a - c): {a - c}")
    print(f"Nhân (b * c): {b * c}")
    print(f"Chia (a / b): {a / b:.2f}")
    print(f"Lũy thừa (b ** 3): {b ** 3}")
    print()


def toan_tu_quan_he(a, b, c):
    print("--- 2. TOÁN TỬ QUAN HỆ ---")
    print(f"a > b: {a > b}")
    print(f"b < c: {b < c}")
    print(f"a == 16: {a == 16}")
    print(f"b != c: {b != c}")
    print()


def toan_tu_gan(a, b, c):
    print("--- 3. TOÁN TỬ GÁN ---")
    temp_a = a
    temp_a += b
    print(f"temp_a += b -> {temp_a}")

    temp_b = b
    temp_b *= c
    print(f"temp_b *= c -> {temp_b}")

    temp_c = c
    temp_c /= b
    print(f"temp_c /= b -> {temp_c:.2f}")
    print()


def toan_tu_logic(a, b, c):
    print("--- 4. TOÁN TỬ LOGIC ---")
    dk1 = a > b
    dk2 = b > c
    print(f"a > b: {dk1}")
    print(f"b > c: {dk2}")
    print(f"dk1 and dk2: {dk1 and dk2}")
    print(f"dk1 or dk2: {dk1 or dk2}")
    print(f"not dk1: {not dk1}")
    print()


def toan_tu_thao_tac_bit(a, b):
    print("--- 5. TOÁN TỬ THAO TÁC BIT ---")
    print(f"a & b: {a & b}")
    print(f"a | b: {a | b}")
    print(f"~a: {~a}")
    print(f"a ^ b: {a ^ b}")
    print(f"a << 3: {a << 3}")
    print(f"a >> 2: {a >> 2}")
    print()


def main():
    phep_toan_so_hoc(A, B, C)
    toan_tu_quan_he(A, B, C)
    toan_tu_gan(A, B, C)
    toan_tu_logic(A, B, C)
    toan_tu_thao_tac_bit(A, B)


if __name__ == '__main__':
    main()