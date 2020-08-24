// Two Methods returning the same functionity, please ensure one class is commented out prior to running


public class Magic8 {
  
    public static void main(String[] args) {
    
      int choice = (int) (Math.random() * 12 + 1);
      
      if (choice == 1) {
        System.out.println("You May Rely On It");
      } else if (choice == 2) {
        System.out.println("Don't Bet On It");
      } else if (choice == 3) {
        System.out.println("You Can Count On It");
      } else if (choice == 4) {
        System.out.println("Focus And Ask Again");
      } else if (choice == 5) {
        System.out.println("Looks Like Yes");
      } else if (choice == 6) {
        System.out.println("Chances Aren't Good");
      } else if (choice == 7) {
        System.out.println("Signs Point to Yes");
      } else if (choice == 8) {
        System.out.println("Most Likely.");
      } else if (choice == 9) {
        System.out.println("Better Not Tell You Now");
      } else if (choice == 10) {
        System.out.println("Yes.");
      } else if (choice == 11) {
        System.out.println("No.");
      } else {
        System.out.println("Maybe.");
      } 
    }
  }


  public class Magic8 {
  
    public static void main(String[] args) {
    
      int choice = (int) (Math.random() * 12 + 1);
      
      switch (choice) {
        case 1:
            System.out.println("You May Rely On It");
            break;
        case 2:
            System.out.println("Don't Bet On It");
            break;
        case 3:
            System.out.println("You Can Count On It");
            break;
        case 4:
            System.out.println("Focus And Ask Again");
            break;
        case 5:
            System.out.println("Looks Like Yes");
            break;
        case 6:
            System.out.println("Chances Aren't Good");
            break;
        case 7:
            System.out.println("Signs Point to Yes");
            break;
        case 8:
            System.out.println("Most Likely.");
            break;
        case 9:
            System.out.println("Better Not Tell You Now");
            break;
        case 10:
            System.out.println("Yes.");
            break;
        case 11:
            System.out.println("No.");
            break;
        default:
            System.out.println("You May Rely On It");
        }

    }
  }