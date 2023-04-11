#include<iostream>
#include<vector>
using namespace std;

int main(){
    int n, k, i, pos=0, bp=0, cnt=0;
    cin>>n>>k;
    vector<int> p(n+1);

    while(1){
        pos++;

        if(pos > n){
            pos = 1;
        }

        if(p[pos] == 0){
            cnt++;
            if(cnt == k){
                p[pos] = 1;
                cnt = 0;
                bp++;
            }
        }

        if(bp == n-1){
            break;
        }

    }

    for(i=1;i<=n;i++){
        if(p[i] == 0){
            cout<<i;
            break;
        }
    }

    return 0;
}