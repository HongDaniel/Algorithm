const record = ['Enter uid1234 Muzi', 'Enter uid4567 Prodo', 'Leave uid1234', 'Enter uid1234 Prodo', 'Change uid4567 Ryan'];

function solution(record) {
    let db = {};
    let history = record.map((el) => el.split(' '));

    for (let ar of history) {
        // console.log(ar[2]);
        if (ar[0] === 'Enter') {
            db[ar[1]] = ar[2];
        } else if (ar[0] === 'Change') {
            db[ar[1]] = ar[2];
        }
    }
    console.log(db);
    var answer = [];
    for (let ar of history) {
        if (ar[0] === 'Enter') {
            answer.push(db[ar[1]] + '님이 들어왔습니다.');
        } else if (ar[0] === 'Leave') {
            answer.push(db[ar[1]] + '님이 나갔습니다.');
        }
    }
    console.log(answer);
    return answer;
}

solution(record);
