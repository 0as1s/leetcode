#define TEST_TIMES 1
#define N 5000


#include <iostream>
#include <stack>
#include <math.h>
#include <chrono>
#include <algorithm>		// shuffle不是在random里的
#include <random>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <limits.h>
#include <set>
#include <fstream>
using namespace std;
int conflict(int arrange[], int n){
  int total = 0;
  for(int i=0;i<n-1;i++)
    for(int j=i+1;j<n;j++){
      if(j-i == abs(arrange[j]-arrange[i])){
	total++;
      }
    }
  return total;
}

int partial_conflict(int arrange[], int n, int i, int j){
  int total = 0;
  for(int k=0;k<n;k++){
    if(abs(k-i) == abs(arrange[k]-arrange[i]))
	total++;
    if(abs(k-j) == abs(arrange[k]-arrange[j]))
	total++;
  }
  return total;
}

int * initial(int n){
  int * a = new int[n];
  set<int> s= set<int>();
  a[0] = 0;
  s.insert(0);
  for(int i=1;i<n;i++){
    int temp = (a[i-1] + i) % n;
    while(s.find(temp)!=s.end())
      temp = (temp + 3) % n;
    a[i] = temp;
    s.insert(temp);
  }
  return a;
}
int * n_queen(int n){
  int *a = new int[n];
  for(int i=0;i<n;i++)
    a[i] = i+1;
  unsigned seed = chrono::system_clock::now().time_since_epoch().count();
  shuffle(a, a + n,default_random_engine(seed));
  a = initial(n);
  int cur_conflict = conflict(a, n);
  int last_i = 0;
  int last_j = 0;
  while(true){
    bool flag = false;		// flag表示一次迭代中是否找到了冲突更少的排列
    for(int i=1;i<n;i++){
      cout << cur_conflict << endl;
      int temp_i = (last_i + i) % n;
      for(int j=1;j<n;j++){
	int temp_j = (last_j + j) % n;
	if(temp_i==temp_j)
	  continue;

	int* temp = new int[n];
	memcpy(temp, a, n*sizeof(int)); // 注意这里应以字节为单位

	int before_conflict = partial_conflict(temp, n, temp_i,temp_j);
	swap(temp[temp_i], temp[temp_j]);
	int after_conflict = partial_conflict(temp,n,temp_i,temp_j);

	if(after_conflict<before_conflict){
	  int c = cur_conflict + (after_conflict - before_conflict);
	  if(c==0 && conflict(temp,n)==0)
	      return temp;
	  free(a);		// 防止内存泄露
	  a = temp;		// 更新排列
	  cur_conflict = c;	// 更新当前冲突
	  flag = true;
	  last_j = temp_j;
	  break;
	}else
	  free(temp);		// 防止内存泄露
      }
      if(flag){
	last_i = temp_i;
	break;
      }
    }
    if(!flag){			// 陷入局部最优，则重新随机生成a
      a = new int[n];
      for(int i=0;i<n;i++)
	a[i] = i+1;
      unsigned seed = chrono::system_clock::now().time_since_epoch().count();
      shuffle(a, a + n,default_random_engine(seed));
      cur_conflict = conflict(a, n);
      last_i = 0;
      last_j = 0;
    }
  }
}

int main(int argc, char *argv[])
{
  const time_t a = time(NULL);
  ofstream out("../output2.txt");
  out<< "begin" << endl;
  for(int i=0;i<TEST_TIMES;i++){
    int * result = n_queen(N);
    cout << i << "---------------" << endl;
    const time_t b = time(NULL);
    cout << b-a << "/" << (i+1) << endl;
    out << b-a << "/" << (i+1) << endl;
    for(int j=0;j<N;j++){
      cout << result[j] << "\t";
    }
  }
  return 0;
}
// 问题规模：　采用了partial_conflict后的时间　-> 删除了栈后的时间　->　最终版本的时间(N/A表示未测试，大体上是这样，由于一开始没想到会做这么多类型的尝试，可能有些是其他情况的测试结果)　
// 100: 2.25s -> 94/100 -> 2/100
// 200: 45s -> 18.9s -> 6/100
// 300: 315s -> 1293/10 -> 15/100
// 500: N/A -> 20/10(这项数据有点问题，具体是什么情况下测试的记不清了) -> 50/100
// 1000: N/A -> 305/10 -> 314/100
// 5000: N/A ->51254/62 -> 3891/20
