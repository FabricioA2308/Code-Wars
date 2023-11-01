// The solution must return the sum of all multiples of 3 or 5 below the number passed in. If the number is a multiple of both, it should only count once.

function solution(number) {
   if(number == 0) return 0;

   let sum = 0;

   for(let i = 1; i < number; i++) {
      if(i % 3 == 0) {
         sum += i;
         continue;
      }

      if(i % 5 == 0) {
         sum += i;
         continue;
      }
   }
   return sum
}
