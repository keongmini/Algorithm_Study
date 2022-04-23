var dailyTemperatures = function(temperatures) {
    let answer = temperatures.map(a => 0)   // list comprehension 구현
    let stack = []
    
    for (const [index, cur] of temperatures.entries()) {    // enumerate 구현
      while (stack && cur > temperatures[stack[stack.length - 1]]){
          const last = stack.pop()
          answer[last] = index - last
      }
        stack.push(index)
    }
    
    return answer
};

// python 처럼 stack[-1]과 같이 마지막값 호출 불가
// append 대신 push
