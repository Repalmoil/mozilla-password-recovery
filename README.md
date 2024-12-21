# mozilla-password-recovery
Recovering passwords from mozilla firefox browsers

## This tool will help you recover passwords from the Mozilla browser using the NSS library for decryption. This tool is part of a segment of  <a href="https://xcore.sell.app/">x-core</a>
 ## from which I extracted a piece of code; I am working on obtaining the rest of the code for Chrome, Edge, Opera...

The code appears to handle credential extraction from Firefox profiles stored in signons.sqlite or logins.json files. It supports different OS environments (Windows, macOS, Linux) and dynamically loads the appropriate NSS library for decryption.



# Key Components:


## Profile Detection
This project focuses on the detection of user profiles through various techniques and methods.

## Overview

### SQLite/JSON Parsing
- Efficiently parse data stored in SQLite databases.
- Handle JSON data for seamless integration and data manipulation.

### NSS Loading and Decryption
- Implement loading of NSS (Network Security Services) files.
- Ensure secure decryption of sensitive information.

### Exception Handling and Logging
- Robust exception handling to manage errors gracefully.
- Comprehensive logging for tracking operations and debugging.

## Dependencies: Ensure you have the required dependencies installed:

<pre><code>pip install pycryptodome</code></pre>

Also, SQLite3 and ctypes are part of the Python standard library, so no need to install them separately. 

Permissions: Running the script might require admin/root privileges, depending on the OS, to access Firefox profile directories.

### Verify NSS Paths: Ensure nss3.dll or libnss3.so can be found in the specified directories. 
<pre><code>locate nss3.dll  # Windows 
locate libnss3.so  # Linux/Mac</code></pre>

# Use:
<pre><code>git clone https://github.com/Repalmoil/mozilla-password-recovery </code</pre>


<pre><code>python main.py </code</pre>



