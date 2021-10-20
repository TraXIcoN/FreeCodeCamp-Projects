package com.asif.snake;

import android.app.*;
import android.content.*;
import android.graphics.*;
import android.os.*;
import android.view.*;

public class SnakeActivity extends Activity {

    // Declare an instance of SnakeView
    SnakeView snakeView;

    // We will initialize it in onCreate
    // once we have more details about the Player's device@Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        //find out the width and height of the screen
        Display display = getWindowManager().getDefaultDisplay();

        // Load the resolution into a Point object
        Point size = new Point();
        display.getSize(size);

        Intent intent = getIntent();

        AppConstants.Control control = (AppConstants.Control) intent.getSerializableExtra(AppConstants.CONTROL_KEY);
        Boolean soundPref =  intent.getBooleanExtra(com.asif.snake.AppConstants.SOUND_KEY,true);
        // Create a new View based on the SnakeView class
        snakeView = new SnakeView(this, size);
        snakeView.setControl(control);
        snakeView.isSoundEnabled = soundPref;

        // Make snakeView the default view of the Activity
        setContentView(snakeView);
        snakeView.startGame();
    }


    // Start the thread in snakeView when this Activity
    // is shown to the player
    @Override
    protected void onResume() {
        super.onResume();
        snakeView.resume();
    }

    // Make sure the thread in snakeView is stopped
    // If this Activity is about to be closed
    @Override
    protected void onPause() {
        super.onPause();
        snakeView.pause();
    }
}


