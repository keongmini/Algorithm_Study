#include<iostream>
using namespace std;

int main(){
    int i, j, n, num, answer, sum=0;
    cin>>n;

    for(i=0; i<n; i++){
        cin>>num>>answer;

        for(j=1; j<=num; j++){
            sum+=j;
        }

        if(sum == answer){
            cout<<"YES\n";
        }else cout<<"NO\n";

        sum = 0;

    }

    return 0;
}