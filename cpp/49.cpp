#include<iostream>
using namespace std;

int a[11][11], b[11];

int main(){
    int n, i, j, sum=0;
    cin>>n;

    for(i=1;i<=n;i++){
        cin>>b[i];
    }

    for(i=1;i<=n;i++){
        for(j=1;j<=n;j++){
            a[j][i] = b[i];     // 열 기준 - j먼저
        }
    }

    for(i=n;i>=1;i--){      // 거꾸로
        cin>>b[i];
    }

    for(i=1;i<=n;i++){
        for(j=1;j<=n;j++){
            if(a[i][j] > b[i]){
                a[i][j] = b[i];
            }
        }
    }

    for(i=1;i<=n;i++){
        for(j=1;j<=n;j++){
            sum += a[i][j];
        }
    }
    
    cout<<sum;

    return 0;
}