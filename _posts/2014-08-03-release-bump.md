---
layout: post
title: "Release Bump"
date:   2014-08-03 23:00
---
It's time to bump the release of hexcap to 0.2. I doubt I can even remember all of the changes that I have made in the past couple of months. Here are the major ones. Most of the changes were on the [todo list](/todo), and are now marked off.

Some changes between hexcap 0.1 and 0.2:

* Transmit packets with mini-buffer commands tx-all, tx-pkt and tx-range.

* Capture packets with mini-buffer commands rx-all and rx-filter.

* Generate packets with mini-buffer commands generator and mask.

* Mini-buffer now supports basic command history.

* Can invoke without filename. It gives you a default packet to edit.

* Many improvements to the man file.

* Removed any semblance of support for a precompiled binary. It was more trouble than it was worth.

* Changed dev environment from Debian to [OpenBSD 5.5](http://www.openbsd.org/)

* Changed license from GPL to [BSD 3 clause](http://opensource.org/licenses/BSD-3-Clause)

See the [man page](/doc/) for more information on new functionality. The plan is also to make a couple videos that explain hexcap in more detail.