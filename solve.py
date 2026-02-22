def 계산기():
    log = []
    def 계산():
        try:
            result = int(input("숫자를 입력 하세요: "))
        except ValueError:
            print("숫자만 입력하세요")
            return
        while True:
            try:
                before = result
            
                부호 = int(input("1. 더하기 2. 빼기 3. 곱하기 4. 나누기 0. 종료"))
                if 부호 == 0:
                    print("종료합니다")
                    break
                a = int(input("계산할 숫자를 입력 하세요: "))
                if 부호 == 1:
                    result += a
                    log.append(f"{before} + {a} = {result}")
                elif 부호 == 2:
                    result -= a
                    log.append(f"{before} - {a} = {result}")
                elif 부호 == 3:
                    result *= a
                    log.append(f"{before} * {a} = {result}")
                elif 부호 == 4:
                    if a == 0:
                        print("0은 나눌 수 없습니다")
                        continue
                    result /= a
                    log.append(f"{before} / {a} = {result}")
                else:
                    print("잘못된 선택입니다")
                    continue
                print(f"현재 결과: {result}")
                
            except ValueError:
                print("잘못된 입력입니다")
    def print_log():
        print("\n 계산 기록 : ")
        for items in log:
            print(items)

    계산()
    print_log()
계산기()