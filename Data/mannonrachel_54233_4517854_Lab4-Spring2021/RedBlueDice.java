//Rachel Mannon 48276128
//Lab 4 - Spring 2021
import java.util.Random;
public class RedBlueDice {
	/* static variables: int array containing three blue die values
	int array containing three red die values
	int containing the sum of the blue dice (initialize to 0)
	int containing the sum of the red dice (initialize to 0)
	Variable containing instance of java.util.Random (this requires an import statement) */

	static int[] blueArray = new int[3];
	static int[] redArray = new int[3];
	static int bluesum = 0;
	static int redsum = 0;
	static Random rand = new Random();

	public static void main(String[] args) {
	//Call rollBlue method
	//Declare and initialize roll counter variable to track the number of rolls required to match
	//Call rollRed method
	//Call showDice method
	rollBlue();
	int counter = 0;
	rollRed();
	showDice(blueArray, bluesum);

	//Call compareDice method
	//If it returns true, break out of the loop
	//If it returns false, increment the counter loop
	compareDice(bluesum);
		for(counter = 1; counter > 0; ++counter) {
			if(compareDice(bluesum) == true) {
				break;
			} else {
				counter++;
			} }

			//Print a message showing the total number of rolls it took to get matching sums*/
			System.out.printf("\n%s%d%s", "It took ", counter, " roll(s) to match the sum of the red and blue dice.");
		
	} 

	public static void rollBlue(){
	/*Generate three random roll values (range 1-6) and store each in the blue die values array
	Sum the three values and save in the variable containing the sum of the blue dice */
	int blue1 = rand.nextInt(6) + 1;
	int blue2 = rand.nextInt(6) + 1;
	int blue3 = rand.nextInt(6) + 1;
	blueArray[0] = blue1;
	blueArray[1] = blue2;  
	blueArray[2] = blue3; 
	int bluesum = blue1+blue2+blue3;
	compareDice(bluesum);
	}
	
	public static void rollRed(){
	/* Generate three random roll values (range 1-6) and store each in the red die values array
	Sum the three values and save in the variable containing the sum of the red dice */

	int red1 = rand.nextInt(6) + 1; 
	int red2 = rand.nextInt(6) + 1;
	int red3 = rand.nextInt(6) + 1;
	redArray[0] = red1;
	redArray[1] = red2;  
	redArray[2] = red3;
	int redsum = red1+red2+red3;
	showDice(redArray, redsum);

	}
	public static void showDice(int[] colorArray, int colorsum){
	/*Print the three blue die values and the blue total and the red die values and the red total.
	(Match the format shown in the sample output on the previous page.)
	MUST USE LOOPS TO RETRIEVE AND PRINT ARRAY VALUES FOR FULL CREDIT */
	System.out.print("Blue Dice: ");
	for(int i = 0; i < blueArray.length; i++) {
				System.out.print(blueArray[i] + " ");}
	System.out.print("(sum: " + bluesum + ") ");
	System.out.print("Red Dice: ");
	for(int i = 0; i < redArray.length; i++) {
				System.out.print(redArray[i] + " ");}
	System.out.print("(sum: " + redsum + ") \n"); 			

	} 

	public static boolean compareDice(int colorsum){
	//Returns true if the blue sum is equal to the red sum, otherwise returns false
	if(bluesum == redsum) {
		return true;
	} else {
		return false;
	}
	
} }