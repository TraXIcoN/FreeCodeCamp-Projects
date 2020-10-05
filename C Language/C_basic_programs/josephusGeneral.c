/*
Developer: Sahil Bairagi(Sahil-k1509)
About problem: There are n people in a circle. Starting from 1. He kills the next mth person and passed sword to m+1 either clockwise or anticlockwise. Process continues until only one person is left.
*/

#include <stdio.h>

int findSoldier(int n, int m, int dir);

int main()
{
    int n, m, dir, answer;
    
    printf("Enter the number of soldiers(n): ");
    scanf("%d", &n);
    
    printf("Enter the number of steps(m): ");
    scanf("%d", &m);
    
    printf("Enter the direction(1 for clockwise, 0 for anti): ");
    scanf("%d", &dir);
    
    answer = findSoldier(n, m, dir);
    
    printf("Soldier Chosen is number %d", answer);
}


int findSoldier(int n, int m, int dir){
    
    int arrayOfSoldiers[n];
    
    // if direction is anticlockwise, we create a reversed array and start from last index.
    for (int i=0; i<n; i++) {   
       arrayOfSoldiers[i] =  dir == 1 ? i+1 : n-i;
    }
    int currentIndex = dir == 1 ? 0 : n-1;
    
    int soldiersLeft = n;
    while (soldiersLeft > 1){
        for (int i=0; i<m-1; i++){
            currentIndex = (currentIndex+1)%n; 
            
            // if present soldier is out of counting, skip that index until a valid soldier is found.
            if (arrayOfSoldiers[currentIndex] == -1){
                while (arrayOfSoldiers[currentIndex] == -1){
                    currentIndex = (currentIndex+1)%n;
                }
            }
        }
        
        arrayOfSoldiers[currentIndex] = -1; // present soldier is set to -1 and is out of counting for next rounds.
        
        // find the next soldier from which counting should start
        currentIndex = (currentIndex+1)%n;
        if (arrayOfSoldiers[currentIndex] == -1){
            while (arrayOfSoldiers[currentIndex] == -1){
                currentIndex = (currentIndex+1)%n;
            }
        }
        
        // number of soldiers is decreased as one soldier is counted out.
        soldiersLeft--;
    }
    
    // Check the final array to find the remaining soldier
    for (int i=0; i<n; i++){
        if (arrayOfSoldiers[i]!= -1){
            currentIndex = i;
            break;
        }
    }
    return arrayOfSoldiers[currentIndex];
    
}
