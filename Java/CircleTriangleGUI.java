import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Point;
import java.awt.RenderingHints;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.event.MouseMotionListener;
import java.awt.geom.Ellipse2D;
import java.util.ArrayList;
import java.util.List;

import javax.swing.JFrame;
import javax.swing.JPanel;

public class CircleTriangleGUI extends JPanel implements MouseListener, MouseMotionListener{

	private static final long serialVersionUID = 1L; 	// to keep track of version of a class
	private static final int W = 400;					//to set window width
    private static final int H = 300;					//to set window height
	private int a = W / 2;								// main circle x coordinate
    private int b = H / 2;								// main circle y coordinate
    private int r = 100;								// main circle radius
    private int n;										// number of smaller circles (here 3)
    private boolean dragging = false; 
    private int index;
    private int[] polygonXS = new int [3]; 				// x coordinates of all small circles
    private int[] polygonYS = new int [3]; 				// y coordinates of all small circles
    private List<Ellipse2D> circles = new ArrayList<Ellipse2D>();
    private double[] lengths = new double[3];			//stores length (a, b, c) of a triangle
    private double[] angles = new double[3];			//stores angles (A, B, C) of a triangle
    private double error;

    public CircleTriangleGUI(int num) {
    	super(true);
        this.setPreferredSize(new Dimension(W, H));
        this.n = num;
        generateCircles(5); // radius = 5
        this.addMouseListener(this);
		this.addMouseMotionListener(this);
    }

    //generates 'n' circles each with 'radius' at random points on circumference 
    private void generateCircles(int radius) {
    	for(int i = 0; i < n; i++) {
    		double angle = Math.random() * Math.PI * 2;
            int x = (int) Math.round(a + r * Math.cos(angle));
            int y = (int) Math.round(b + r * Math.sin(angle));
            circles.add(new Ellipse2D.Double(x - radius, y- radius, 2 * radius, 2 * radius));
            polygonXS[i] = x;
            polygonYS[i] = y;
    	}
    	
    	//calculates length of all 3 sides
    	for(int i = 0; i < lengths.length; i++) {
			lengths[i] = Math.sqrt(Math.pow((polygonXS[(i + 1) % 3] - polygonXS[(i + 2) % 3]), 2) + Math.pow((polygonYS[(i + 1) % 3] - polygonYS[(i + 2) % 3]), 2));
		}
    	
    	// calculate angles
    	for(int i = 0; i < angles.length; i++) {
			angles[i] = Math.round(Math.toDegrees(Math.acos(((lengths[i % 3] * lengths[i % 3]) - (lengths[(i + 1) % 3] * lengths[(i + 1) % 3]) - (lengths[(i + 2) % 3] * lengths[(i + 2) % 3])) / (-2 * lengths[(i + 1) % 3] * lengths[(i + 2) % 3]))));
		}
    	
    	//find error (There may be small error because of double data type calculation)
    	error = 180 - (angles[0] + angles[1] + angles[2]);
    	
	}

	@Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2d = (Graphics2D) g;
        g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
        g2d.setColor(Color.black);
        g2d.drawLine(a, b, a, b); // draws point
        g2d.drawOval(a - r, b - r, 2 * r, 2 * r); //main circle
        g2d.setColor(Color.red);
        for (Ellipse2D circle : circles) {
            g2d.fill(circle);
        }
        g2d.setColor(Color.black);
        g2d.drawPolygon(polygonXS, polygonYS, n);
        
        for(int i = 0; i < 3; i++) {
        	if(polygonXS[i] >= a && polygonYS[i] <= b) {
        	
        		// point in 1st quadrant
        		g2d.drawString(Double.toString(angles[i]) + "°", polygonXS[i] + 10, polygonYS[i] - 10);
        	
        	}else if(polygonXS[i] >= a && polygonYS[i] >= b) {
        		
        		// point in 4th quadrant
        		g2d.drawString(Double.toString(angles[i]) + "°", polygonXS[i] + 10, polygonYS[i] + 10);
        	
        	}else if(polygonXS[i] <= a && polygonYS[i] >= b) {
        		
        		// point in 3rd quadrant
        		g2d.drawString(Double.toString(angles[i]) + "°", polygonXS[i] - 25, polygonYS[i] + 15);
        	
        	}else if(polygonXS[i] <= a && polygonYS[i] <= b) {
        		
        		// point in 2nd quadrant
        		g2d.drawString(Double.toString(angles[i]) + "°", polygonXS[i] - 25 , polygonYS[i] - 10);
        	}
        }
        
