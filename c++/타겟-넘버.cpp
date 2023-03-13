#include <string>
#include <vector>

using namespace std;
int dfs(vector<int> numbers, int target, int index, int sum){
	// 종료 조건 : 모두 탐색한 경우 
    if (numbers.size() == index){
        return sum == target ? 1 : 0;
    }
    // sum에 더하기 연산을 한 경우와 빼기 연산을 한 경우를 합함
    else {
        return dfs(numbers, target, index + 1, sum + numbers[index]) + dfs(numbers, target, index + 1, sum - numbers[index]);
    }
}

int solution(vector<int> numbers, int target) {
    return dfs(numbers, target, 0, 0);
}
