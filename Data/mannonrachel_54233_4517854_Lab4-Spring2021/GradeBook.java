import java.util.Scanner;
public class GradeBook
{

public static void main(String[] args)
{
Scanner input = new Scanner(System.in);

System.out.println("Welcome to the CS Gradebook\n");

System.out.print("How many exams? ");
int x = input.nextInt();
int[] examGrades = new int[x];

System.out.print("How many quizzes? ");
x = input.nextInt();
int[] quizGrades = new int[x];

System.out.print("How many lab assignments? ");
x = input.nextInt();
int[] labGrades = new int[x];


captureGrades("exam",examGrades);
captureGrades("quiz",quizGrades);
captureGrades("lab",labGrades);
System.out.printf("Exam average: %5.2f\n", calculateAverage(examGrades));
System.out.printf("Quiz average: %5.2f\n", calculateAverage(quizGrades));
System.out.printf("Lab average: %5.2f\n", calculateAverage(labGrades));

}//end main

public static void captureGrades (String gradeType, int[] grades)
{
Scanner input = new Scanner(System.in);
//System.out.printf("Enter %s %d grades:\n",gradeType,grades.length);
for(int i = 0; i < grades.length; i++)
  {
    System.out.printf("Enter %s grade #%d: ",gradeType,(i + 1));
    grades[i] = input.nextInt();
  }

}//end captureGrades

public static double calculateAverage(int[] grades)
{
  int sum = 0;
  for(int i =  0; i < grades.length; i++)
     sum += grades[i];
  double average = (double) sum / grades.length;
  return average; 
}

}//end Gradebook