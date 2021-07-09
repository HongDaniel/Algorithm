function solution(board, moves) {
    var answer = 0;
    let stack = [];
    for (const m of moves) {
        for (let row = 0; row < board.length; row++) {
            if (board[row][m - 1] !== 0) {
                if (stack[stack.length - 1] !== board[row][m - 1]) {
                    stack.push(board[row][m - 1]);
                } else {
                    stack.pop();
                    answer += 2;
                }
                board[row][m - 1] = 0;
                break;
            }
        }
    }
    return answer;
}
