import java.util.Random;				// import class scanner

public class RedBlueDice {				// declares class RedBlueDice
	

    static int[] blueDice = new int[3];		//sets static array for blue dice
	static int[] redDice = new int[3];		// sets static array for red dice
	
	static int blueSum = 0;					// declares sum of blue dice array 
	
	
	static int redSum = 0;					//declares sum of red dice array
	static int counter = 0;					// declares the counter mechanism and sets it to 0
	
	
	public static void main(String[] args) {		// main method for class
		
		rollBlue();									//calls rollBlue method 
		
		
		while(redSum != blueSum) {					// loops between rollRed method, showDice method and compareDice method until the sums equal
			rollRed();
			showDice();
			compareDice();
			counter++;
			
			if(redSum == blueSum){					// once the sums equal eachother it presents the closing statment
				System.out.println("It took "+ counter +" rolls to match the sums of the red and blue dice");
				break;
			}else{								// if sums do not equal eachother than it calls rollRed and gives new random numbers
				rollRed();
				continue;}
		}
		
		
		
		
	}
	
	public static void rollBlue() {							// declares rollBlue method, used to assign random intergers in blueArray
		Random b1 = new Random();
		Random b2 = new Random();
		Random b3 = new Random();
		int upperbound = 7;
		blueDice[0] = b1.nextInt(upperbound);
		blueDice[1] = b2.nextInt(upperbound);
		blueDice[2] = b3.nextInt(upperbound);
		blueSum = (blueDice[0]+blueDice[1]+blueDice[2]);
	
	}
	
	public static void rollRed() {							// declares rollRed method, used to assign random intergers in redArray
		
		Random r1 = new Random();
		Random r2 = new Random();
		Random r3 = new Random();
		int upperbound = 7;
		redDice[0] = r1.nextInt(upperbound);
		redDice[1] = r2.nextInt(upperbound);
		redDice[2] = r3.nextInt(upperbound);
		redSum = (redDice[0]+redDice[1]+redDice[2]);
			
		}
				
	public static void showDice() {							// declares showDice method, prints all the information related to the dice 
		while(redSum != blueSum) {							// makes the print statment reprint itself with new red dice variables as long as the sums do not equal
			System.out.printf("%s %2d %1d %1d %s %2d %s %s %2d %1d %1d %s %2d %s\n","Blue dice:",blueDice[0],blueDice[1],blueDice[2],"(sum: ", blueSum,")","Red dice:",redDice[0], redDice[1], redDice[2], "(sum: ",redSum,")");
		counter +=1;
			rollRed();	
			
		}
		
	}
	
	public static boolean compareDice() {					// declares compareDice method, this method checks wheter the sums equal eachother
		if(redSum == blueSum) {
			return true;
		}
		else {
		return false;
		}
		}
	}
