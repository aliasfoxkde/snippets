// See: https://www.codewars.com/kata/5be7f613f59e0355ee00000f

function solve(a, b){
    var m = ['Jan', 'Mar', 'May', 'Jul', 'Aug', 'Oct', 'Dec'], c = 0, ans = []
    for (var i = a; i <= b; ++i) {
        for (var j of m) {
            if (new Date(j + " 1, " + i.toString()).getDay() == 5) {ans.push(j);c++}
        }
    }
    return [ans[0], ans[ans.length-1], c]
}