#include<iostream>
using namespace std;
int a[51][51];

int main(){
    int h, w, n, m, i, j, k, s, sum=0, max=-2147000000;
    cin>>h>>w;
    for(i=1;i<=h;i++){
        for(j=1;j<=w;j++){
            cin>>a[i][j];
        }
    }
    cin>>n>>m;
    for(i=1;i<=h-n+1;i++){
        for(j=1;j<=w-m+1;j++){
            sum=0;
            for(k=i;k<i+n;k++){
                for(s=j;s<j+m;s++){
                    sum+=a[i][j];
                }
            }
            if(sum > max){
                max = sum;
            }
        }
    }
    cout<<max;
    return 0;
}