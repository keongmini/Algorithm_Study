var isValid = function(s) {
    const stack = []
    const paren = {
        ")" : "(",
        "}" : "{",
        "]" : "["
    }
    const keys = Object.keys(paren);
    
    for (let i=0; i<s.length; i++){
        if(!keys.includes(s[i])){
            stack.push(s[i])
        }else{
            if(!stack || paren[s[i]] !== stack.pop()){
                return false
            }
        }
    }
    return stack.length === 0
};
