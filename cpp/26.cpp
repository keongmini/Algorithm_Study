#include<iostream>
#include<vector>
using namespace std;

int main(){
    int i, j, n;
    cin>>n;
    vector<int> a(n);
    vector<int> result(n, 1);

    for(i=0;i<n;i++){
        cin>>a[i];
        for(j=i-1; j>=0; j--){
            if(a[i] < a[j]){
                result[i]++;
            }
        }

        cout<<result[i]<<" ";
    }

    return 0;
}