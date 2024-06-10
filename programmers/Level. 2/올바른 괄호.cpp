// 프로그래머스 Lv.2 올바른 괄호

#include<string>
#include <iostream>

using namespace std;

bool solution(string s)
{
    int check = 0;
    
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == '(')
            check++;
        else if (s[i] == ')')
            check--;
        
        if (check < 0)
            return false;
    }
    
    return check == 0;
}