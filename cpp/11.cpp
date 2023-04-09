#include<iostream>
using namespace std;

int main(){
    int n, i, cnt=0, tmp;
    cin>>n;
    for(i=1; i<=n; i++){
        tmp=i;
        while(tmp>0){
            tmp=tmp/10;
            cnt++;
        }
    }

    cout<<cnt;

    return 0;
}