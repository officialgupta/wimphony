package com.wimphony.collector;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

/**
 * Created by cameron on 12/11/16.
 */

public class WifiDataPoint {
    public int rssi;
    public String ssid;
    // add location in here

    @Override
    public String toString()
    {
        return ssid + ':' + Integer.toString(rssi);
    }

}
