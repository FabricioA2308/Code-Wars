// The solution must return the count of vowels in the input string.

function getCount(str) {
  let counter = 0;
  
  for(let i = 0; i <= str.length; i++) {
    let num = str.charCodeAt(i);
    
    if(num == 97 || num == 101 || num == 105 || num == 111 || num == 117) {
      counter++;
    }
    
    
  } 
  return counter
}
