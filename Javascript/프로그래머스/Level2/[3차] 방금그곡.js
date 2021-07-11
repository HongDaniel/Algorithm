function change(str) {
    str = str.replace(/C\#/g, '1').replace(/D\#/g, '2').replace(/F\#/g, '3').replace(/G\#/g, '4').replace(/A\#/g, '5');
    return str;
}
function solution(m, musicinfos) {
    var answer = '';
    let candi = [];

    for (let info of musicinfos) {
        info = info.split(',');
        let endtime = info[1];
        let starttime = info[0];
        let runtime =
            (Number(endtime.slice(0, 2)) - Number(starttime.slice(0, 2))) * 60 +
            Number(endtime.slice(3, 5)) -
            Number(starttime.slice(3, 5));

        let lyrics = info[3].match(/\D#?/g);
        let played = [];
        let tmp = 0;
        for (let i = 0; i < runtime; i++) {
            if (tmp == lyrics.length) {
                tmp = 0;
            }
            played.push(lyrics[tmp]);
            tmp += 1;
        }
        played = change(played.join(''));
        if (played.includes(change(m))) {
            candi.push({ title: info[2], length: runtime });
        }
    }
    candi.sort((a, b) => {
        if (a.length <= b.length) {
            return 1;
        } else {
            return -1;
        }
    });
    console.log(candi);

    if (candi.length === 0) {
        return '(None)';
    } else {
        return candi[0].title;
    }
}
