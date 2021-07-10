function solution(files) {
    var answer = [];
    let newfiles = [];

    for (let i = 0; i < files.length; i++) {
        let file = files[i].match(/(\D+)(\d+)(.*)/);
        newfiles.push({ head: file[1].toLowerCase(), number: Number(file[2]), tail: file[3], index: i });
    }
    newfiles.sort((a, b) => {
        if (a.head !== b.head) {
            if (a.head > b.head) {
                return 1;
            } else {
                return -1;
            }
        } else {
            if (a.number >= b.number) {
                return 1;
            } else {
                return -1;
            }
        }
    });
    return newfiles.map((each) => {
        return files[each.index];
    });
}
