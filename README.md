# String Similarity Calculation

Methods: 

[1.] Levenshtein Distance  <br>

The Levenshtein distance is a string metric for measuring the difference between two sequences. Informally, the Levenshtein distance between two words is the minimum number of single-character edits (insertions, deletions or substitutions) required to change one word into the other

Calculates how many transformations you need to perform on the string A to make it equal to string B. The algorithm is also known as Edit Distance.

pip install python-Levenshtein


[2.] Cosine Similarity <br>

Cosine similarity is a measure of similarity between two non-zero vectors of an inner product space that measures the cosine of the angle between them.

Calculates the angle between two vectors first. But you can’t represent some sentence as a vector in n-dimensional space just out of the box.
You’ll want to construct a vector space from all the ‘sentences’ you want to calculate similarity for. That vector space will have as many dimensions as there are unique words in all sentences combined.


