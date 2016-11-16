Wimphony
========

Wimphony is a project that started at GreatUniHack 2016. It aims to help people sense the Wi-fi networks around them using music and VR. The members of the project are [Adam Ditchfield](https://github.com/Surfad), [Agnes Wąsikowska](https://github.com/aga11313), [Cameron MacLeod](https://github.com/notexactlyawe) and [Mayank Gupta](https://github.com/officialgupta).

## Structure

Wimphony is split into three main sections. An Android app collects Wi-fi SSIDs and RSSIs at various locations and and attempts to localise the networks to come co-ordinates. These get sent to a Flask server that takes the SSIDs and generates music based off them. A user with a VR headset (currently Google Cardboard) queries the server for all Wi-fi networks within an area and the app then places these Wi-fi networks within a virtual world that can then be explored.

## Current state of the project

Currently each of the components more or less work on their own in a demoable state, but they are not integrated.

