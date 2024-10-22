Issue was that I was previously 'stripping' on ",":
​
- Fixed this by BOTH stripping and splitting on " ".
- UPDATE: NO NEED TO EVEN USE ".strip(" ") - all this does is remove an LEADING OR TRAILING occurances of a specified char (so irrelevant to use on the OG string!!)
​
​