// The solution must return if the given string is a isogram or not. An isogram is a word with no repeating letters.

function isIsogram(str) {
   let string = str.toLowerCase();
   let strArray = string.split('')
   let charArray = [];
   
   
   for(let i = 0; i < str.length; i++) {   
     if(charArray.includes(strArray[i])) {
       return false
     }
     
     charArray.push(strArray[i])
   }
  
  return true
}
