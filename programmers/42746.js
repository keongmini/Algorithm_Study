function solution(numbers) {

    var answer = numbers.map(c=> c + '')
    var tmp = answer.sort((a,b) => (b+a) - (a+b)).join('');

    return answer[0]==='0'? '0' : answer;
}

s = solution([3, 30, 34, 5, 9])
console.log(s)