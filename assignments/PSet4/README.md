**Problem Set \#4**

**Assignment Learning Objectives**

1.  Write a program using Python language syntax

2.  Translate a program from Fortran to Python to further aid in
    learning Python language syntax

3.  Develop debugging skills to aid in writing and using computer code

**Due 6 October 2020 by 3:00 pm**

*Due Online*

-   Three scripts in the PSet4 repository on your GitHub account

*Due Via Blackboard*

-   A PDF version of your code. Make sure the honor code appears in the comment block at the beginning of the script and that it has your full typed out name. This will serve as your assertion that you have upheld the honor code.

**Honor Code**

You must type the full honor code into each comment block to indicate
that you have upheld the code. Authorized aid for this assignment is
your notes and any previous programs you have written. You are highly
encouraged to work with others in the class to help diagnose bugs and
work out programming logic. Any copying of someone else's code IS A
VIOLATION OF THE HONOR CODE, whether from a classmate, or the Internet.
*Be sure to indicate with whom you have worked in the comment block of
your submission.*

Problems

1.  Convert the Fortran program, **windspeed\_conversion.for**, to do
    exactly the same thing, but using the Python programming language.
    (Fortran program in /archive/data\_kevin/met330)

    Program Name: **windspeed\_conversion.py**

    Program Input: wind speed and units from the command line

    Program Output: Original Wind Speed and Units, Converted Wind Speed
    and Units

    Note: Don't worry about formatting the output in Python.

2.  Debug the Python program, **broken\_leap.py**, for syntax errors
    (Python program available in /archive/data\_kevin/met330). Put
    comments in the script for what you corrected to make it work
    properly. Call the corrected program **leap.py**.

    Program Name: **leap.py**

    Program Input: year from command line

    Output: year and whether it is a leap year

3.  Write a Python program to determine the months that the standardized
    Southern Oscillation Index (SOI) indicate El Nino conditions (for
    simplicity defined for this assignment as SOI \< -1.25) or La Nina
    conditions (for simplicity defined for this assignment as SOI \>
    1.25). Report the actual SOI value, the month and year it occurred,
    and whether this is indicative of El Nino or La Nina conditions over
    the period 1951 to current. Additionally, determine the maximum and
    minimum value SOI over the entire period, reporting the month and
    year they occurred in. Print the results to the screen.

    Program Name: **soi.py (starter code given in assignment repo)**

    Input File: soi\_data.txt (Available in /archive/data\_kevin/met330)

    Output:

-   The average SOI value for each year

-   The maximum SOI value for each year

-   The minimum SOI value for each year

-   The total number of months spent in La Nina for the dataset

-   The total number of months spent in El Nino for the dataset

> **Background**
> 
> The Southern Oscillation Index (SOI) is a measure of the difference
> between sea level pressure in Tahiti and Darwin, Australian, which
> gives a proxy for shifts in the Walker Circulation and thus the El
> Nino -- Southern Oscillation (ENSO). There are many other ways to
> define ENSO periods and a good resource for background information can
> be found at:
> <https://www.climate.gov/news-features/blogs/enso/why-are-there-so-many-enso-indexes-instead-just-one>.
> 
> Generally, an El Nino or La Nina event cannot be determined from any
> one month of an ENSO index, however, for simplicity here we define an
> El Nino event when the SOI value is below -1.25 for any particular
> month and a La Nina event when the SOI value is above 1.25 for any
> particular month.
> 
> Notes:
> 
> -   Break the problem down into smaller bite size pieces. For example,
>     first write your program to be able to read in the input file and
>     final global max and min values. Then submit that working code to
>     your GitHub repository for this assignment. Now go back and work on
>     finding individual months that can be classified as El Nino, etc.
> 
> -   Make sure to regularly submit your work to your GitHub site. Part of
>     your grade on each assignment is on your regular submission of the
>     program(s) as they are in progress of being developed. This is
>     easily done when regularly submitting the bite size pieces that you
>     create when breaking down any coding project!
> 
> -   Be sure to verify that your results are correct.
> 
>     *Please make your program to produce output in the same fashion as
>     the test cases below.*

    **Example Output (Fake Data)**

    >>>

    El Nino: February 2020

    SOI: -3.5

    La Nina: July 2021

    SOI: 1.4

    .

    .

    .

    .

    Max SOI of 2.2 in October 2050

    Min SOI of -3.1 in December 2024

    >>>

**Evaluation Criteria**

Each of the following criteria will be rated from not present/completed
to exemplary, having all of the elements will yield at least a 7/10 for
a particular criterion. The assignment is out of 50 points.

-   Conversion of windspeed\_conversion.for efficiently coded, styled
    well, and correct values reported in output (10 points)

-   Corrected leap.py program (10 points)

-   Efficiently coded, styled well, and correct months for El Nino and
    La Nina events with Max and Min SOI correctly reported (10 points)

-   Informative and Clear Output from running code (10 points)

-   Code is well documented (informative comments/descriptions of code
    blocks; 5 points)

-   Code was regularly updated and committed to GitHub repository (5
    points)
