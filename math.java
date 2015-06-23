import java.io.*;

public class math {
	public static void main(String [] args)throws IOException{
	   BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
	   float a,b;
	   float sum,subtract, quotient ,product ;
	   System.out.println("Please enter: a");
	   a=Float.parseFloat(br.readLine());
	   System.out.println("Please enter: b");
	   b=Float.parseFloat(br.readLine());
	   sum=a+b;
	   subtract=a-b;
	    quotient =a/b;
	   product =a*b;
	   System.out.printf("Sum:      %9.2f\n"
						+"Subtract  %9.2f\n"
						+"Quotient  %9.2f\n"
						+"Product   %9.2f\n",sum,subtract, quotient ,product );
		
	}}
