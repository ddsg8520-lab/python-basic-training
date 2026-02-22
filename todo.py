def todo():
    todo_list = []
    def add_todo():
        try:
            b = str(input("할 일을 입력 하세요 : "))
            todo_list.append(f"{b}")
        except ValueError:
            print("잘못된 입력입니다")
    
    def del_todo():
        try:
            for i, item in enumerate(todo_list):
                print(i+1, item)
            del_a = int(input("삭제할 번호를 입력하세요: "))
            todo_list.pop(del_a-1)
        except ValueError:
            print("번호를 숫자로 입력하세요")
        except IndexError:
            print("존재하지 않는 번호입니다")

    def check_todo():
        print("할 일 목록입니다")
        for i, check_list in enumerate(todo_list):
            print(i+1, check_list)

    def save_todo():
        with open("todo.txt", "w", encoding="utf-8") as f:
            for item in todo_list:
                f.write(item + "\n")
    
    def load_todo():
        try:

            with open("todo.txt", "r", encoding="utf-8") as f:
                todo_list.clear()
                for line in f:
                    todo_list.append(line.strip())
        except FileNotFoundError:
            print("저장된 파일이 없습니다")

        
    while True:
        try:
            a = int(input("1.할 일 추가 2. 할 일 삭제 3. 목록 보기 4. 파일 저장 5. 파일 불러오기 0.종료"))
            if a == 0:
                print("종료합니다")
                break
            elif a == 1:
                add_todo()
            elif a == 2:
                del_todo()
            elif a == 3:
                check_todo()
            elif a == 4:
                save_todo()
            elif a == 5:
                load_todo()
            else:
                print("입력값이 올바르지 않습니다")

        except ValueError:
            print("잘못된 입력입니다")

todo()
        

