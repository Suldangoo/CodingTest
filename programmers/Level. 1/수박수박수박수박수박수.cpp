// 프로그래머스 Lv.1 수박수박수박수박수박수?

#include <string>

using namespace std;

string solution(int n) {
    string S = "";

    for (int i = 0; i < n; i++) {
        if (i % 2 == 0) {
            S += "수";
        } else {
            S += "박";
        }
    }

    return S;
}
