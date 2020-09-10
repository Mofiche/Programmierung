package com.example.zeiterfassung;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.os.Bundle;
import android.view.KeyEvent;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RelativeLayout;

import java.io.File;

public class ProjektLoeschen extends AppCompatActivity {

    String formatieren(String string){
        int index = string.indexOf(".dat");
        return string.replaceAll(".dat","");
    }

    @Override
    public boolean onKeyDown(int keyCode, KeyEvent event) {
        if(keyCode == KeyEvent.KEYCODE_BACK) {
            System.out.println("!!!");
            final ProjektLoeschen projekt = this;
            Intent intent = new Intent(projekt, MainActivity.class);
            startActivity(intent);
        }
        return super.onKeyDown(keyCode, event);
    }

    @SuppressLint("ResourceType")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        RelativeLayout rel = new RelativeLayout(this);
        File directory = getFilesDir();
        String[] files = directory.list();
        final ProjektLoeschen projekt = this;
        final Button[] buttons = new Button[files.length];
        final RelativeLayout.LayoutParams[] button_details = new RelativeLayout.LayoutParams[buttons.length];


        for(int i = 0; i<=files.length - 1;i++){
            System.out.println(files[i]);
        }

        for(int i = 0; i<= buttons.length - 1;i++){
            buttons[i] = new Button(this);
            buttons[i].setText(formatieren(files[i].toString()));
            buttons[i].setId(i+1);
            button_details[i] = new RelativeLayout.LayoutParams(RelativeLayout.LayoutParams.WRAP_CONTENT, RelativeLayout.LayoutParams.WRAP_CONTENT);
            button_details[i].addRule(RelativeLayout.CENTER_HORIZONTAL);
            if(i != 0) {
                button_details[i].addRule(RelativeLayout.BELOW, i);
            }else {
                button_details[i].addRule(RelativeLayout.BELOW);
            }
            final int j = i;
            buttons[i].setOnClickListener(
                    new Button.OnClickListener(){
                        @Override
                        public void onClick(View view) {
                            File directory = getFilesDir();
                            File file = new File(directory, ((String) buttons[j].getText()).concat(".dat"));
                            file.delete();
                            Intent intent = new Intent(projekt, ProjektLoeschen.class);
                            startActivity(intent);
                        }
                    }
            );
            rel.addView(buttons[i], button_details[i]);

        }

        setContentView(rel);
    }
}