# femurgebot
### A bot seeking to programmatically catalogue all possible feminine urges

Based on jarfbot - Jarf Beezers name generator  
Based on assaultbot - internet gunshitpostbot  
Based on automatli - Swiss trollage generator  

Format is:

Verb - English verbs - in Verb.txt  
Noun - English nouns - in Noun.txt  

EXAMPLES:

```
Verb == post
Noun == shit

output: The feminine urge to post a shit
```

## Usage
* Clone repo
* pip3 install -r requirements.txt
* edit femurgebot.py and add your Twitter API details
* run

Optionally, you can run it as a service on Debian by creating /lib/systemd/system/femurgebot.service and symlinking it to /etc/systemd/system/multi-user.target.wants/femurgebot.service.

A service template is included in this distribution.
