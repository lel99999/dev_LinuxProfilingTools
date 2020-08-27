# dev_LinuxProfilingTools
Software Performance Measurements on Linux with Instrumentation and Sampling 

#### Perf

##### Listing Events

##### Listing all currently known events:
`$perf list`<br/>

##### Listing sched tracepoints:
`$perf list 'sched;*'`<br/>

#### <ins>Counting Events</ins>

##### cpu counter statistics for the specified command:
`$perf stat command`<br/>

##### Detailed CPU Counter statistics for specified command:
`$perf stat -d command`<br/>

##### CPU counter statistics for the specified PID, until Ctrl-C:
`$perf stat -p PID`<br/>

##### CPU counter statistics for the entire system, for 5 seconds:
`$perf stat -a sleep 5`<br/>

##### Various basic CPU statistics, system wide, for 10 seconds:
`$perf stat -e cycles,instructions,cache-references,cache-misses,bus-cycles -a sleep 10`<br/>

##### Various CPU level 1 data cache statistics for the specified command:
`$perf stat -e L1-dcache-loads,L1-dcache-load-misses,L1-dcache-stores command`<br/>

##### Various CPU data TLB statistics for the specified command:
`$perf stat -e dTLB-loads,dTLB-load-misses,dTLB-prefetch-misses command`<br/>

##### Various CPU last level cache statistics for the specified command:
`$perf stat -e LLC-loads,LLC-load-misses,LLC-stores,LLC-prefetches command`<br/>

##### Using raw PMC counters, eg, counting unhalted core cycles:
`$perf stat -e r003c -a sleep 5 `<br/>

##### PMCs: counting cycles and frontend stalls via raw specification:
`$perf stat -e cycles -e cpu/event=0x0e,umask=0x01,inv,cmask=0x01/ -a sleep 5`<br/>

##### Count syscalls per-second system-wide:
`$perf stat -e raw_syscalls:sys_enter -I 1000 -a`<br/>

##### Count system calls by type for the specified PID, until Ctrl-C:
`$perf stat -e 'syscalls:sys_enter_*' -p PID`<br/>

##### Count system calls by type for the entire system, for 5 seconds:
`$perf stat -e 'syscalls:sys_enter_*' -a sleep 5`<br/>

##### Count scheduler events for the specified PID, until Ctrl-C:
`$perf stat -e 'sched:*' -p PID`<br/>

##### Count scheduler events for the specified PID, for 10 seconds:
`$perf stat -e 'sched:*' -p PID sleep 10`<br/>

##### Count ext4 events for the entire system, for 10 seconds:
`$perf stat -e 'ext4:*' -a sleep 10`<br/>

##### Count block device I/O events for the entire system, for 10 seconds:
`$perf stat -e 'block:*' -a sleep 10`<br/>

##### Count all vmscan events, printing a report every second:
`$perf stat -e 'vmscan:*' -a -I 1000`<br/>
<br/>
#### <ins>Profiling</ins>

##### Sample on-CPU functions for the specified command, at 99 Hertz:
`$perf record -F 99 command`<br/>

##### Sample on-CPU functions for the specified PID, at 99 Hertz, until Ctrl-C:
`$perf record -F 99 -p PID`<br/>

##### Sample on-CPU functions for the specified PID, at 99 Hertz, for 10 seconds:
`$perf record -F 99 -p PID sleep 10`<br/>

##### Sample CPU stack traces (via frame pointers) for the specified PID, at 99 Hertz, for 10 seconds:
`$perf record -F 99 -p PID -g -- sleep 10`<br/>

##### Sample CPU stack traces for the PID, using dwarf (dbg info) to unwind stacks, at 99 Hertz, for 10 seconds:
`$perf record -F 99 -p PID --call-graph dwarf sleep 10`<br/>

##### Sample CPU stack traces for the entire system, at 99 Hertz, for 10 seconds (< Linux 4.11):
`$perf record -F 99 -ag -- sleep 10`<br/>

##### Sample CPU stack traces for the entire system, at 99 Hertz, for 10 seconds (>= Linux 4.11):
`$perf record -F 99 -g -- sleep 10`<br/>

##### If the previous command didn't work, try forcing perf to use the cpu-clock event:
`$perf record -F 99 -e cpu-clock -ag -- sleep 10`<br/>

##### Sample CPU stack traces for a container identified by its /sys/fs/cgroup/perf_event cgroup:
`$perf record -F 99 -e cpu-clock --cgroup=docker/1d567f4393190204...etc... -a -- sleep 10`<br/>

##### Sample CPU stack traces for the entire system, with dwarf stacks, at 99 Hertz, for 10 seconds:
`$perf record -F 99 -a --call-graph dwarf sleep 10`<br/>

##### Sample CPU stack traces for the entire system, using last branch record for stacks, ... (>= Linux 4.?):
`$perf record -F 99 -a --call-graph lbr sleep 10`<br/>

##### Sample CPU stack traces, once every 10,000 Level 1 data cache misses, for 5 seconds:
`$perf record -e L1-dcache-load-misses -c 10000 -ag -- sleep 5`<br/>

