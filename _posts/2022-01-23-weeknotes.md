---
date: '2022-01-23'
layout: post
summary: ''
title: Weeknotes for January 16th-23rd
---

A second week doing weeknotes *nearly* establishes this as a tradition! I've been keeping an open scratchpad document
for the past week, quickly noting down pretty much anything that got a git commit or that felt otherwise important. The
most astounding part was how **fast and long** this document grew! If you had asked me without it, I would have told you
that this felt like any other week: a bit disappointing, not productive enough, and that I got basically nothing done.
Huh.

## pretalx

I got a surprising amount done this week in pretalx! All of it small bugfixes or tiny features, but these add up, it
turns out:

- It was impossible to create events in the past, even though I intended to only show a warning against it.
- On some pages, empty alert boxes were displayed due to mishandled template logic.
- On the central schedule page, the timezone picker (or at least its dropdown) disappeared halfway behind a foreground
  element.
- I found out that in most places, I had used bootstrap's `table-responsive` incorrectly, applying it to the table
  itself instead of to a wrapper element!
- A tiny bug led to deleted proposals being included in the total count on one dashboard, oops. But this got me to learn
  about the `filter` attribute for Django's `Count()` aggregation!
- It was possible to create teams with no associated events, and once you had done so, it was pretty hard to pick out
  that something was wrong, and why the team members didn't turn out to have the correct permissions.
- The automatic email confirming a new proposal's successful submission was not shown in the list of emails sent to
  speakers, which led to some confusion, so it's now included (leading to some minor changes in email/templating APIs).
- pretalx-public-voting, the plugin featured last week, had a bug where withdrawn proposals would still be listed on the
  public voting list. I fixed that and made the proposal selection generally more safe and restrictive.

## Venueless

I added tests, documentations, bugfixes and general improvements to our [most requested Pull
Request](https://github.com/venueless/venueless/pull/295), adding global announcements to Venueless. It's been in the
works for a long time, and close to being done!

I also fixed a bunch of bugs in the pretalx-venueless integration. Most importantly, pretalx will notify Venueless users
when a new schedule is released, but its caching of the schedule page led to users then not getting the changes from the
API! The fix took some navigating how pretalx caches things, leading to …

## Django caching memes

I don't tend to use built-in caching in Django a lot, prefering to rely on external tools (nginx, for example) or
manually caching data where appropriate. That's mostly because Django's caching is a bit too magical for my tastes, and
I don't really understand what's happening, which is a really bad feeling for a vital part in your application stack.

Or rather: I *didn't* understand it – I finally took the time to dig into the code, and I wrote a [blog
post](https://rixx.de/blog/how-django-s-page-cache-works/) explaining to Future Me how all the parts come together. I
really liked this approach – it's basically poor man's rubber duck debugging, but leaving something useful behind!

I also put my result (a way to make Django's page-level cache optional) on
[djangosnippets.org](https://djangosnippets.org/snippets/10865/), which led to me fixing a
[bug](https://github.com/django/djangosnippets.org/pull/344) in djangosnippets, because you can't ever just shave part
of the yak (remember this started with a bug in venueless, carrying over to pretalx and then to a blog post and then to
djangosnippets.org!).

Writing the blog post also led me to realise that I don't think it's reasonable to require developers to go through
these steps to get a fairly simple bit of functionality – usually I tend to think that I'm just a bit on the slow side
picking up what needs to be done (which I am!), but here, a very reasonable behaviour could be provided by the framework
in the first place.

So, to finish shaving the yak, I dug up the [old ticket describing the ideal
behaviour](https://code.djangoproject.com/ticket/11269), that had been opened 13 years ago and closed 11 years ago, went
through the context, and wrote a [long-ish email](https://groups.google.com/g/django-developers/c/UbD1DkV1uPo) to the
Django developer mailinglist, asking for opinions on re-opening the issue. So far, there has been one response agreeing
with me, so I'm hoping this will happen (either magically, or maybe I'll find some time next month to look into this).

## Other tech things

I accidentally triggered the numlock on my external keyboard and thought I broke it. In the hour before somebody kindly
told me I was being an idiot, I looked longingly at fancy split keyboards, which I WANT, but can't justify getting just
now. My external keyboard is a Thinkpad one with a great wrist rest, a TrackPoint (which I don't use a lot because it
tends to hurt my fingers in the long run) and, most importantly, mouse buttons. This is *so* good.

So if I were to replace this keyboard, I'd either go with a fairly cheap Cherry one with a similarly short key travel
distance, **or** go all in. But I didn't find a keyboard that was convincing: I really want a mix of the [Ultimate
Hacking Keyboard](https://ultimatehackingkeyboard.com/), because you can add mouse buttons and track balls to either
side of the split keyboard, and the [Ergodox](https://ergodox-ez.com/pages/customize) or the Moonlander for its Matrix
layout. (Just putting this here so that Future Me has less research to do once the old keyboard dies). But also, all of
them have fairly long travel, which I don't like, and I don't have the energy to solder my own (though there are great
kits out there!)

Other small tech things:

- New Python versions came out, so I updated the Archlinux AUR PKGBUILDs for 3.9-3.11.
- I added an alias to my zshrc, `pydist`, which simply runs `python setup.py sdist bdist_wheel` and uploads the result
  to PyPI. It doesnt' touch git or versioning at all, but it's really nice for very small packages.
- I tried out [pyupgrade](https://github.com/asottile/pyupgrade) on a couple of projects, adding more f-strings and
  replacing a ton of `set()` calls with set literals.
- For a hobby (speedrunning), I needed a small helper tool automating the manual splitting of two racers during speedrun
  races/tournaments. I wrote a tiny website (180 lines including everything) that will do the job [pretty
  well](https://github.com/rixx/tools/blob/master/speedrun-race-timer/index.html). We'll see how well it works next
  week.
  
## Life stuff

I tried out Trello and the GitHub Projects (with a closed private repo for life stuff) for todo management. Turns out:
Nope, long walks and a bullet journal are still the only way for me to organise what's in my head. Bonus points for the
two days of snow – I swear, I'm like a Discworld troll, and I think better the colder it is.

Related to the long walks: I found a rhythm for daily life that works well for me without forcing me to get up early or
go to bed early (which simply does not work), and that leaves enough flexibility to make every day interesting while
also including luxuries such as regular meal times. I've been cooking every day and enjoying it a lot.
My flatmate also moved his stationary bike to our shared living room, so on days with terrible weather I've still got
the option to get some movement in, which is really nice!

Oh, I also drank a bottle of Club Mate after a full year of no caffeine, which was a *terrible* decision, and I think
I'm solidly off caffeine still, with no desire to go back.

And finally, my ebook reader broke, by which I mean that I forgot to turn off the wifi before rebooting, and so the
Amazon firmware updated to a version that doesn't have a jailbreak yet. Which was disastrous, because it meant no more
PDFs (with a jailbreak, Kindle devices can run KOReader, which can reflow PDFs and has a ton of other great features). I
spent half a day researching devices, and finally bought, received and configured a Kobo Libra 2.

## Books

Despite the book disaster, I read some books last week (5, I think?), but I didn't get around to writing any reviews,
putting my backlog at 12. I hope I have something to link in this section next week!

I also added more quotes to my book site, reminding me that I finally need to put those quotes … somewhere. So if I find
a free minute, I might finally build the cool quotes feature, which is (I think) the last big thing missing from
[books.rixx.de](https://books.rixx.de).
