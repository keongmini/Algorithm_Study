#include<iostream>
#include<string>
#include<vector>
#include <queue>
#include<algorithm>

using namespace std;

int n;
int map[26][26];
int visited[26][26];

int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

int bfs(int x, int y){
    queue<pair<int, int>> q;
    q.push({x, y});
    visited[x][y] = 1;

    int result = 1;

    while(!q.empty()){
        int a = q.front().first;
        int b = q.front().second;
        q.pop();

        for(int i=0; i<4; i++){
            int nx = a + dx[i];
            int ny = b + dy[i];

            if(nx < 0 || nx >= n || ny < 0 || ny >= n){
                continue;
            }

            if(visited[nx][ny] == 1 || map[nx][ny] == 0){
                continue;
            }

            visited[nx][ny] = 1;
            result ++;
            q.push({nx, ny});
        }
    }

    return result;
}

int main(){
    cin>>n;

    for(int i=0; i<n; i++){
        string str;
        cin>>str;

        for(int j=0; j<n; j++){
            map[i][j] = str[j] - '0';
        }
    }

    vector<int> answer;
    int tmp = 0;

    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            if(visited[i][j] == 0 && map[i][j] == 1){
                answer.push_back(bfs(i, j));
                tmp ++;
            }
        }
    }
    
    if(tmp != 0){
        sort(answer.begin(), answer.end());
    }


    cout<<tmp<<endl;
    for(int i=0; i<answer.size(); i++){
        cout<<answer[i]<<endl;
    }



    return 0;
}