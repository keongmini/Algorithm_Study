#include<iostream>
using namespace std;
int a[2001];
int main(){
    int n, k, i, p=0, cnt=0, total=0;
    cin>>n;
    for(i=1;i<=n;i++){
        cin>>a[i];
        total+=a[i];
    }
    cin>>k;
    if(k>=total){
        cout<<"-1\n";
        return 0;
    }

    while(1){
        p++;
        if(p>n) p = 1;

        if(a[p] == 0) continue;
        a[p]--;
        cnt++;

        if(cnt == k){
            break;
        }
    }

    while(1){
        p++;
        if(p>n) p = 1;
        
        if(a[p] != 0) break;
    }

    cout<<p;


    return 0;
}