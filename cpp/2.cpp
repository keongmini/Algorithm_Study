#include<iostream>
using namespace std;
int main(){
    int a, b, i, sum = 0;
    cin>>a>>b;

    for(i = a; i < b; i++){
        cout<<i<<" + ";
        sum = sum + i;
    }
    cout<<b<<" = ";
    cout<<sum+b;

    return 0;
}