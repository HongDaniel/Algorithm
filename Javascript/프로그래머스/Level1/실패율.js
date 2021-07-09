function solution(N, stages) {
  var answer = [];
  let players=stages.length;
  let failor=[];
  for(let i=1;i<=N;i++){
      let current = stages.filter(el=>el===i).length // 현재 스테이지
      if (players>0){
      failor.push({idx:i,rate:current/players});
      players-=current
      }
      else {
          failor.push({idx:i,rate:0});
      }
  }
  
  failor.sort((a,b)=>{
      if(a.rate<b.rate)
      {
          return 1;
      }
      else if(a.rate>b.rate)
      {
          return -1;
      }
      else{
          if(a.idx>b.idx){
              return 1;
          }
          else{
              return -1;
          }
      }
  
  })
    
  return failor.map(el=>el.idx)
}