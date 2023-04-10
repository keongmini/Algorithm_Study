#include<iostream>
using namespace std;

int main(){
    int n, i, j, tmp, cnt1=0, cnt2=0;
    cin>>n;

    for(i=2; i<=n; i++){
        tmp = i;
        j = 2;
        while(1){
            if(tmp % j == 0){
                if(j == 2) cnt1++;
                else if(j == 5) cnt2++;
                tmp = tmp / j;
            }
            else j++;
            if(tmp == 1) break;
        }
    }

    if(cnt1 < cnt2) cout<<cnt1;
    else cout<<cnt2;

    return 0;
}