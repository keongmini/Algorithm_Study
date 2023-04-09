#include<iostream>
using namespace std;

int digit_sum(int x){
    int tmp, sum = 0;

    while(x>0){
        tmp=x%10;
        sum+=tmp;
        x = x / 10;
    }

    return sum;
}

int main(){
    int n, num, i, sum, max=-2147000000, result;
    cin>>n;

    for(i=0; i<n; i++){
        cin>>num;
        sum=digit_sum(num);
        if(sum>max){
            max = sum;
            result = num;
        }
        else if(sum == max){
            if(num>result) result = num;
        }
    }

    cout<<result;

    return 0;
}