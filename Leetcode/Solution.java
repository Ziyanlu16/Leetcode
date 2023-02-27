public class App {
    public static void main(String[] args) throws Exception {
        System.out.println(expandFormMiddle(args[0]));
    }

    public  static boolean expandFormMiddle(String s){
        int left;
        int right;
        int n = s.length();
        if (s.length()%2 == 0){
             left = n/2 - 1;
             right = n/2;
        }else{
            left = right = (n - 1) / 2;
        }
        if(s == null || left > right) return false;

        while(left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)){
            left --;
            right ++;
            if (left == 0 && right == s.length() - 1) {
                return true;
           }
        }
    return false;
    }
}
