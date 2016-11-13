package com.wimphony.collector;

import java.io.BufferedOutputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.List;

/**
 * Created by cameron on 12/11/16.
 */

public class ServerComms {
    public static void sendDataPoints(List<WifiDataPoint> wdp)
    {
        try {
            URL url = new URL("http://wimphony.com/post");

            HttpURLConnection conn = (HttpURLConnection) url.openConnection();

            conn.setChunkedStreamingMode(0);

            conn.setRequestMethod("POST");
            conn.setRequestProperty("USER-AGENT", "Mozilla/5.0");
            conn.setRequestProperty("ACCEPT-LANGUAGE", "en-US,en;0.5");
            conn.setDoOutput(true);

            String rssi = "";
            String ssid = "";

            for (WifiDataPoint w : wdp) {
                rssi = rssi + Integer.toString(w.rssi);
                ssid = ssid + w.ssid;
            }

            String urlParameters = String.format("rssi={}", rssi);

            DataOutputStream out = new DataOutputStream(conn.getOutputStream());
            out.writeBytes(urlParameters); //Writes out the string to the underlying output stream as a sequence of bytes
            out.flush(); // Flushes the data output stream.
            out.close(); // Closing the output stream.

            //writeStream(out, wdp);
        } catch (Exception e){

        }

    }



}
