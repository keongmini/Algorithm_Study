#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(){
    int i, n, prev, tmp, now;
    cin>>n;
    vector<int> a(n);

    cin>>prev;
    for(i=1; i<n; i++){
        cin>>now;
        tmp = abs(now - prev);
        a[tmp] = 1;
        prev = now;
    }

    for(i=1; i<n; i++){
        if(a[i] != 1){
            cout<<"NO\n";
            exit(0);
        }
    }
    
    cout<<"YES\n";

    return 0;
}