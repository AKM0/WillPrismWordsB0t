//This program creates a prism from a phrase
//Programmed by AKM
//January 25, 2016 - January 31, 2016

import java.lang.StringBuilder; //used to build string for arguments passed from WillPrismWordsBot.py
import java.io.FileNotFoundException;
import java.io.UnsupportedEncodingException;
import java.io.PrintWriter;
import java.io.File;


public class WillPrismWordsBot {
	
	static String space = "\u3000"; //ideographic space, same width as a fullwidth character
	static String input; //string of args[]
	static int num_of_s; //length of string
	static StringBuilder final_string = new StringBuilder (); //builds string to write to file
	static StringBuilder initial_string = new StringBuilder (); //constructs string from args []
	
	public static void main (String [] args) {

        for (int i = 0; i < args.length; i++) { //builds a string from args[]
			if ((i) >= args.length-1) {
				initial_string = initial_string.append (args[i]);
			} else {
				initial_string = initial_string.append (args[i] + " ");
			}
		}
		
		input = initial_string.toString (); //formats to string
		input = input.toUpperCase ();
		input = format (input); //standarizes input to fullwidth characters
		num_of_s = (input.length()-2); //variable used in loops later

		print_top_half (input); //creates top half of prism
		print_lower_half (input); //creates botton half of prism
		
		PrintWriter writer;
		File out = new File ("out.txt"); //writes end result to file for WillPrismWordsBot.py
		try {
			writer = new PrintWriter (out, "UTF-8");
			writer.print(final_string);
			writer.close ();
		} catch (FileNotFoundException | UnsupportedEncodingException e) {
			e.printStackTrace();
		}

	}
	

	public static String format (String s) { //turns string into fullwidth characters

		String alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890";
		String fullwidth_characters = "ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ　１２３４５６７８９０";
		String unicode_string;

		for (int i = 0; i < s.length(); i++) { //scans through entire string
			for (int k = 0; k < alphabet.length(); k++) { //replaces ASCII character with Unicode fullwidth character
				if (s.charAt(i) == alphabet.charAt(k)) { 
					s = s.replace(s.charAt(i), fullwidth_characters.charAt(k));
				}
			}
		}
		
		unicode_string = s;
		return unicode_string; //returns Unicode string
	
	}
	
	public static void print_top_half (String s) {
			
		for (int w = (s.length()-1); w > 0; w--) { //prints spaces before first horizontal edge
			final_string.append(space);
		}
		
		print_word (s); //prints out first horizontal edge
		final_string.append("\n\n");
		
		for (int i = (num_of_s); i > 0; i--) {
			
			for (int k = i; k > 0; k--) { //space between wall and first diagonal
				final_string.append(space);
			} 
			
			final_string.append(s.charAt(i));
			for (int n = num_of_s; n > 0; n--) { //prints spaces between first and second diagonal
			    final_string.append(space);
			}
			
			final_string.append(s.charAt(i));
			
			for (int c = (num_of_s - i); c > 0; c--) { //prints spaces between second diagonal and vertical edge
				final_string.append(space);
			}
			final_string.append(s.charAt(i));
			final_string.append("\n\n");
		}
	}
	
	public static void print_lower_half (String s) {
		
	    print_word (s); //prints out second horizontal edge
		
		for (int w = num_of_s; w > 0; w--) { //prints spaces before first horizontal edge and outer letter
		    final_string.append(space);
		}
		
		final_string.append(s.charAt(0));
		final_string.append("\n\n");

		for (int i = 1; i < s.length()-1; i++) {
		
			final_string.append(s.charAt(i));
				
			for (int n = num_of_s; n > 0; n--) { //prints spaces between first and second vertical edge
			    final_string.append(space);
			}
		
			final_string.append(s.charAt(i));
				
			for (int c = (num_of_s -i); c > 0; c--) { //prints spaces between second diagonal and vertical edge
				final_string.append(space);
			}
			
			final_string.append(s.charAt(i));
			final_string.append(space);
			final_string.append("\n\n");
				
		}
		print_word (s);
	}
	
	public static void print_word (String s) { // simply prints word without any ideographic spaces
		
		for (int i = 0; i < s.length(); i++) {
			final_string.append(s.charAt(i));
		}
	}
}