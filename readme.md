Port Scanner Tool
A simple and efficient port scanner written in Python.

------------------------------------------------------------------------------------------------
Usage:
. <target(s): Comma-separated list of target IP addresses or hostnames (e.g. 192.168.1.1, example.com )
. <port_range>: Number of ports to scan (e.g. 100)

----------------------------------------------------------------------------------------------------

Features:
1. Simple and easy-to-use command line interface
2. Supports multiple targets separated by commas
3. Scans a specified range of ports
4. Displays open ports for each target
5. Displays a banner with scan information

Port Scanner Tool
------------------------------------------------------------------------------------------------

Target(s): 192.168.1.12, example.com
Port(s): 100

------------------------------------------------------------------------------------------------

Requirements:
Python 3.x
socket library (included in Python standard library)
termcolor

-----------------------------------------------------------------------------------------------------------------

Installation:
1. clone the repository
2. Run pip install termcolor (Optional)
3. Run the port scanner script