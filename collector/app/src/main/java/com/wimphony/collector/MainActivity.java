package com.wimphony.collector;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.content.pm.PackageManager;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.net.wifi.WifiManager;
import android.os.Handler;
import android.support.v4.app.ActivityCompat;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.widget.Toast;

import java.util.List;
import java.util.jar.Manifest;

public class MainActivity extends AppCompatActivity {

    private LocationManager locationmanager;
    private LocationListener locationlistener;

    private class scanResultsHandler extends BroadcastReceiver
    {
        @Override
        public void onReceive(Context c, Intent i) {
            Log.d("MainActivity", "inside onReceive");
            List<WifiDataPoint> w = Wifihelper.getCurrentDataPoints(c);

            for (WifiDataPoint p : w) {
                Log.v("MainActivity", p.toString());
            }
            ServerComms.sendDataPoints(w);
        }
    }

    private boolean permissionCheck(String toCheck)
    {
        if (ContextCompat.checkSelfPermission(this, toCheck)
                != PackageManager.PERMISSION_GRANTED) {
            Log.d("MainActivity", "requesting permission " + toCheck);
            ActivityCompat.requestPermissions(this,
                   new String[]{toCheck}, 42); // magic number
        }
        else {
            Log.d("MainActivity", "apparently " + toCheck + " already granted");
        }

        if (ContextCompat.checkSelfPermission(this, toCheck)
                != PackageManager.PERMISSION_GRANTED) {
            return false;
        }
        return true;
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        final Handler h = new Handler();
        final int scanDelay = 5000;

        if (!permissionCheck(android.Manifest.permission.ACCESS_WIFI_STATE) ||
                !permissionCheck(android.Manifest.permission.CHANGE_WIFI_STATE) ||
                !permissionCheck(android.Manifest.permission.ACCESS_COARSE_LOCATION))
        {
            Log.e("MainActivity", "fatal error: permissions not granted");
            this.finish();
        }
        else {
            Log.d("welp", "that happened");
        }

        h.postDelayed(new Runnable(){
            public void run(){
                try {
                    Log.d("MainActivity", "reached start");
                    Wifihelper.startScan(getApplicationContext());
                       h.postDelayed(this, scanDelay);
                } catch (Exception e)
                {
                    Toast t = Toast.makeText(getApplicationContext(),
                            "Couldn't start scan",
                            Toast.LENGTH_SHORT);
                    t.show();
                }
            }
        }, scanDelay);

        this.registerReceiver(new scanResultsHandler(),
                new IntentFilter(WifiManager.SCAN_RESULTS_AVAILABLE_ACTION));

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        
    }
}
