#include<iostream>
using namespace std;

int C[20];
int main(){
    int s, n, a, i, j, pos;
    cin>>s>>n;

    for(i=1;i<=n;i++){
        cin>>a;
        pos = -1;
        for(j=0;j<s;j++){
            if(C[j] == a){
                pos = j;
            }
        }

        if(pos == -1){      // Miss
            for(j=s-1;j>=1;j--){
                C[j] = C[j - 1];
            }
        }
        else{               // Hit
            for(j=pos;j>=1;j--){
                C[j] = C[j - 1];
            }
        }
        C[0] = a;
    }

    for(i=0;i<s;i++){
        cout<<C[i]<<" ";
    }

    return 0;
}