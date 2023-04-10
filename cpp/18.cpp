#include<iostream>
using namespace std;

int main(){
    int n, m, num, i, cnt=0, result=0;
    cin>>n>>m;

    for(i=0;i<n;i++){
        cin>>num;

        if(num > m){
            cnt++;
        }else{
            result = max(result, cnt);
            cnt = 0;
        }
    }
    
    if(result == 0){
        cout<<-1;
    }else cout<<result;

    return 0;
}