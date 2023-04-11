#include<iostream>
using namespace std;

int a[10][10];

int main(){
    int i, j, sum, ave, min, tmp, result;
    for(i=1;i<=9;i++){
        sum=0;
        for(j=1;j<=9;j++){
            cin>>a[i][j];
            sum+=a[i][j];
        }
        ave = (sum/9.0) + 0.5;      // 반올림
        cout<<ave<<" ";
        min=2147000000;
        for(j=1;j<=9;j++){
            tmp = abs(a[i][j] - ave);
            if(tmp<min){
                min=tmp;
                result = a[i][j];
            }
            else if(tmp == min){
                if(a[i][j] > result){
                    result = a[i][j];
                }
            }
        }
        cout<<result<<"\n";
    }

    return 0;
}