def solve():
    log = []
    def calculate():
        try:
            result = int(input("숫자를 입력 하세요: "))
        except ValueError:
            print("숫자만 입력 하세요")
            return

        while True:
            try:
                y = int(input("1. 더하기 2. 빼기 3. 곱하기 4. 나누기 0. 종료"))
                if y == 0:
                    print("종료합니다")
                    break
                z = int(input("계산할 숫자를 입력하세요"))
                before = result

                if y == 1:
                    result += z
                    log.append(f"{before} + {z} = {result}")
                elif y == 2:
                    result -= z
                    log.append(f"{before} - {z} = {result}")
                elif y == 3:
                    result *= z
                    log.append(f"{before} * {z} = {result}")
                elif y == 4:
                    if z == 0:
                        print("0으로 나눌 수 없습니다")
                        continue
                    result /= z
                    log.append(f"{before} / {z} = {result}")
                else:
                    print("잘못된 입력입니다")
                    continue

                print(f"현재 결과: {result}")
            except ValueError:
                print("숫자만 입력 하세요")
    def print_log():
        print("\n계산 기록: ")
        for item in log:
            print(item)
    calculate()
    print_log()
    
solve()