#include <pthread.h> 
#include <stdio.h> 
#include <stdlib.h> 
#include <string.h> 
#include <unistd.h> 
#include<time.h>

time_t current_time;
struct tm * time_info;
char timeString[9];  // space for "HH:MM:SS\0"

int counter; 
int ti;
pthread_mutex_t lock; 

void* fun1(void* arg) 
{ 
    pthread_mutex_lock(&lock); 
  
    unsigned long i = 0; 
    for (i = 0; i < (0xFFFFFFFF); i++) 
      ;
    printf("%c%c%c",timeString[ti],timeString[ti+1],timeString[ti+2]);
    ti += 3;
    pthread_mutex_unlock(&lock); 
  
    return NULL; 
} 

void* fun2(void* arg) 
{ 
    pthread_mutex_lock(&lock); 
  
    unsigned long i = 0;  
  
    for (i = 0; i < (0xFFFFFFFF); i++) 
      ; 
    printf("%c%c%c",timeString[ti],timeString[ti+1],timeString[ti+2]);
    ti += 3;
  
    pthread_mutex_unlock(&lock); 
  
    return NULL; 
}

void* fun3(void* arg) 
{ 
    pthread_mutex_lock(&lock); 
  
    unsigned long i = 0; 
    printf("%c%c%c",timeString[ti],timeString[ti+1],timeString[ti+2]);
    ti += 3;
    pthread_mutex_unlock(&lock); 
  
    return NULL; 
} 
  
int main(void) 
{ 
    int i = 0; 
    int error; 
    pthread_t thread1,thread2,thread3; 
    time(&current_time);
    time_info = localtime(&current_time);

    strftime(timeString, sizeof(timeString), "%H:%M:%S", time_info);
  
    if (pthread_mutex_init(&lock, NULL) != 0) { 
        printf("\n mutex init has failed\n"); 
        return 1; 
    }  
    pthread_create(&thread1,NULL,&fun1,NULL);
    pthread_create(&thread2,NULL,&fun2,NULL);
    pthread_create(&thread3,NULL,&fun3,NULL);

    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);
    pthread_join(thread3, NULL);
    pthread_mutex_destroy(&lock); 
  
    return 0; 
} 