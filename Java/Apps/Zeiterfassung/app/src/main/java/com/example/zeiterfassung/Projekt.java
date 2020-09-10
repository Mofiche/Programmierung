package com.example.zeiterfassung;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.KeyEvent;

public class Projekt extends AppCompatActivity {

    @Override
    public boolean onKeyDown(int keyCode, KeyEvent event) {
        if(keyCode == KeyEvent.KEYCODE_BACK) {
            System.out.println("!!!");
            final Projekt projekt = this;
            Intent intent = new Intent(projekt, ProjektLaden.class);
            startActivity(intent);
        }
        return super.onKeyDown(keyCode, event);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_projekt);
    }
}