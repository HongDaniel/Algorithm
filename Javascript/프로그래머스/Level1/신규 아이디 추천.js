function solution(new_id) {
    new_id = new_id.toLowerCase(); // 1단계

    new_id = new_id.replace(/[^\d\w-_.]/g, ''); // 2단계

    new_id = new_id.replace(/[\.]{2,}/g, '.'); // 3단계

    if (new_id[0] === '.') {
        // 4단계
        new_id = new_id.slice(1);
    }
    if (new_id[new_id.length - 1] === '.') {
        // 4단계
        new_id = new_id.slice(0, new_id.length - 1);
    }

    if (new_id.length === 0) {
        // 5단계
        new_id += 'a';
    }

    if (new_id.length > 15) {
        // 6단계
        new_id = new_id.slice(0, 15);
    }

    if (new_id[new_id.length - 1] === '.') {
        // 6단계
        new_id = new_id.slice(0, new_id.length - 1);
    }

    if (new_id.length < 3) {
        // 7단계
        while (true) {
            if (new_id.length === 3) {
                break;
            }
            new_id += new_id[new_id.length - 1];
        }
    }

    console.log(new_id);
    return new_id;
}
