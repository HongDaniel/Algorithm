m = 6;
n = 6;
board = ['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ'];

function pop(i, j, board) {
    // if(board[i][j]===board[i+1][j]===board[i][j+1]===board[i+1][j+1])
}

function solution(m, n, board) {
    var answer = 0;
    let newBoard = []; // 행,열 위치 바꾸기
    let visited = [];
    for (let i = 0; i < m; i++) {
        newBoard.push(new Array());
        visited.push(new Array());
    }
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            newBoard[j].push(board[i][j]);
            visited[j].push(false);
        }
    }

    console.log(newBoard);
    console.log(visited);
    return answer;
}

solution(m, n, board);
