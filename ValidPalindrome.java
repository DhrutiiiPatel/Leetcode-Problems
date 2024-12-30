class Solution {
    public boolean isPalindrome(String s) {

        String r = "";

        for (char c : s.toCharArray()){
            if( Character.isDigit(c) || Character.isLetter(c)){
                r += c;
            }
        }
        
        r = r.toUpperCase();

        int a=0;
        int b=r.length()-1;
        while (a <= b){
        if (r.charAt(a) != r.charAt(b)){
            return false;
        }
        a +=1;
        b -=1;
      }

        return true;
    }

}
