#include <iostream>
#include <string>
#include <queue>
using namespace std;

int n, m;
int map[101][101];
int visited[101][101];
int result[101][101];

int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

int main(){
    cin>>n>>m;
    for(int i=0; i<n; i++){
        string str;
        cin>>str;
        for(int j=0; j<str.size(); j++){
            map[i][j] = str[j] - '0';
        }
    }

    queue<pair<int,int>> q;
    q.push({0, 0});
    visited[0][0] = 1;
    result[0][0] = 1;

    while (!q.empty()){
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for(int i=0; i<4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];

            if(nx < 0 || nx >= n || ny < 0 || ny >= m){
                continue;
            }

            if(visited[nx][ny] == 1 || map[nx][ny] == 0){
                continue;
            }

            visited[nx][ny] = 1;
            result[nx][ny] = result[x][y] + 1;
            q.push({nx, ny});

        }

    }

    cout<<result[n-1][m-1];




    return 0;
}