import java.util.*;

class Solution {
    final char FILE = '#';
    int minRow, minCol;
    int maxRow, maxCol;
        
    public int[] solution(String[] wallpaper) {
        minRow = minCol = Integer.MAX_VALUE;
        maxRow = maxCol = Integer.MIN_VALUE;
        
        for(int i=0; i<wallpaper.length; i++){
            for(int j=0; j<wallpaper[0].length(); j++){
                if(wallpaper[i].charAt(j) == FILE){
                    if(i < minRow) {
                        minRow = i;
                    }
                    if(i + 1 > maxRow) {
                        maxRow = i + 1;
                    }
                    if(j < minCol){
                        minCol = j;
                    }
                    if(j + 1> maxCol){
                        maxCol = j + 1;
                    }
                }
            }
        }
        
        return new int[]{minRow, minCol, maxRow, maxCol};
    }
}
