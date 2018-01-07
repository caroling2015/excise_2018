package jmt;

import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class first {
	public static void main(String[] args){
		
		System.out.print(getvaluecode("code"));

	}
	
	public static String getvaluecode(String input){
		String pattern = "\\d{6}";		
		Pattern r = Pattern.compile(pattern);
		Matcher m=r.matcher(input);
		if(m.find()){
			return m.group(0);			
		}else{
			return "no match";
		}
	}

}
