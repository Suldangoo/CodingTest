// 프로그래머스 Lv.1 문자열 내 p와 y의 개수

#include <string>
#include <iostream>
using namespace std;

bool solution(string s)
{
    int p = 0, y = 0; // p와 y의 개수
    
    for (char c : s) {
        if (c == 'p' || c == 'P')
            p += 1;
        else if (c == 'y' || c == 'Y')
            y += 1;
    }
    
    return p == y;
}