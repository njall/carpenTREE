# carpenTREE
repo for carpentries lesson visualization

## Backgroud

This is a hackday project created at the #CollabW19 workshop in Loughborough on 3 April 2019. 

We aim to address the following use cases:

As a carpentry instructor,  
I want to create a customised lesson for a specific outcome  
In order to deliver efficient and tailored training.

As a carpentries student  
I want to know which lessons would be a good follow up to what I just learned  
In order to get the most out of the software carpentries class and material.

## Idea
The idea is to scrape software carpentries lessons for learning outcomes and prerequisites and visualize them in an interactive tree structure that helps navigating episodes within software carpentry lessons. A manual prototype is available [on the TeSS ELIXIR portal](https://tess.elixir-europe.org/workflows/carpentree-test-case/).


## Implementation

fertilizer.py 

#### Ideas that didn't work 
* using the glossary as this is lesson and not episode specific

#### Other things that could work and need further investigation
* look at code examples used in episodes and see if they import any libraries or packages that could be linked to other episodes

### Installation

`pip install -r requirements.txt`

Run with:

`python fertilizer.py'

## Further work

Ideas for further improvements are listed as [issues](https://github.com/vwkoppejan/carpenTREE/issues).
