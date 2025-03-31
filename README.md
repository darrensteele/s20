# s20
Python to pair abandoned s20 smart plug.

Change wifi_ssid_goes_here and super_secret_password_goes_here in the pair_s20.py script to be your SSID and password.  Be sure to keep the \r after each string.

Get your Orvibo S20 into local wifi network mode by long pressing the power button for 5s until it flashes red.  Then long press for 5s again until it starts flashing blue.

The S20 has now created a wifi network called something like WiWo-S20.  Connect to this wifi network and execute the pair_s20.py script either by "python3 pair_s20.py" or by making it executable if you're running on linux.

It should then power cycle the S20 and it should be on your network.  If you get any issues feel free to reach out.

Only tested on linux!  But it's python so you should be alright
