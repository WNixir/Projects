package snake;

import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.util.Random;
import javax.swing.ImageIcon;
import javax.swing.JPanel;
import javax.swing.Timer;

public class Gameplay extends JPanel implements KeyListener, ActionListener {

  private int[] snakeXLength = new int[750];
  private int[] snakeYLength = new int[750];
  private int snakeLength = 2;

  private int moves = 0;
  private boolean left = false;
  private boolean right = false;
  private boolean up = false;
  private boolean down = false;

  private ImageIcon titleImage;
  private ImageIcon snakeImage;
  private ImageIcon leftMouth;
  private ImageIcon rightMouth;
  private ImageIcon upMouth;
  private ImageIcon downMouth;
  private ImageIcon enemy;

  private Timer timer;
  private int delay = 100;

  private int[] enemyXPos = {25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375,
      400, 425, 450, 475, 500, 525, 550, 575, 600, 625, 650, 675, 700, 725, 750, 775, 800, 825};
  private int[] enemyYPos = {100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375,
      400, 425, 450, 475, 500, 525, 550, 575, 600, 625};
  private Random enemyPos = new Random();
  private int xPos = enemyPos.nextInt(34);
  private int yPos = enemyPos.nextInt(23);

  public Gameplay() {
    addKeyListener(this);
    setFocusable(true);
    setFocusTraversalKeysEnabled(false);
    timer = new Timer(delay, this);
    timer.start();
  }

  public void paint(Graphics graphics) {

    // set the default position of snake
    if (moves == 0) {
      snakeXLength[1] = 50;
      snakeXLength[0] = 75;

      snakeYLength[1] = 100;
      snakeYLength[0] = 100;
    }

    // draw title image border
    graphics.setColor(Color.white);
    graphics.drawRect(24, 10, 851, 55);

    // draw title image
    titleImage = new ImageIcon(
        "/Users/wangrixin/Dropbox/Projects/Java/2DSnake/src/assets/snaketitle.jpg");
    titleImage.paintIcon(this, graphics, 25, 11);

    // draw border for play area
    graphics.setColor(Color.white);
    graphics.drawRect(24, 74, 851, 577);

    // draw background
    graphics.setColor(Color.black);
    graphics.fillRect(25, 75, 850, 575);

    // draw snake
    rightMouth = new ImageIcon(
        "/Users/wangrixin/Dropbox/Projects/Java/2DSnake/src/assets/rightmouth.png");
    rightMouth.paintIcon(this, graphics, snakeXLength[0], snakeYLength[0]);

    for (int i = 0; i < snakeLength; i++) {
      if (i == 0 && right) {
        rightMouth = new ImageIcon(
            "/Users/wangrixin/Dropbox/Projects/Java/2DSnake/src/assets/rightmouth.png");
        rightMouth.paintIcon(this, graphics, snakeXLength[i], snakeYLength[i]);
      } else if (i == 0 && left) {
        leftMouth = new ImageIcon(
            "/Users/wangrixin/Dropbox/Projects/Java/2DSnake/src/assets/leftmouth.png");
        leftMouth.paintIcon(this, graphics, snakeXLength[i], snakeYLength[i]);
      } else if (i == 0 && up) {
        upMouth = new ImageIcon(
            "/Users/wangrixin/Dropbox/Projects/Java/2DSnake/src/assets/upmouth.png");
        upMouth.paintIcon(this, graphics, snakeXLength[i], snakeYLength[i]);
      } else if (i == 0 && down) {
        downMouth = new ImageIcon(
            "/Users/wangrixin/Dropbox/Projects/Java/2DSnake/src/assets/downmouth.png");
        downMouth.paintIcon(this, graphics, snakeXLength[i], snakeYLength[i]);
      } else if (i != 0) {
        snakeImage = new ImageIcon(
            "/Users/wangrixin/Dropbox/Projects/Java/2DSnake/src/assets/snakeimage.png");
        snakeImage.paintIcon(this, graphics, snakeXLength[i], snakeYLength[i]);
      }
    }
    enemy = new ImageIcon("/Users/wangrixin/Dropbox/Projects/Java/2DSnake/src/assets/enemy.png");
    if ((enemyXPos[xPos] == snakeXLength[0]) && (enemyYPos[yPos] == snakeYLength[0])) {
      snakeLength++;
      xPos = enemyPos.nextInt(34);
      yPos = enemyPos.nextInt(23);
    }
    enemy.paintIcon(this, graphics, enemyXPos[xPos], enemyYPos[yPos]);

    for (int i = 1; i < snakeLength; i++) {
      if ((snakeXLength[i] == snakeXLength[0]) && (snakeYLength[i] == snakeYLength[0])) {
        right = false;
        left = false;
        up = false;
        down = false;

        graphics.setColor(Color.white);
        graphics.setFont(new Font("arial", Font.BOLD, 50));
        graphics.drawString("Game Over", 300, 300);
      }
    }
    graphics.dispose();
  }

