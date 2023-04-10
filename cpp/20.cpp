#include<iostream>
using namespace std;

int a[100], b[100];
int main(){
    int i, n;
    cin>>n;

    for(i=0; i<n; i++){
        cin>>a[i];
    }
    for(i=0; i<n; i++){
        cin>>b[i];
    }

    for(i=0; i<n; i++){
        if(a[i] == b[i]) cout<<"D\n";
        else if(a[i] == 1 && b[i] == 2) cout<<"B\n";
        else if(a[i] == 2 && b[i] == 3) cout<<"B\n";
        else if(a[i] == 3 && b[i] == 1) cout<<"B\n";
        else cout<<"A\n";
    }

    return 0;
}