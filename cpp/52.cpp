#include<iostream>
using namespace std;
int a[1501];
int main(){
    int n, i, p2, p3, p5, min=2147000000;
    cin>>n;
    a[1] = 1;
    p2 = p3 = p5 = 1;
    for(i=2;i<=n;i++){
        if(a[p2] * 2 < a[p3] * 3) min = a[p2] * 2;
        else min = a[p3] * 3;
        if(a[p5]*5 < min) min = a[p5] * 5;

        if(a[p2]*2 == min) p2++;
        if(a[p3]*3 == min) p3++;
        if(a[p5]*5 == min) p5++;
        a[i] = min;
    }

    cout<<a[n];

    return 0;
}