##### Sample CPU stack traces, once every 100 last level cache misses, for 5 seconds:
`$perf record -e LLC-load-misses -c 100 -ag -- sleep 5 `<br/>

##### Sample on-CPU kernel instructions, for 5 seconds:
`$perf record -e cycles:k -a -- sleep 5 `<br/>

##### Sample on-CPU user instructions, for 5 seconds:
`$perf record -e cycles:u -a -- sleep 5 `<br/>

##### Sample on-CPU user instructions precisely (using PEBS), for 5 seconds:
`$perf record -e cycles:up -a -- sleep 5 `<br/>

##### Perform branch tracing (needs HW support), for 1 second:
`$perf record -b -a sleep 1`<br/>

##### Sample CPUs at 49 Hertz, and show top addresses and symbols, live (no perf.data file):
`$perf top -F 49`<br/>

##### Sample CPUs at 49 Hertz, and show top process names and segments, live:
`$perf top -F 49 -ns comm,dso`<br/>
<br/>
#### <ins>Static Tracing</ins>
##### Trace new processes, until Ctrl-C:
`$perf record -e sched:sched_process_exec -a`<br/>

##### Sample (take a subset of) context-switches, until Ctrl-C:
`$perf record -e context-switches -a`<br/>

##### Trace all context-switches, until Ctrl-C:
`$perf record -e context-switches -c 1 -a`<br/>

##### Include raw settings used (see: man perf_event_open):
`$perf record -vv -e context-switches -a`<br/>

##### Trace all context-switches via sched tracepoint, until Ctrl-C:
`$perf record -e sched:sched_switch -a`<br/>

##### Sample context-switches with stack traces, until Ctrl-C:
`$perf record -e context-switches -ag`<br/>

##### Sample context-switches with stack traces, for 10 seconds:
`$perf record -e context-switches -ag -- sleep 10`<br/>

##### Sample CS, stack traces, and with timestamps (< Linux 3.17, -T now default):
`$perf record -e context-switches -ag -T`<br/>

##### Sample CPU migrations, for 10 seconds:
`$perf record -e migrations -a -- sleep 10`<br/>

##### Trace all connect()s with stack traces (outbound connections), until Ctrl-C:
`$perf record -e syscalls:sys_enter_connect -ag`<br/>

##### Trace all accepts()s with stack traces (inbound connections), until Ctrl-C:
`$perf record -e syscalls:sys_enter_accept* -ag`<br/>

##### Trace all block device (disk I/O) requests with stack traces, until Ctrl-C:
`$perf record -e block:block_rq_insert -ag`<br/>

##### Sample at most 100 block device requests per second, until Ctrl-C:
`$perf record -F 100 -e block:block_rq_insert -a`<br/>

##### Trace all block device issues and completions (has timestamps), until Ctrl-C:
`$perf record -e block:block_rq_issue -e block:block_rq_complete -a`<br/>

##### Trace all block completions, of size at least 100 Kbytes, until Ctrl-C:
`$perf record -e block:block_rq_complete --filter 'nr_sector > 200'`<br/>

##### Trace all block completions, synchronous writes only, until Ctrl-C:
`$perf record -e block:block_rq_complete --filter 'rwbs == "WS"'`<br/>

##### Trace all block completions, all types of writes, until Ctrl-C:
`$perf record -e block:block_rq_complete --filter 'rwbs ~ "*W*"'`<br/>

##### Sample minor faults (RSS growth) with stack traces, until Ctrl-C:
`$perf record -e minor-faults -ag`<br/>

##### Trace all minor faults with stack traces, until Ctrl-C:
`$perf record -e minor-faults -c 1 -ag`<br/>

##### Sample page faults with stack traces, until Ctrl-C:
`$perf record -e page-faults -ag`<br/>

##### Trace all ext4 calls, and write to a non-ext4 location, until Ctrl-C:
`$perf record -e 'ext4:*' -o /tmp/perf.data -a `<br/>

##### Trace kswapd wakeup events, until Ctrl-C:
`$perf record -e vmscan:mm_vmscan_wakeup_kswapd -ag`<br/>

##### Add Node.js USDT probes (Linux 4.10+):
`$perf buildid-cache --add `which node``<br/>

##### Trace the node http__server__request USDT event (Linux 4.10+):
`$perf record -e sdt_node:http__server__request -a`<br/>

<br/>
#### <ins>Dynamic Tracing</ins>
##### Add a tracepoint for the kernel tcp_sendmsg() function entry ("--add" is optional):
`$perf probe --add tcp_sendmsg`<br/>

##### Remove the tcp_sendmsg() tracepoint (or use "--del"):
`$perf probe -d tcp_sendmsg`<br/>

##### Add a tracepoint for the kernel tcp_sendmsg() function return:
`$perf probe 'tcp_sendmsg%return'`<br/>

##### Show available variables for the kernel tcp_sendmsg() function (needs debuginfo):
`$perf probe -V tcp_sendmsg`<br/>

##### Show available variables for the kernel tcp_sendmsg() function, plus external vars (needs debuginfo):
`$perf probe -V tcp_sendmsg --externs`<br/>

