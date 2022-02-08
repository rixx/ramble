---
date: '2022-02-06'
layout: post
summary: ''
title: Weeknotes for January 31st – February 6th
---

If last week felt more normal than the week before, than this week continued the downwards trend: I felt slow and spent
most of my time in brain fog country. I got basically nothing done, particularly next to no work on my freelance
projects. I'm recording this week in the hopes that it will help (either to motivate me, or to see, looking back, that
these things do pass).

## pretalx

I tried to create an organization README for pretalx on GitHub, and failed, because my brain is ill-suited to highly
complex tasks, like reading a very short three step list. In a similarly depressing vein, there were no new features
this week, though I improved the proposal list sites by adding some clever grouping to the default sorting behaviour.

I fixed a bunch of minor bugs: one in the new review restrictions, which also prevented non-reviewers from seeing part
of the unassigned reviews, one including a missing filter on the review dashboard for better searching, and one that
missed an edge case in collision detection in the schedule editor. Oh, and I fixed a bug that arose from an annotation
returning duplicate objects in what turned out to be a very annoying bug hunt. Big yikes.

That part did have some upsides, though: I had to debug the problem in production, which means that I'm fluent again in
making Django help me find out what's wrong (there may be a blog post in that). It also meant that I ran py-spy against
production, and in consequence improved the performance of some of the organiser area **heavily**. Part of that involved
being more clever about polling on the schedule editor page, and some of it came from me introducing an incredibly
stupid (but helpful) permissions cache.

## Venueless

I should have fixed some Venueless bugs, too, but the brain fog was just too thick.

## Other tech things

I once again had to remove ``xdg-desktop-portal xdg-desktop-portal-gtk``, because all GTK apps started to have
horrifyingly slow startup times (30-90 seconds). What's with that.

I did some server maintenance: Fixed things that crawled through the syslog, and moved my mail server setup from
spamassassin to rspamd, fixing multiple inconveniences in the process. Now I have a pretty dashboard and can also
manually add mails to the learning pool. (Of course, mails moved to the Junk folder get learned as spam automatically).
Nothing broke in the process, even though I had to rewrite chunks of my ``master.cf``. Felt like I knew what I was doing
for about five minutes.

Oh, and Python 3.11.0a5 came out, so I updated that AUR PKGBUILD.
  
## Life stuff

I managed to maintain my pretty new life rhythm, complete with long walks and proper meals. And yet I felt like shit – I
feel like I've been lied to by the average advice giver. Shocker. (I have to assume I'd feel even worse had I sat
through last week at home, but …)

Other than that, little of interest happened. Didn't have the energy to stream. Took care of end-of-January invoices,
payment reminders, bookkeeping and tax forms (I'm on a monthly cycle as of this month).

This week in media: I gave in and subscribed to a "top x hackernews" feed, with a strict ban on opening the comments. I
have brain fog already, imagine what it would feel like after reading HN comments. RSS is the least addictive and most
reliable source of information out there – I also took the opportunity to update my weekly reddit roundup subscriptions,
because I found another cool niche subreddit. Oh, and I discovered a brand new 2022 Billy Talent album and felt
hilariously old. Devil on my shoulder, all that.

In social news, nothing happened, because a fucking pandemic is still ongoing. Yup. My most fulfilling social
interactions were whacking people with the big ol' banhammer over on chaos.social (though sending a nearly-on-time
birthday present to a friend came close).

## Books

As befitting this stupid, stupid week, I wrote zero book reviews, and while I read two books, those were web serials,
and the equivalent of the cheapest candy imaginable. At least not particularly addictive – there are four more books in
the series and I haven't felt any urge to continue, for now.

All things considered, this week *sucked*. New brain, please.
