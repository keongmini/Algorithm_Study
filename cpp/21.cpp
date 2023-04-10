#include<iostream>
using namespace std;

int main(){
    int i, A[10], B[10], as=0, bs=0, lw=0;
    for(i=0; i<10; i++){
        cin>>A[i];
    }
    for(i=0; i<10; i++){
        cin>>B[i];
    }
    
    for(i=0; i<10; i++){
        if(A[i] > B[i]){
            as += 3;
            lw = 1;
        }else if(A[i] < B[i]){
            bs += 3;
            lw = 2;
        }else{
            as += 1;
            bs += 1;
        }
    }

    cout<<as<<" "<<bs<<"\n";

    if(as > bs) cout<<"A";
    else if(as < bs) cout<<"B";
    else{
        if(lw == 0){
            cout<<"D";
        }else if(lw == 1){
            cout<<"A";
        }else{
            cout<<"B";
        }
    }

    return 0;
}