---
date: '2022-01-31'
layout: post
summary: ''
title: Weeknotes for January 23rd-30th
---

This week felt more normal than last week – I got much less done, though did more paid work and hit what felt like a
sustainable pace, at least for now.

## pretalx

Okay, so there was one exception to my less productive week: one huge pretalx feature! Organisers can now **asign
reviewers to specific proposals**, and can either *limit* reviewers to their assignments, or just make those assignments
their *priority*. I admittedly finished that one on the night from Sunday to Monday, but I decided to count it towards
this week on account of most of the final touches taking place in the hours from 4am to 8am.

I also spent something close to a day fiddling with the pretalx schedule, because it sometimes bugged out when people
nested break periods. Things look much better now, and some incidental bugs got fixed, too. Thanks go to rash for
double-checking my logic. While working on that, I got myself a list of good testing schedules from the past week, and
also documented how I exported them, for future reference (because real-world data is great to find nasty edge-cases).

Othere than that, I focused on bugfixes and maintenance work. I improved the team settings I mentioned last week some
more (prompted by writing my weeknotes, which are already paying off!), so that reviewer settings are integrated better
and the UI is more friendly. I also found a small bug in last week's caching feture.

Maintenance-wise, I added GitHub Workflows to all of the older plugins that didn't have those already, migrated the
remaining `master` branches to `main` branches, and applied flake8-bugbear and django-upgrade all over the place (thanks
to Adam Johnson for mentioning those!).

Oh, and with the help of the Fediverse, I found [quickchart.io](https://quickchart.io), which generates charts from URL
parameters. The pretalx [list of events](https://github.com/pretalx/pretalx/wiki/Events) now comes with a fancy chart,
at nearly no additional effort!

## Venueless

My only contribution to Venueless this week was a small bugfix for an incorrect URL join, and then I also applied
flake8-bugbear and django-upgrade here. Didn't catch any bugs, but improved some code smells and made future upgrades
easier.

## Other tech things

I focused a lot on freelance work this week, with nearly five full-time days spent on two clients. Naturally, this left
much less time for tinkering, so I only have some small hacks to report:

I added an audio mixer one-click shortcut to my status bar, because I've been switching more between work at my desk and
my couch, with multiple possible audio devices per location.

I also found a way to use a real (CLI) file browser with neomutt, both to select attachments and to save them later on.
I also memorised two or three more shortcuts for my preferred file browser (ranger), and I hope I can keep using them
until they sink in, this time.

And finally, I did two programming streams with one of my generative art projects (still very much a baby project). I
learnt how to rotate points around a given origin (remembering the odder parts of trig), and then figured out how to get
the same results with subsketches and transformations. I have some pretty cool plans for the project, and I'm currently
hunting for books and other resources to get going.
  
## Life stuff

For the first time in what feels like ages, I'm actually in a regular rhythm for daily life that works well for me, and
is healthy AND productive AND sustainable. I mentioned this last week, and to my ongoing astonishment it still seems to
work, complete with long walks and daily hot meals and a good and stable mood. I can't overstate how good this is.

Despite this, Monday through Wednesday were fairly unproductive unless you count reading, because I screwed over my
sleep cycle in order to finish the huge pretalx feature in time for an event to test it. I was back to normal around
Wednesday or Thursday, which also means that I did the bulk of my five freelance work days in the second half of the
week.

The weekend was great: I spent part of it with my flatmate and my family, enjoying our time together and also debugging
my grandfather's model train table. Lots of tricks to pick up from a clever old physics teacher! Then, afterwards, there
was a speedrunning tournament in a community I'm involved in, and I took up my role as inofficial official timekeeper.
My helper tool I had written in the week before came in very handy, and I added some further small modifications.

And finally, I streamed one last time on Sunday, this time gaming instead of coding. I had a ton of fun and got to show
off my first ever commissioned channel emote. More are going to follow soon-ish (as soon as my Twitch payouts pay for
them, basicalls), and I think I'll try to keep up the split between coding streams during the week and gaming streams
during the weekend.

## Books

I read some more books, though less than before because I was tired from both last week and all the other things to do
this week. Instead, I have written eight (!) book reviews, which brought my review backlog down from 12 to 9. There is
still hope for me.

- [Four Roads Cross](https://books.rixx.de/max-gladstone/four-roads-cross/)
- [Between Copernicus and Galileo](https://books.rixx.de/james-m-lattis/between-copernicus-and-galileo/) (longest review
  so far this year)
- [Salt Magic, Skin Magic](https://books.rixx.de/lee-welch/salt-magic-skin-magic/)
- [Widdershins](https://books.rixx.de/jordan-l-hawk/widdershins/)
- [Death by Silver](https://books.rixx.de/melissa-scott-amy-griswold/death-by-silver/)
- [Son of a Liche](https://books.rixx.de/j-zachary-pike/son-of-a-liche/)
- [Leviathan Falls](https://books.rixx.de/james-s-a-corey/leviathan-falls/)
- [City of Blades](https://books.rixx.de/robert-jackson-bennett/city-of-blades/)
