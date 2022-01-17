---
date: '2022-01-16'
layout: post
summary: ''
title: Weeknotes?
---

Going to put this here because I don't want to spam my main blog with an experiment I'm sure to abandon soon, but I'll
try out Weeknotes (as inspired by [Simon](https://simonwillison.net/)) for a bit. I pretty much took the first week of
January off, so we're starting with the second week.

## Weeknotes question mark

There are some very tempting things about weeknotes. For one, I tend to underestimate the amount of work I do. For
example, I could swear that I haven't done any work on pretalx since Christmas, and yet, the
[changelog](https://docs.pretalx.org/en/latest/changelog.html) lists six bug fixes, two features, and there are some
things that were too minor to be listed there. Go figure.

Another thing is that working in public seems to go over very well for a lot of people, and I do enjoy reading about
what they are doing – and people consistently give me positive feedback when I do the same. I just rarely do that, so
I'll try to do it more regularly for a bit, and see how it goes.

I do have some worries, hence using my ramble blog. For one, it's easy to imagine how these notes could turn into an
obligation, or build up pressure to perform, or a way to make myself feel bad when I don't do as much as I'd like. And I
don't want to spam people who read my main blog for the very occasional long post (and in case I abandon this experiment
in two weeks, I don't want *that* on my main blog, either), so I'm taking this slowly.

## pretalx-public-voting

pretalx-public-voting is a really cool plugin for pretalx that allows attendees to vote on proposals! It supports
different scoring procedures, and has been successfully used by several conferences. It's one of the plugins I like
best, because it showcases how good plugins are for a project of this size.

Due to interest of another event using pretalx, the plugin gained two new features: First off, the list of voters can be
limited to an organiser-curated list of emails, and secondly, organisers can choose to display more information about
proposals (namely, display more submitted data instead of just the abstract).

I also noticed some missing basic features, and fixed their lack: I added a handy link to the signup site, so that
organisers know what to link. And when copying one event to a new one, the public voting settings will be copied, too.
Additionally, there's now a changelog in the README documenting recent changes. (All changes have been released to PyPI,
of course).

In the process of building these features, I also migrated the plugin away from an old pattern widespread in pretalx
plugins, where all data would be shoved into the key value store – while that kind of data handling makes prototyping
really fast, it's hacky underneath and often leads to problems down the line. Migrating away is not terrible once you
have a template for the data migration, and leads to a much clearer interface. (I do love Django's data migrations a
lot.)

## pretalx

I fixed some tiny documentation bugs, helped out some people who want to contribute to pretalx, and also fixed some
small bugs: Emails required input in *all* languages configured for the event, instead of at least one language (still
not sure what was going on there, but it's fixed). Another bug was related to the complex review system, that didn't get
copied when one event was created from another one.

Oh, and as a small feature: review forms can now be submitted with ctrl+enter. I really should be rolling out this
change to all textareas in all forms! It's a very useful change for those who are used to it.

## pretalx test coverage

Occasionally, I worry about pretalx test coverage – I'm not super consistent at adding tests along with features, so I
tend to go and browse [codecov](https://app.codecov.io/gh/pretalx/pretalx) to see which lines are uncovered and add
tests periodically. I did this for two pretalx apps (`common` and `cfp`), and increased total coverage from 95.01 to
95.60. Not a ton, but improvements do get harder the closer you are to 100%! (A few of these were `pragma: no cover`
lines, but only for really weird edge cases, like testing external email server failures.)

## business stuff

The beginning of the year is rather slow, but I did manage to get my taxes *mostly* done, except for two documents that
have several months left before I have to get them done. I also finished negotiations for a new rather big project, and
discussed a possible side project (secret for now, stay tuned!) with a friend. Nothing much else yet, but the year is
only just beginning.

## Books!

I read a book *every day* that week, but I only wrote a handful of reviews. I finished a long [fanfic
series](https://books.rixx.de/flamethrower/of-a-linear-circle-part-ix-serpent-in-the-grass/) (the ending was a letdown,
but the series was good), read [This Alien Shore](https://books.rixx.de/c-s-friedman/this-alien-shore/) which is
*excellent* worldbuilding around an ehhh story, and re-read [Three Parts
Dead](https://books.rixx.de/max-gladstone/three-parts-dead/), which wasn't as shockingly good the second time around,
but still extremely fun.

## misc

The pandemic is in full swing, here: incidence numbers are soaring, particularly in nearby Berlin, so there's not much
to do. I did meet a friend for a very long walk, which was much needed and very good, and led each of us to go away with
a very long new reading list. I also had some pretty bad sad depressed days, but what can you do.

## What's missing

There is a whole lot I didn't get around to this week: I need to make some changes to venueless that have been
backlogged for MONTHS (yikes). Next week will involve catching up on that stuff, and also doing some work for two
clients (one old, one new).
