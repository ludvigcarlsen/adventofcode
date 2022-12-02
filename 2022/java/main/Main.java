package main;

import main.Day;

import java.io.IOException;
import java.lang.reflect.InvocationTargetException;

public class Main {    
    public static void main(String[] args) throws InstantiationException, IllegalAccessException, ClassNotFoundException, IOException, InvocationTargetException, NoSuchMethodException {
        
        for (int day = 1; day < 2; day++) {
            System.out.println(String.format("Day %s:", day));
            Day d = (Day) Class.forName("days.Day" + day).getDeclaredConstructor().newInstance();
            d.printParts();
            System.out.println();
        }
    }    
}





