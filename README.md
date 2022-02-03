# automatli
### e süsse roboterli uus Züri

Swiss noun trollage generator
Based on jarfbot - Jarf Beezers name generator
Based on assaultbot - internet gunshitpostbot
Based on automatli - Swiss trollage generator

Format is:

Verb - English verbs

Noun - English nouns

EXAMPLES:

```
Verb == post
Noun == shit

output: The feminine urge to post shit
```

## Usage
* Clone repo
* pip3 install -r requirements.txt
* edit femurgebot.py and add your Twitter API details
* run

Optionally, you can run it as a service on Debian by creating /lib/systemd/system/femurgebot.service and symlinking it to /etc/systemd/system/multi-user.target.wants/femurgebot.service.

A service template is included in this distribution.
