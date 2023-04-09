#include<iostream>
using namespace std;

int main(){
    int n, sum=0, c=1, d=9, result=0;
    cin>>n;

    while(sum+d<n){
        result = result + (c*d);
        sum = sum + d;
        c++;
        d = d * 10;
    }

    result = result + ((n - sum) * c);

    cout<<result;

    return 0;
}