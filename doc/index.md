---
layout: default
title: Hexcap/Documentation
---

## NAME
hexcap \- A hex editor for libpcap files.



## SYNOPSIS
hexcap [filename]


## DESCRIPTION
hexcap is an interactive libpcap hex editor, packet generator and capturing tool for Ethernet. It can be used to edit libpcap files, transmit parts of libpcap files, capture packets on Ethernet interfaces, or generate packets from scratch. hexcap supports two modes in its main editor, and a mini-buffer for more complex commands.

## OPTIONS
hexcap can be invoked with no options, or a single filename. Where filename is a libpcap capture file.

## MODES
hexcap supports Navigate and Insert modes, and launches in Navigate mode.In Navigate mode the user cannot modify packet values. In Insert mode the keys [1-9,a-f] change values.

## MAIN EDITOR
**Ctrl-A** Goto beginning of line

**Ctrl-B** Page Up

**Ctrl-F** Page Down

**Ctrl-E** Goto end of line

**Ctrl-K** Yank single packet

**Ctrl-N** Toggle Navigate/Insert modes. See the MODES section for an explanation of modes.

**Ctrl-Q** Quit

**Ctrl-R** Reread file from disk.

**Ctrl-S** Save file

**Ctrl-W** Yank packet(s)

**Ctrl-X** Toggle mini-buffer focus. See the MINI-BUFFER section for a full list of supported commands.

**Ctrl-Y** Paste packet(s)

**Ctrl-Z** Show/Hide the current column

**Ctrl-_** Set mark

**<** Move left one column.

**\>** Move right one column.

**Arrows** Do what you expect(up, down, left, right)

## MINI-BUFFER
The mini-buffer allows invocation of more complex editing commands. It supports tab completion, and basic history.

**Ctrl-X** Toggle mini-buffer focus.

**ESC** Escape mini-buffer focus.

**pkt-min-size** Set minTU. All packets saved or transmitted will be padded to meet minTU.

**pkt-max-size** Set maxTU aka MTU. All packets saved or transmitted will be truncated to meet minTU.

**pkt-size-range** Set both minTU and maxTU. All saved or transmitted packets will be padded or truncated so that (minTU < packet < maxTU).

**save-as-file** Save to a new file and continue working on new file.

**save-file** Save current file.

**interface** Set ethernet interface for transmitting and capturing. [ex. eth0, em1, etc]

**tx-all** Transmit entire buffer. 

**tx-pkt** Transmit single selected packet.

**tx-range** Transmit an inclusive range of packets.

**rx-all** Capture every packet ingressing or egressing the selected interface.

**rx-filter** Capture every packet ingressing or egressing the selected interface that matches the filter given. Filter must be given in Berkeley Packet Filter(BPF) syntax.

**generator** Add a generator to the current section and column. Takes a 'count' and 'step'. 'count' is a positive integer between [1-255]. 'step' is an integer between [-16-16] 

**mask** Add a generator to the current section and column. Takes a single hex 'mask' value. Every zero bit of the mask will iterated over by the generator. A mask cannot contain non-consecutive zero bits.

## Tansmitting
Hexcap can transmit packets on the selected ethernet interface. All tx commands take a 'repeat' argument, where 'repeat' must be between 0-999. If 'repeat' is 0, then transmission will continue until interrupted by the user. hexcap requires superuser access to transmit.

## Capturing
Hexcap can capture packets on the selected ethernet interface. Both rx commands take a 'count' argument, where 'count' must be between 0-999. If 'count' is 0, then capturing will continue until interrupted by the user, or MAX_PACKETS is reached. Currently MAX_PACKETS is set at 9999. hexcap require superuser access to capture.

## Generators and Masks
Hexcap supports the generation of packets using iterators, akin to 'for loops' in imperative programming. Packets are generated at transmission and save time. hexcap allows the setting of masks to place iterators at user defined offsets within headers.

## SEE ALSO
tcpdump(8), tcpreplay(1), wireshark(1), pcap(3), 

## SUPPORT
hexcap supports the following network protocols:

Ethernet(802.2, 802.3, Ethernet II, SNAP), 802.1q, Cisco Discovery Protocol(CDP), Extreme Networks Discovery Protocol(EDP), Spanning Tree Protocol, ARP, IPv4, IPv6, IGMPv1, IGMPv2, ICMP, UDP, and TCP. hexcap does not support libpcapng.

## BUGS
Probably lots.

## AUTHOR
Andrew McConachie (andrewm@ischool.berkeley.edu)


