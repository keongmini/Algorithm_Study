#include<iostream>
#include<string>

using namespace std;

int main(){
    string str;
    cin>>str;

    int result = 0;

    string num;
    bool isMinus = false;

    for(int i=0; i<= str.size(); i++){
        if(str[i] == '-' || str[i] == '+' || i == str.size()){
            if(isMinus){
                result -= stoi(num);
                num = "";
            }else{
                result += stoi(num);
                num = "";
            }
        }else{
            num += str[i];
        }

        if(str[i] == '-'){
            isMinus = true;
        }
    }

    cout<<result;


    return 0;
}