        // all summary
        g2d.drawString("Angle A : "+ Double.toString(angles[0]) + "°", 10, 20);
        g2d.drawString("Angle B : "+ Double.toString(angles[1]) + "°", 10, 40);
        g2d.drawString("Angle C : "+ Double.toString(angles[2]) + "°", 10, 60);
        g2d.drawString("Error : "+ Double.toString(error) + "°", 10, 80);
    }

    private static void create() {
    	
    	// create JFrame to draw some graphics
        JFrame f = new JFrame("Circle - Triangle");
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.add(new CircleTriangleGUI(3));
        f.pack();
        f.setVisible(true);
        f.setLocationRelativeTo(null);
    }

    public static void main(String[] args) {
    	create();
    }

	@Override
	public void mouseDragged(MouseEvent event) {
		double x0;
		double y0;
		if(dragging) {
    		x0 = event.getX();
			y0 = event.getY();
			
			double angle = Math.toDegrees(Math.atan2(y0 - b, x0 - a));	//gives angle between -180 to 180
			angle = angle < 0 ? angle + 360 : angle;					//convert [-180, 180] to [0, 360]
			angle = Math.toRadians(angle);								//[0, 360] to [0, 6.28]
			x0 = Math.round(a + Math.cos(angle) * r);					//update x0 to move over circle circumference
			y0 = Math.round(b + Math.sin(angle) * r);					//update y0 to move over circle circumference
			
			polygonXS[index] = (int) x0;	//set updated x0 value to selected circle
			polygonYS[index] = (int) y0;	//set updated y0 value to selected circle
			
			updateLengthsAngles();
			
			//finally replace circle with newer value
			circles.set(index, new Ellipse2D.Double(x0 - 5, y0 - 5, 10, 10));
			
			repaint();
		}
	}

	private void updateLengthsAngles() {
		
		for(int i = 0; i < lengths.length; i++) {
			lengths[i] = Math.sqrt(Math.pow((polygonXS[(i + 1) % 3] - polygonXS[(i + 2) % 3]), 2) + Math.pow((polygonYS[(i + 1) % 3] - polygonYS[(i + 2) % 3]), 2));
		}
		for(int i = 0; i < angles.length; i++) {
			angles[i] = Math.round(Math.toDegrees(Math.acos(((lengths[i % 3] * lengths[i % 3]) - (lengths[(i + 1) % 3] * lengths[(i + 1) % 3]) - (lengths[(i + 2) % 3] * lengths[(i + 2) % 3])) / (-2 * lengths[(i + 1) % 3] * lengths[(i + 2) % 3]))));
		}
		error = 180 - (angles[0] + angles[1] + angles[2]);
	}

	@Override
	public void mousePressed(MouseEvent event) {
		
		// get the index of which circle was clicked and set dragging flag
		dragging = true;
		Point p = new Point(event.getX(), event.getY());
		
		if(circles.get(0).contains(p)) {
			index = 0;
		}else if(circles.get(1).contains(p)) {
			index = 1;
		}else if(circles.get(2).contains(p)) {
			index = 2;
		}else {
			index = -1;
			dragging = false;
		}
		
	}

	@Override
	public void mouseReleased(MouseEvent arg0) {
		dragging = false;
	}
	
	@Override
	public void mouseMoved(MouseEvent arg0) {}

	@Override
	public void mouseClicked(MouseEvent arg0) {}

	@Override
	public void mouseEntered(MouseEvent arg0) {}

	@Override
	public void mouseExited(MouseEvent arg0) {}
	
}