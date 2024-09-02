// 26069. 붙임성 좋은 총총이 (실버 4)
// 알고리즘 분류 : 해시를 사용한 집합과 맵

#include <iostream>
#include <string>
#include <map>

using namespace std;

int main() {
    int N;
    cin >> N; // 맵의 크기를 입력받음

    map<string, bool> m; // N 크기의 맵 생성
    m["ChongChong"] = true; // ChongChong은 Ture인 상태로 삽입

    for (int i = 0; i < N; i++) {
        string a, b;
        bool check = false;
        cin >> a >> b;

        // A나 B가 맵에 있고, true인지 확인
        if (m.find(a) != m.end()) {
            if (m[a]) {
                check = true;
            }
        }
        if (m.find(b) != m.end()) {
            if (m[b]) {
                check = true;
            }
        }

        // true가 한 명이라도 있으면 모두 true
        if (check) {
            m[a] = true;
            m[b] = true;
        }
        else {
            m[a] = false;
            m[b] = false;
        }
    }

    int answer = 0;

    // 맵에 저장된 사람들 중 true인 사람들의 수를 측정
    for (const auto &pair : m)
        if (pair.second == true)
            answer++;

    cout << answer << endl;

    return 0;
}