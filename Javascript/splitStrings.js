// The solution must return a array of the characters from the input string, separated in pairs. If the string has a odd number of characters, it must add a underscore to the final character.

function solution(str) {
  const pairs = [];
  
   if(str.length % 2 != 0) {
    str += "_"
  }

  for(let i = 0; i < str.length; i += 2) {
     const par = str.slice(i, i + 2)
     pairs.push(par)
  }
 
  return pairs
}
