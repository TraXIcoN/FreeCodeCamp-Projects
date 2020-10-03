// Sudarshan Hiray
// 3rd October 2020
// Given two strings, this program checks if they are anagrams or not ?
// Anagram: An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
// For example, the word anagram can be rearranged into nag a ram, or the word binary into brainy or the word adobe into abode.

import java.util.Arrays;
import java.util.Scanner;

public class CheckAnagrams {

    public static void main(String args[])
    {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Please enter first String");
        String string1 = scanner.next();
        System.out.println("Please enter second String");
        String string2 = scanner.next();

        AnagramChecker anagramChecker = new AnagramChecker();
        boolean isAnagram = anagramChecker.checkAnagramsBySorting(string1, string2);
        System.out.println("Checking by Sorting strings");
        System.out.println(string1 + " and " + string2 + " are " + (isAnagram ? " " : "NOT ") + "ANAGRAMS of each other");

        boolean isAnagram1 = anagramChecker.checkAnagramsByCountingOccurrences(string1, string2);
        System.out.println("Checking by counting Character occurrences in strings");
        System.out.println(string1 + " and " + string2 + " are " + (isAnagram1 ? " " : "NOT ") + "ANAGRAMS of each other");
    }
}

class AnagramChecker{
    public boolean checkAnagramsBySorting(String string1, String string2){

        if (string1.length() != string2.length())
            return false;

        char[] stringArray1 = string1.toLowerCase().toCharArray();
        char[] stringArray2 = string2.toLowerCase().toCharArray();
        // Sort both character arrays
        Arrays.sort(stringArray1);
        Arrays.sort(stringArray2);

        // Compare sorted strings
        for (int i = 0; i < string1.length(); i++)
            if (stringArray1[i] != stringArray2[i])
                return false;

        return true;
    }

    public boolean checkAnagramsByCountingOccurrences(String string1, String string2){

        if (string1.length() != string2.length())
            return false;

        int count1[] = new int[127];
        int count2[] = new int[127];

        char[] stringArray1 = string1.toLowerCase().toCharArray();
        char[] stringArray2 = string2.toLowerCase().toCharArray();

        for (int i = 0; i < stringArray1.length; i++) {
            count1[stringArray1[i]]++;
            count2[stringArray2[i]]++;
        }

        // Iterating through COUNT arrays to verify number of occurrences of each Character.
        for (int i = 0; i < 127; i++)
            if (count1[i] != count2[i])
                return false;

        return true;
    }
}