  @Override
  public void actionPerformed(ActionEvent e) {
    timer.start();

    if (right) {
      for (int r = snakeLength - 1; r >= 0; r--) {
        snakeYLength[r + 1] = snakeYLength[r];
      }
      for (int r = snakeLength - 1; r >= 0; r--) {
        if (r == 0) {
          snakeXLength[r] = snakeXLength[r] + 25;
        } else {
          snakeXLength[r] = snakeXLength[r - 1];
        }
        if (snakeXLength[r] > 850) {
          snakeXLength[r] = 25;
        }
      }
      repaint();
    }

    if (left) {
      for (int r = snakeLength - 1; r >= 0; r--) {
        snakeYLength[r + 1] = snakeYLength[r];
      }
      for (int r = snakeLength - 1; r >= 0; r--) {
        if (r == 0) {
          snakeXLength[r] = snakeXLength[r] - 25;
        } else {
          snakeXLength[r] = snakeXLength[r - 1];
        }
        if (snakeXLength[r] < 25) {
          snakeXLength[r] = 850;
        }
      }
      repaint();
    }

    if (up) {
      for (int r = snakeLength - 1; r >= 0; r--) {
        snakeXLength[r + 1] = snakeXLength[r];
      }
      for (int r = snakeLength - 1; r >= 0; r--) {
        if (r == 0) {
          snakeYLength[r] = snakeYLength[r] - 25;
        } else {
          snakeYLength[r] = snakeYLength[r - 1];
        }
        if (snakeYLength[r] < 75) {
          snakeYLength[r] = 625;
        }
      }
      repaint();
    }

    if (down) {
      for (int r = snakeLength - 1; r >= 0; r--) {
        snakeXLength[r + 1] = snakeXLength[r];
      }
      for (int r = snakeLength - 1; r >= 0; r--) {
        if (r == 0) {
          snakeYLength[r] = snakeYLength[r] + 25;
        } else {
          snakeYLength[r] = snakeYLength[r - 1];
        }
        if (snakeYLength[r] > 625) {
          snakeYLength[r] = 75;
        }
      }
      repaint();
    }
  }

  @Override
  public void keyTyped(KeyEvent e) {
  }

  @Override
  public void keyPressed(KeyEvent e) {

    if (e.getKeyCode() == KeyEvent.VK_SPACE) {
      moves = 0;
      snakeLength = 2;
      repaint();
    }

    if (e.getKeyCode() == KeyEvent.VK_RIGHT) {
      moves++;
      right = true;
      if (!left) {
        right = true;
      } else {
        right = false;
        left = true;
      }
      up = false;
      down = false;
    }

    if (e.getKeyCode() == KeyEvent.VK_LEFT) {
      moves++;
      left = true;
      if (!right) {
        left = true;
      } else {
        left = false;
        right = true;
      }
      up = false;
      down = false;
    }

    if (e.getKeyCode() == KeyEvent.VK_UP) {
      moves++;
      up = true;
      if (!down) {
        up = true;
      } else {
        up = false;
        down = true;
      }
      right = false;
      left = false;
    }

    if (e.getKeyCode() == KeyEvent.VK_DOWN) {
      moves++;
      down = true;
      if (!up) {
        down = true;
      } else {
        down = false;
        up = true;
      }
      right = false;
      left = false;
    }
  }

  @Override
  public void keyReleased(KeyEvent e) {
  }

}
