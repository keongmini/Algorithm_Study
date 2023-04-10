#include<iostream>
using namespace std;

int reverse(int x){
    int result = 0;
    int tmp;
    while(x>0){
        tmp = x % 10;
        result = result * 10 + tmp;
        x = x / 10;
    }
    return result;
}

bool isPrime(int x){
    int i;

    if(x == 1){
        return false;
    }
    
    bool flag = true;

    for(i=2; i<x; i++){
        if(x % i == 0){
            flag = false;
            break;
        }
    }
    return flag;
}

int main(){
    int n, num, i, tmp;
    cin>>n;

    for(i=1;i<=n;i++){
        cin>>num;

        tmp = reverse(num);
        if(isPrime(tmp)){
            cout<<tmp<<" ";
        }
    }

    return 0;
}