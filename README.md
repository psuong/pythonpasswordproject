Python Password Project
=======================

This is my final project for my intro to Python class.
I try to "break" the Yahoo file, but it's really data scraping.
The Yahoo file is not push through a hash function, so I simply
had to read from the file.

The Linkedin passwords use a SHA-1 Hash. Since it is a 1-way hash,
the easiest way is to brute force through the program.  Additionally,
the hashes consists of random hexdecimals and random hexdecimals with
'00000' in front.  Rather than bruteforce every possible combination,
I read from a textfile containing 10,000 common passwords.

Of the 10,000 common passwords, approximately 7,000 of them were used.

Formsprings is rather annoying/weird. While it uses SHA-256, the added extra
characters to the password to strengthen the security. This password consists of
your original password and a number from 00-99 at the front of the password.

Because the text files are large for Yahoo and Linkedin, contact
-psuong95@gmail.com- for a copy of the files.

Files are courtesy of the Computer Security Class at NYU Poly.

Progress:
Yahoo: Done
Linkedin: Done
Formsprings: In Progress
GUI Implementation: Not Started
