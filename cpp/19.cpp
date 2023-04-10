#include<iostream>
using namespace std;

int main(){
    int n, i, cnt=0, h[101], max;
    cin>>n;

    for(i=1; i<=n; i++){
        cin>>h[i];
    }

    max = h[n];
    for(i=n-1;i>=1;i--){
        if(h[i] > max){
            max = h[i];
            cnt ++;
        }
    }

    cout<<cnt;

    return 0;
}