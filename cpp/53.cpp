#include<iostream>
#include<stack>
#include<algorithm>
using namespace std;
// int stack[100], top=-1;

// stack 직접 구현
// void push(int x){
//     stack[++top] = x;
// }

// int pop(){
//     return stack[top--];
// }

int main(){
    int n, k;
    stack<int> s;
    char str[20] = "0123456789ABCDEF";
    cin>>n>>k;
    while(n>0){         // 진수 변환
        s.push(n%k);
        n=n/k;
    }
    while(!s.empty()){
        cout<<str[s.top()];
        s.pop();
    }

    return 0;
}