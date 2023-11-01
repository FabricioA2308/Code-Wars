// The solution must return a array without duplicates, keeping the last occurrence of each element.

function solve(arr) {
   let newArr = arr.slice().filter((a, b) => arr.indexOf(a) != b);
   for(let s = 0; s < newArr.length; s++) {
      arr.splice(arr.indexOf(newArr[s]), 1)
   }
   return arr
}
