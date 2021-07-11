function solution(rows, columns, queries) {
    var answer = [];
    let board = new Array(rows);
    for (let r = 0; r < rows; r++) {
        // board 초기화
        board[r] = new Array(columns);
        for (let c = 0; c < columns; c++) {
            board[r][c] = columns * r + (c + 1);
        }
    }

    for (let query of queries) {
        let [x1, y1, x2, y2] = query;
        x1 -= 1;
        y1 -= 1;
        x2 -= 1;
        y2 -= 1;
        let tmp = board[x1][y1]; // 구멍
        let changed = [];

        for (let r = x1; r < x2; r++) {
            // 왼쪽
            board[r][y1] = board[r + 1][y1];
            changed.push(board[r][y1]);
        }

        for (let c = y1; c < y2; c++) {
            //아래
            board[x2][c] = board[x2][c + 1];
            changed.push(board[x2][c]);
        }

        for (let r = x2; r > x1; r--) {
            // 오른쪽
            board[r][y2] = board[r - 1][y2];
            changed.push(board[r][y2]);
        }

        for (let c = y2; c > y1; c--) {
            //위
            board[x1][c] = board[x1][c - 1];
            changed.push(board[x1][c]);
        }
        board[x1][y1 + 1] = tmp;
        changed.push(board[x1][y1 + 1]);
        answer.push(Math.min.apply(null, changed));
    }

    return answer;
}
