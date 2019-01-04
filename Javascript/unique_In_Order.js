var uniqueInOrder=function(iterable){
  //your code here - remember iterable can be a string or an array
  let list = [...iterable]
  if (list.length > 1) {
    
    let adjacentUniqList = list.reduce(adjacentUniq, [])
    
    return adjacentUniqList
  } else {
    return list 
  }
}

function adjacentUniq (pre, cur, currentIndex) {

  if (currentIndex) {
    if (cur !== pre[pre.length - 1]) {
      pre.push(cur)
    }
    return pre
  }
  pre.push(cur)
  return pre
}
