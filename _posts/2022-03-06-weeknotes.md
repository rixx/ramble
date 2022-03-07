---
date: '2022-03-06'
layout: post
summary: ''
title: Weeknotes for February 28th – March 6th. Catching up.
---

Now that I'm not sick anymore, and I haven't worked for most of February, March will be mostly about catching back up.
This week was a pretty decent intro to that, consisting mostly of a ton of tiny things, with no big satisfying
overarching theme. Where is the hero's journey I was promised?!

## pretalx

Nothing big and heroic this week, sadly, but a lot of small important things. I spent an unusual amount of time with
sales and support things, but it's all worth it when you can fix bugs within eight minutes of them being (rather
urgently) reported.

I implemented two features, one larger and one smaller: Organisers can now change what fields in the CfP are called – so
if you want to rename title to "snazzy tagline", I can't stop you anymore. I also made it easier to select all fields
for the proposal/speaker export, to avoid turning that into a chore of its own.

Additionally, as always, some bugfixes happened: Filtering proposals by answers to (multiple) choice questions was
broken, as was travelling back to older schedule versions in the schedule editor. There was also a mildly buggy redirect
(pretalx sometimes tried to send you back to the proposal page after deleting the proposal, which predictably did not
work out), and a super rare race condition that got triggered for the first time on pretalx.com, and is now
fixed/patched over.

## Venueless

The eternal PR got merged! I only had to add some more docs. We spent some time brainstorming the next big feature, but
resolved to ask users what they actually need before getting started on details. More next week, hopefully.

## Other tech things

There was a lot of small, unexciting tech stuff this week:

- Wrote a tiny style for danluu's blog, because he was writing about people hassling him about his site style,
  particularly the line lengths, and it turns out that I don't use Firefox Reader mode, ever.
- Spent five minutes figuring out which filters I needed to make bit.ly only show the interesting parts (i.e. the
  actual URL shortener)
- Included pip in all my AUR versions of Python, prompted by a comment on Python 3.9
- Added `--delete` to my backup sync, freeing up a lot of space on our NAS, oops
- Wrote [dev.rixx.de](https://dev.rixx.de) as an introduction page for future clients, and updated my
  [CV](https://dev.rixx.de/cv.pdf)
- Made sure that `pam_faillock` won't lock me out of my servers anymore, following Arch's move to the new default of
  three incorrect passwords locking you out, which is an excellent denial-of-service vector
- Extended my book website so it also outputs a database, which is included on [data.rixx.de](https://data.rixx.de)
- At the same time, noticed that the Django issues database on that page was wildly out of date, so recreated it in a
  way that makes future updates easy.
- Looked at my old PRs and issues on GitHub and closed all that didn't look like they'd get resolved (if they were older
  than two or three years)
  
## Life stuff

The biggest thing that happened last week was me finishing a project proposal for a gig I'd really like to get. No other
big things happened, but a ton of small things:

- I started being more active in a friend's Discord server, where I have a channel that I can use for diary writing/live
  debugging. Very cool.
- Made some major-ish life choices for the next 5-10 years. Stressful, but good to have done.
- Asked people on fedi about [finances after moving out from home](https://chaos.social/@rixx/107881153618832791), with
  a lot of very interesting answers
- Did my monthly taxes, felt quiet despair that the next months won't look very good on account of not having worked in
  February
- Lent began, so I made some changes to my quiet day-to-day life, all of which seem to be working out for me
- I booked business and leisure travel things, and made summer plans with various friends. Feeling very content.
- Compiled Stepmania because I wanted to move, but it was strictly too cold to go outside
- Helped review a friend's (big, cool) blog post, and while I was at it, also fixed some factual inaccuracies on my
  website, like claiming on my funding page that I was employed as software developer and didn't need no money (oops)
- Streamed twice! Streams were good, both the gaming stream and the coding stream. Came up with a cool new channel point
  rewards (etymology facts), and collected a long list of cool facts, mostly from memory with safety double checks

## Books

No reviews AND no new books this week, which feels concerning. I started reading Seveneves, but didn't get very far.
