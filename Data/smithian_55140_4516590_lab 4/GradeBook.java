import java.util.Scanner;										// imports the scanner class

public class GradeBook {										// declares GradeBook class
	static Scanner input = new Scanner(System.in);				// declares scanner class and makes it static
		static int exams = 0;									
		static int[] examArray; 
		static int quizzes = 0;
		static int[] quizArray;
		static int labs = 0;
		static int[] labArray;
		
	public static void main(String[] args) {					// declares main method, starts by assigning variables for number of exams quizzes and labs
		System.out.println("How many exams?");
		 exams += input.nextInt();
		
		examArray = new int[exams];
		System.out.println("How many quizzes?");
		 quizzes += input.nextInt();
		
		quizArray = new int[quizzes];
		System.out.println("How many labs?");
		 labs += input.nextInt();
		
		labArray = new int[labs];
		captureGrades();										// calls captureGrades method
		calculateAverage();										// calls calculateAverage method
	}
		
	public static void captureGrades() {									// declares captureGrades method, this method prompts the user to enter the grades for the number of exams quizzes and labs that where determined previously in the main method
		int a = 0;
		int b = 0;
		int c = 0;
		while(exams != a) {													// loop asks to enter the grade for exams until the number of grades entered equals the specified number for exams
			System.out.println("Enter exam grade #" + (a + 1) + ":");
			examArray[a] = input.nextInt();
			a++;}
		
		while(quizzes != b) {												// loop asks to enter the grade for quizzes until the number of grades entered equals the specified number of quizzes
			System.out.println("Enter quiz grade #"+ (b + 1) + ":");
			quizArray[b] = input.nextInt();
			b++;}
		
		while(labs != c) {													// loop asks to enter the grade for labs until the number of grades entered equals the specified number of labs
			System.out.println("Enter lab grade #"+ (c + 1) + ":");
			labArray[c] = input.nextInt();
			c++;}
	}
	
	public static void calculateAverage() {							// declares calculateAverage method, this calculates the average of the grades enterd
		int examSum = 1;
		double examAvg = 1;
		double quizAvg = 1;
		double labAvg = 1;
		for( int a1 : examArray) {									// takes the sum of the exam grades
			examSum += a1;
		}
		
		examAvg += examSum / exams  ;
		int quizSum = 1;
		for(int b1 : quizArray) {									// takes the sum of the quiz grades
			quizSum += b1;
		}
		
		quizAvg += quizSum / quizzes;
		int labSum = 1;
		for(int c1 : labArray) {									// takes the sum of the lab grades
			labSum += c1;
		}
		labAvg += labSum / labs;
		
		System.out.printf("%s %.2f \n", "Exam average: ", examAvg);
		System.out.printf("%s %.2f \n", "Quiz average: ", quizAvg);
		System.out.printf("%s %.2f \n", "Lab average: ", labAvg);
	}
	
}
