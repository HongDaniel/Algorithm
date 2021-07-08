target = 3


def dfs(start_node):
    stack = [start_node, ]  # 스택에 첫 번째 노드 삽입

    while(1):
        # stack이 비어있는지 확인
        if(len(stack) == 0):
            print("없음")
            return 0

        # stack의 맨 위의 노드를 pop
        node = stack.pop()

        # 꺼낸 노드가 타겟넘버와 같은지 확인
        if(target == node):
            print("찾음!")
            return node
