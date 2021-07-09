function solution(str1, str2) {
    var answer = 0;
    let ar1 = [];
    let ar2 = [];
    //소문자 변환
    str1 = str1.toLowerCase();
    str2 = str2.toLowerCase();

    //2글자씩 띄어주기
    for (let i = 0; i < str1.length - 1; i++) {
        let tmp = str1.slice(i, i + 2).match(/[a-z]+/g);
        // console.log(tmp);
        if (tmp !== null && tmp[0].length > 1) {
            ar1.push(tmp[0]);
        }
    }

    for (let i = 0; i < str2.length - 1; i++) {
        let tmp = str2.slice(i, i + 2).match(/[a-z]+/g);
        if (tmp !== null && tmp[0].length > 1) {
            ar2.push(tmp[0]);
        }
    }
    // console.log(ar1)
    // console.log(ar2)
    let set = new Set([...ar1, ...ar2]); // 모든요소
    let common = 0;
    let union = 0;

    set.forEach((el) => {
        let cnt1 = ar1.filter((each) => each === el).length;
        let cnt2 = ar2.filter((each) => each === el).length;
        common += Math.min(cnt1, cnt2);
        union += Math.max(cnt1, cnt2);
    });
    // console.log(common)
    // console.log(union)
    if (union !== 0) {
        return Math.floor((common / union) * 65536);
    } else {
        return 65536;
    }
}
