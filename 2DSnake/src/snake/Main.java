package snake;

import java.awt.Color;
import javax.swing.JFrame;

public class Main {

  public static void main(String[] args) {
    JFrame mainFrame = new JFrame();
    Gameplay gameplay = new Gameplay();

    mainFrame.add(gameplay);
    mainFrame.setBounds(10, 10, 905, 700);
    mainFrame.setBackground(Color.DARK_GRAY);
    mainFrame.setResizable(false);
    mainFrame.setVisible(true);
    mainFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
  }

}
