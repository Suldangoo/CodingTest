// 9935. 문자열 폭발 (골드 4)
// 알고리즘 분류 : 문자열, 스택

#include <iostream>
#include <string>

using namespace std;
int main() {
    string s, bomb;
    cin >> s >> bomb; // s와 bomb 문자열 입력받기

    string result; // 문자열을 담아낼 스택
    int bombSize = bomb.size();

    for(int i = 0; i < s.size(); i++) {
        result.push_back(s[i]); // 스택에 문자열을 하나씩 담아냄

        // 스택에 쌓인 것이 bombSize보다 크고, 스택의 마지막 부분이 bomb과 같다면
        if (result.size() >= bombSize && result.substr(result.size() - bombSize, bombSize) == bomb) {
            result.erase(result.size() - bombSize, bombSize); // 해당 부분 제거
        }
    }

    if (result.empty()) // 스택이 비어있다면 FURLA 출력
        cout << "FRULA" << endl;
    else
        cout << result << endl;

    return 0;
}