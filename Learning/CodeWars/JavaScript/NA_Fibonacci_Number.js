// See: https://www.codewars.com/kata/553e6558e848c5a3180000bc

/* compact version:
   var fib = (n, a=0, b=1) => n==0? a: fib(n-1, b, a+b)
*/

var fib = function (n) {
  var i, a = 0, b = 1;
  
  for (i = 1; i < n; i++) { 
    var c = a + b; 
    var a = b, b = c;
  }
  if (n>0) { 
    return b
  } else {
    return 0
  }
}