#### Difference between search and match.

There is a difference between the use of both functions. Both return the first match of a substring found in the string, but re.match() searches only from the beginning of the string and return match object if found. But if a match of substring is found somewhere in the middle of the string, it returns none. 
While re.search() searches for the whole string even if the string contains multi-lines and tries to find a match of the substring in all the lines of string.
 