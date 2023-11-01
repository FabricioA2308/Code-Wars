// The solution must return a pattern, using N as the parameter of how many times it gets repeated.

function pattern(n){
  let output = "";
  let stars = "";
  
  for(let i = 1; i <= n; i++) {
    if(i == 1) {
        output += `1${stars}`
    }

    if(i >= 2) {
        output += `1${stars}${i}`
    }

    if(i != n) {
        output += '\n'
    }

    stars += '*'
  }
   
 return output;
}
