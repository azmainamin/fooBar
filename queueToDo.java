package com.google.challenges; 

public class Answer {
    public static int answer(int start, int length) {
        /*
        The idea: There is a pattern for each line of workers.
        The first worker of row i and first worker of row i+1 always has a difference of length.
        The last worker of row i and last worker of row i+1 always vary by length -1.
        */
        
        // Edge case when length is 1.
        if(length == 1) return start;
        
        int lower = start;
        int upper = start + length -1;
        int j = 0;
        int answer = 0;
        
        while(j < length){
            for(int i= lower;i<upper + 1; i++){
                answer ^= i;
            }
            lower = lower + length; //First worker of next row varies by length
            upper = upper + length -1; //Last worker of next row varies by length -1
            j++;
        }
        return answer;
    }
}
