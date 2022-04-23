var MyQueue = function() {
    this.input = []
    this.output = []
};
// let 사용 x

MyQueue.prototype.push = function(x) {
    this.input.push(x)
};

MyQueue.prototype.pop = function() {
    this.peek()
    return this.output.pop()
};

MyQueue.prototype.peek = function() {
    if (!this.output.length){       // length없이 비교x
        while(this.input.length){
            this.output.push(this.input.pop())
        }
    }
    return this.output[this.output.length - 1]
};

MyQueue.prototype.empty = function() {
    return this.input.length === 0 && this.output.length === 0
    // return this.input === [] && this.output === [] 오류남
};
