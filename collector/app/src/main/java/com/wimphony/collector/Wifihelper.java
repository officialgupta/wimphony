package com.wimphony.collector;

import android.content.Context;
import android.net.wifi.ScanResult;
import android.net.wifi.WifiManager;
import android.util.Log;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by Cameron on 12/11/16.
 */

public class Wifihelper {
    static WifiManager getWifiManager(Context c) throws Exception
    {
        WifiManager w =  (WifiManager) c.getSystemService(Context.WIFI_SERVICE);

        if (!w.isWifiEnabled())
        {
            Log.w("WifiHelper", "Wifi not enabled");

            boolean enabled = w.setWifiEnabled(true);
            // if not enabled then show toast and stop
            if (!enabled) {
                throw new Exception("Wifi not enabled, and that's, like, most of the point");
            }
        }

        return w;
    }

    static List<WifiDataPoint> getCurrentDataPoints(Context c)
    {
        WifiManager w;
        try {
            w = getWifiManager(c);
        } catch (Exception e) {
            Log.e("WifiHandler", "getCurrentDataPoints caught an error");
            return new ArrayList<WifiDataPoint>();
        }
        Log.d("Wifihelper", "Inside: getCurrentDataPoint");
        List<WifiDataPoint> l_wdp = new ArrayList<WifiDataPoint>();

        List<ScanResult> res = w.getScanResults();
        Log.d("Wifihelper", Integer.toString(res.size()));

        for (ScanResult s : res)
        {
            Log.d("GetCurrentDataPoints", "added summat");
            l_wdp.add(scanResultToWDP(s));
        }

        return l_wdp;
    }

    static public void startScan(Context c) throws Exception
    {
        WifiManager w = getWifiManager(c);

        boolean scanStarted = w.startScan();
        if (!scanStarted)
        {
            Log.e("WifiHelper", "Couldn't start scan");
            throw new Exception("Couldn't start scan");
        }
    }

    static public WifiDataPoint scanResultToWDP(ScanResult s)
    {
        WifiDataPoint w = new WifiDataPoint();
        w.rssi = s.level;
        w.ssid = s.SSID;

        return w;
    }
}
