#define TEST_TIMES 1
#define N 5000
#define T 100
#define MIN_T 0.00001
#define COOLING 0.9999

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
#include <stdlib.h>
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

int * n_queen(int n){
  int *a = new int[n];
  for(int i=0;i<n;i++)
    a[i] = i+1;
  unsigned seed = chrono::system_clock::now().time_since_epoch().count();
  srand(seed);
  shuffle(a, a + n,default_random_engine(seed));
  int cur_conflict = conflict(a, n);
  float t = T;

  ofstream out("../intervals.npy");
  ofstream out2("../probabilities.npy");
  ofstream out3("../thresholds.npy");

  int backward_times=0;
  int iterate_times=0;
  int last_backward_time = 0;
  while(true){
    cout << cur_conflict << endl;
    while(true){
      int i = rand() % N;
      int j = rand() % N;
      int* temp = new int[n];
      memcpy(temp, a, n*sizeof(int)); // 注意这里应以字节为单位

      int before_conflict = partial_conflict(temp, n, i, j);
      swap(temp[i], temp[j]);
      int after_conflict = partial_conflict(temp, n, i, j);

      // 计算采用采用坏的排列的概率
      float threshold = min(exp(float(before_conflict - after_conflict) / t), (float)1);
      float p = (float)rand()/RAND_MAX;
      out3 << threshold << endl;
      // 如果新的排列冲突更小，一定选择它，否则以上面计算的概率选择它
      if(after_conflict<before_conflict || p<=threshold){
	iterate_times += 1;
	if(after_conflict<before_conflict && p<=threshold){
	  backward_times += 1;	// 记录采用坏的排列的次数
	  
	  out << iterate_times - last_backward_time << endl; // 记录两次采用坏的排列的间隔
	  out2 << (float) backward_times / (float) iterate_times << endl;

	  last_backward_time = iterate_times;
	}
	int c = cur_conflict + (after_conflict - before_conflict);
	if(c==0 && conflict(temp,n)==0)
	  return temp;
	free(a);		// 防止内存泄露
	a = temp;		// 更新排列
	cur_conflict = c;	// 更新当前冲突
	t *= COOLING;		// 更新温度
	if(t<=MIN_T){		// 如果温度过低还没法找到解，视为陷入局部最优，重新开始算法
	  shuffle(a, a + n,default_random_engine(seed));
	  t = T;
	  cur_conflict = conflict(a,n);
	}
	break;
      }else
	free(temp);
    }
  }
}

int main(){
  const time_t a = time(NULL);
  for(int i=0;i<TEST_TIMES;i++){
    int * result = n_queen(N);
    cout << i << "---------------" << endl;
    const time_t b = time(NULL);
    cout << b-a << "/" << (i+1) << endl;
  }
  return 0;
}
// 效率与完全随机的算法类似，速度稍慢
