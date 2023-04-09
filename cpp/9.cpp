#include<iostream>
using namespace std;

int cnt[50001];
int main(){
    int n, i, j;
    cin>>n;
    for(i=1;i<=n;i++){
        for(j=i;j<=n;j=j+i){
            cnt[j]++;
        }
    }
    for(i=1;i<=n;i++){
        cout<<cnt[i]<<" ";
    }

    return 0;
}