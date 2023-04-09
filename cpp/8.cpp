#include<iostream>
using namespace std;

int main(){
    char a[100];
    int i, cnt=0;
    cin>>a;

    for(i=0; a[i]!='\0'; i++){
        if(a[i]=='(') cnt++;
        else if(a[i]==')') cnt--;

        if(cnt<0) break;
    }

    if(cnt == 0) cout<<"YES\n";
    else cout<<"NO\n";

    return 0;
}