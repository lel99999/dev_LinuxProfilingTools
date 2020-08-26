# dev_LinuxProfilingTools
Software Performance Measurements on Linux with Instrumentation and Sampling 

#### Perf

##### Listing Events

##### Listing all currently known events:
`$perf list`<br/>

##### Listing sched tracepoints:
`$perf list 'sched;*'`<br/>

#### Counting Events

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