##### Show available line probes for tcp_sendmsg() (needs debuginfo):
`$perf probe -L tcp_sendmsg`<br/>

##### Show available variables for tcp_sendmsg() at line number 81 (needs debuginfo):
`$perf probe -V tcp_sendmsg:81`<br/>

##### Add a tracepoint for tcp_sendmsg(), with three entry argument registers (platform specific):
`$perf probe 'tcp_sendmsg %ax %dx %cx'`<br/>

##### Add a tracepoint for tcp_sendmsg(), with an alias ("bytes") for the %cx register (platform specific):
`$perf probe 'tcp_sendmsg bytes=%cx'`<br/>

##### Trace previously created probe when the bytes (alias) variable is greater than 100:
`$perf record -e probe:tcp_sendmsg --filter 'bytes > 100'`<br/>

##### Add a tracepoint for tcp_sendmsg() return, and capture the return value:
`$perf probe 'tcp_sendmsg%return $retval'`<br/>

##### Add a tracepoint for tcp_sendmsg(), and "size" entry argument (reliable, but needs debuginfo):
`$perf probe 'tcp_sendmsg size'`<br/>

##### Add a tracepoint for tcp_sendmsg(), with size and socket state (needs debuginfo):
`$perf probe 'tcp_sendmsg size sk->__sk_common.skc_state'`<br/>

##### Tell me how on Earth you would do this, but don't actually do it (needs debuginfo):
`$perf probe -nv 'tcp_sendmsg size sk->__sk_common.skc_state'`<br/>

##### Trace previous probe when size is non-zero, and state is not TCP_ESTABLISHED(1) (needs debuginfo):
`$perf record -e probe:tcp_sendmsg --filter 'size > 0 && skc_state != 1' -a`<br/>

##### Add a tracepoint for tcp_sendmsg() line 81 with local variable seglen (needs debuginfo):
`$perf probe 'tcp_sendmsg:81 seglen'`<br/>

##### Add a tracepoint for do_sys_open() with the filename as a string (needs debuginfo):
`$perf probe 'do_sys_open filename:string'`<br/>

##### Add a tracepoint for myfunc() return, and include the retval as a string:
`$perf probe 'myfunc%return +0($retval):string'`<br/>

##### Add a tracepoint for the user-level malloc() function from libc:
`$perf probe -x /lib64/libc.so.6 malloc`<br/>

##### Add a tracepoint for this user-level static probe (USDT, aka SDT event):
`$perf probe -x /usr/lib64/libpthread-2.24.so %sdt_libpthread:mutex_entry`<br/>

##### List currently available dynamic probes:
`$perf probe -l`<br/>

<br/>
#### <ins>Mixed</ins>
##### Trace system calls by process, showing a summary refreshing every 2 seconds:
`$perf top -e raw_syscalls:sys_enter -ns comm`<br/>

##### Trace sent network packets by on-CPU process, rolling output (no clear):
`$stdbuf -oL perf top -e net:net_dev_xmit -ns comm | strings`<br/>

##### Sample stacks at 99 Hertz, and, context switches:
`$perf record -F99 -e cpu-clock -e cs -a -g `<br/>

##### Sample stacks to 2 levels deep, and, context switch stacks to 5 levels (needs 4.8):
`$perf record -F99 -e cpu-clock/max-stack=2/ -e cs/max-stack=5/ -a -g `<br/>

<br/>
#### <ins>Special</ins>
##### Record cacheline events (Linux 4.10+):
`$perf c2c record -a -- sleep 10`<br/>

##### Report cacheline events from previous recording (Linux 4.10+):
`$perf c2c report`<br/>

<br/>
#### <ins>Reporting</ins>
##### Show perf.data in an ncurses browser (TUI) if possible:
`$perf report`<br/>

##### Show perf.data with a column for sample count:
`$perf report -n`<br/>

##### Show perf.data as a text report, with data coalesced and percentages:
`$perf report --stdio`<br/>

##### Report, with stacks in folded format: one line per stack (needs 4.4):
`$perf report --stdio -n -g folded`<br/>

##### List all events from perf.data:
`$perf script`<br/>

##### List all perf.data events, with data header (newer kernels; was previously default):
`$perf script --header`<br/>

##### List all perf.data events, with customized fields (< Linux 4.1):
`$perf script -f time,event,trace`<br/>

##### List all perf.data events, with customized fields (>= Linux 4.1):
`$perf script -F time,event,trace`<br/>

##### List all perf.data events, with my recommended fields (needs record -a; newer kernels):
`$perf script --header -F comm,pid,tid,cpu,time,event,ip,sym,dso `<br/>

##### List all perf.data events, with my recommended fields (needs record -a; older kernels):
`$perf script -f comm,pid,tid,cpu,time,event,ip,sym,dso`<br/>

##### Dump raw contents from perf.data as hex (for debugging):
`$perf script -D`<br/>

##### Disassemble and annotate instructions with percentages (needs some debuginfo):
`$perf annotate --stdio`<br/>

<br/>
