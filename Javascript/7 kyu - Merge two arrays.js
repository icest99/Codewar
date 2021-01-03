function mergeArrays(a, b) {
  c = [];
  var i;
  for (i = 0; i < a.concat(b).length ; i++){
    
    if (i < a.length) {
      c.push(a[i]);
    }
    
    if (i < b.length) {
      c.push(b[i]);
    }
  }
  return c
}

//A LOT CAN BE IMPROVE I WILL revisit this later, it's ok for now.